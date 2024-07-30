"""Tests for utils module"""

import json
import os
import unittest
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from aind_data_schema_models import utils

TEST_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


class TestUtils(unittest.TestCase):
    """Tests methods in utils module"""

    def test_read_csv(self):
        """Tests read csv method"""

        harp_types_dict = utils.read_csv(TEST_DIR / "harp_types.csv")
        expected_harp_types_dict = [
            {"name": "Behavior", "whoami": "1216"},
            {"name": "Cuttlefish", "whoami": "1403"},
            {"name": "Treadmill", "whoami": "1402"},
        ]
        self.assertEqual(expected_harp_types_dict, harp_types_dict)

    def test_create_model_class_name(self):
        """Tests method removes punctuation and white space from strings."""

        self.assertEqual("HelloWorld", utils.create_model_class_name("HELLO_WORLD"))
        self.assertEqual("HelloWorld", utils.create_model_class_name("HELLO WORLD!"))
        self.assertEqual("HelloWorld1", utils.create_model_class_name("HELLO # WORLD! 1"))

    def test_create_literal_model(self):
        """Tests create_literal_model method"""

        class HarpDeviceTypeModel(BaseModel):
            """Base model config"""

            model_config = ConfigDict(frozen=True)
            name: str = Field(..., title="Harp device type name")
            whoami: int = Field(..., title="Harp whoami value")

        harp_types_dict = utils.read_csv(TEST_DIR / "harp_types.csv")
        behavior_model = utils.create_literal_model(
            obj=harp_types_dict[0],
            base_model=HarpDeviceTypeModel,
            discriminator="name",
            class_module=__name__,
        )
        expected_behavior_schema = {
            "properties": {
                "name": {
                    "const": "Behavior",
                    "default": "Behavior",
                    "enum": ["Behavior"],
                    "title": "Name",
                    "type": "string",
                },
                "whoami": {"const": "1216", "default": "1216", "enum": ["1216"], "title": "Whoami", "type": "string"},
            },
            "title": "Behavior",
            "type": "object",
        }
        self.assertEqual(expected_behavior_schema, behavior_model.model_json_schema())

    def test_create_literal_class(self):
        """Tests create_literal_class method"""

        class HarpDeviceTypeModel(BaseModel):
            """Base model config"""

            model_config = ConfigDict(frozen=True)
            name: str = Field(..., title="Harp device type name")
            whoami: int = Field(..., title="Harp whoami value")

        harp_types_dict = utils.read_csv(TEST_DIR / "harp_types.csv")
        HarpDeviceType = utils.create_literal_class(
            objects=harp_types_dict,
            class_name="HarpDeviceType",
            base_model=HarpDeviceTypeModel,
            discriminator="name",
            class_module=__name__,
        )
        self.assertEqual("Behavior", HarpDeviceType.Behavior.name)
        self.assertEqual("1216", HarpDeviceType.Behavior.whoami)
        self.assertEqual("Cuttlefish", HarpDeviceType.Cuttlefish.name)
        self.assertEqual("1403", HarpDeviceType.Cuttlefish.whoami)
        self.assertEqual("Treadmill", HarpDeviceType.Treadmill.name)
        self.assertEqual("1402", HarpDeviceType.Treadmill.whoami)

    def test_one_of_instances(self):
        """Tests one_of_instance method"""

        class HarpDeviceTypeModel(BaseModel):
            """Base model config"""

            model_config = ConfigDict(frozen=True)
            name: str = Field(..., title="Harp device type name")
            whoami: int = Field(..., title="Harp whoami value")

        harp_types_dict = utils.read_csv(TEST_DIR / "harp_types.csv")
        HarpDeviceType = utils.create_literal_class(
            objects=harp_types_dict,
            class_name="HarpDeviceType",
            base_model=HarpDeviceTypeModel,
            discriminator="name",
            class_module=__name__,
        )
        annotated_list = utils.one_of_instance([HarpDeviceType.Cuttlefish, HarpDeviceType.Treadmill])

        class Model(BaseModel):
            """A small model to test the annotated list field"""

            my_choice: annotated_list

        with self.assertRaises(ValidationError) as e:
            Model(my_choice=HarpDeviceType.Behavior)

        expected_error_message = (
            "Input tag 'Behavior' found using 'name' does not match any of the "
            "expected tags: 'Cuttlefish', 'Treadmill'"
        )

        model_instance = Model(my_choice=HarpDeviceType.Cuttlefish)

        deserialized_model = Model.model_validate_json(model_instance.model_dump_json())

        self.assertEqual(json.loads(e.exception.json())[0]["msg"], expected_error_message)

        self.assertEqual(deserialized_model, model_instance)


if __name__ == "__main__":
    unittest.main()
