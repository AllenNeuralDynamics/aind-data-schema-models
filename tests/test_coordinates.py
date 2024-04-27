"""Tests classes in coordinates module"""

import json
import unittest
from decimal import Decimal

from pydantic import ValidationError

from aind_data_schema_models.coordinates import (
    Affine3dTransform,
    AnatomicalDirection,
    Axis,
    AxisName,
    CcfCoords,
    CcfVersion,
    Coordinates3d,
    CoordinateTransform,
    ImageAxis,
    ModuleOrientation2d,
    ModuleOrientation3d,
    Orientation3d,
    Origin,
    RelativePosition,
    Rotation3dTransform,
    Scale3dTransform,
    Size2d,
    Size3d,
    Translation3dTransform,
)
from aind_data_schema_models.units import AngleUnit, SizeUnit
from tests import PYD_VERSION


class TestCcfVersion(unittest.TestCase):
    """Tests CcfVersion"""

    def test_ccf_version(self):
        """Test for enum construction"""
        self.assertEqual(CcfVersion.CCFv3, CcfVersion("CCFv3"))


class TestOrigin(unittest.TestCase):
    """Tests Origin"""

    def test_origin(self):
        """Test for enum construction"""
        self.assertEqual(Origin.BREGMA, Origin("Bregma"))


class TestAxisName(unittest.TestCase):
    """Tests AxisName"""

    def test_axis_name(self):
        """Test for enum construction"""
        self.assertEqual(AxisName.X, AxisName("X"))


class TestAnatomicalDirection(unittest.TestCase):
    """Tests AnatomicalDirection"""

    def test_anatomical_direction(self):
        """Test for enum construction"""
        self.assertEqual(AnatomicalDirection.LR, AnatomicalDirection("Left_to_right"))


class TestCoordinateTransform(unittest.TestCase):
    """Tests CoordinateTransform"""

    def test_coordinate_transform(self):
        """Test for model construction"""
        coordinate_transform = CoordinateTransform(type="affine")
        self.assertIsNotNone(coordinate_transform)


class TestScale3dTransform(unittest.TestCase):
    """Tests Scale3dTransform"""

    def test_scale_3d_transform(self):
        """Test for model construction"""
        transform = Scale3dTransform(scale=[Decimal("0.5"), Decimal("0.6"), Decimal("0.7")])
        self.assertEqual("scale", transform.type)
        self.assertEqual([Decimal("0.5"), Decimal("0.6"), Decimal("0.7")], transform.scale)

    def test_invalid_scale_3d_transform(self):
        """Tests validation error is raised if scale list doesn't have 3 items"""

        with self.assertRaises(ValidationError) as e:
            Scale3dTransform(scale=[Decimal("0.5"), Decimal("0.6")])

        expected_errors = [
            {
                "type": "too_short",
                "loc": ["scale"],
                "msg": "List should have at least 3 items after validation, not 2",
                "input": ["0.5", "0.6"],
                "ctx": {"field_type": "List", "min_length": 3, "actual_length": 2},
                "url": f"https://errors.pydantic.dev/{PYD_VERSION}/v/too_short",
            }
        ]
        self.assertEqual(expected_errors, json.loads(e.exception.json()))


class TestTranslation3dTransform(unittest.TestCase):
    """Tests Translation3dTransform"""

    def test_translation_3d_transform(self):
        """Test for model construction"""
        transform = Translation3dTransform(translation=[Decimal("0.5"), Decimal("0.6"), Decimal("0.7")])
        self.assertEqual("translation", transform.type)
        self.assertEqual([Decimal("0.5"), Decimal("0.6"), Decimal("0.7")], transform.translation)

    def test_invalid_translation_3d_transform(self):
        """Tests validation error is raised if translation list doesn't have 3 items"""

        with self.assertRaises(ValidationError) as e:
            Translation3dTransform(translation=[Decimal("0.5"), Decimal("0.6")])

        expected_errors = [
            {
                "type": "too_short",
                "loc": ["translation"],
                "msg": "List should have at least 3 items after validation, not 2",
                "input": ["0.5", "0.6"],
                "ctx": {"field_type": "List", "min_length": 3, "actual_length": 2},
                "url": f"https://errors.pydantic.dev/{PYD_VERSION}/v/too_short",
            }
        ]
        self.assertEqual(expected_errors, json.loads(e.exception.json()))


class TestRotation3dTransform(unittest.TestCase):
    """Tests Rotation3dTransform"""

    def test_rotation_3d_transform(self):
        """Test for model construction"""
        given_rotation = [
            Decimal("0.0"),
            Decimal("0.1"),
            Decimal("0.2"),
            Decimal("1.0"),
            Decimal("1.1"),
            Decimal("1.2"),
            Decimal("2.0"),
            Decimal("2.1"),
            Decimal("2.2"),
        ]
        transform = Rotation3dTransform(rotation=given_rotation)
        self.assertEqual("rotation", transform.type)
        self.assertEqual(given_rotation, transform.rotation)

    def test_invalid_translation_3d_transform(self):
        """Tests validation error is raised if rotation list doesn't have 9 items"""

        given_rotation = [
            Decimal("0.0"),
            Decimal("0.1"),
            Decimal("0.2"),
            Decimal("1.0"),
            Decimal("1.1"),
            Decimal("1.2"),
            Decimal("2.0"),
            Decimal("2.1"),
        ]

        with self.assertRaises(ValidationError) as e:
            Rotation3dTransform(rotation=given_rotation)

        expected_errors = [
            {
                "type": "too_short",
                "loc": ["rotation"],
                "msg": "List should have at least 9 items after validation, not 8",
                "input": [str(d) for d in given_rotation],
                "ctx": {"field_type": "List", "min_length": 9, "actual_length": 8},
                "url": f"https://errors.pydantic.dev/{PYD_VERSION}/v/too_short",
            }
        ]
        self.assertEqual(expected_errors, json.loads(e.exception.json()))


class TestAffine3dTransform(unittest.TestCase):
    """Tests Affine3dTransform"""

    def test_affine_3d_transform(self):
        """Test for model construction"""
        given_affine_transform = [
            Decimal("0.0"),
            Decimal("0.1"),
            Decimal("0.2"),
            Decimal("0.3"),
            Decimal("1.0"),
            Decimal("1.1"),
            Decimal("1.2"),
            Decimal("1.3"),
            Decimal("2.0"),
            Decimal("2.1"),
            Decimal("2.2"),
            Decimal("2.3"),
        ]
        transform = Affine3dTransform(affine_transform=given_affine_transform)
        self.assertEqual("affine", transform.type)
        self.assertEqual(given_affine_transform, transform.affine_transform)

    def test_invalid_affine_3d_transform(self):
        """Tests validation error is raised if affine_transform list doesn't have 12 items"""

        given_affine_transform = [
            Decimal("0.0"),
            Decimal("0.1"),
            Decimal("0.2"),
            Decimal("0.3"),
            Decimal("1.0"),
            Decimal("1.1"),
            Decimal("1.2"),
            Decimal("1.3"),
            Decimal("2.0"),
            Decimal("2.1"),
            Decimal("2.2"),
        ]

        with self.assertRaises(ValidationError) as e:
            Affine3dTransform(affine_transform=given_affine_transform)

        expected_errors = [
            {
                "type": "too_short",
                "loc": ["affine_transform"],
                "msg": "List should have at least 12 items after validation, not 11",
                "input": [str(d) for d in given_affine_transform],
                "ctx": {"field_type": "List", "min_length": 12, "actual_length": 11},
                "url": f"https://errors.pydantic.dev/{PYD_VERSION}/v/too_short",
            }
        ]
        self.assertEqual(expected_errors, json.loads(e.exception.json()))


class TestSize2d(unittest.TestCase):
    """Tests Size2d"""

    def test_size_2d(self):
        """Test for model construction"""

        size = Size2d(width=1, height=2)
        self.assertEqual(SizeUnit.PX, size.unit)
        self.assertEqual(1, size.width)
        self.assertEqual(2, size.height)


class TestSize3d(unittest.TestCase):
    """Tests Size3d"""

    def test_size_3d(self):
        """Test for model construction"""

        size = Size3d(width=1, height=2, length=3)
        self.assertEqual(SizeUnit.M, size.unit)
        self.assertEqual(1, size.width)
        self.assertEqual(2, size.height)
        self.assertEqual(3, size.length)


class TestOrientation3d(unittest.TestCase):
    """Tests Orientation3d"""

    def test_orientation_3d(self):
        """Test for model construction"""

        orientation = Orientation3d(pitch=Decimal("0.1"), yaw=Decimal("0.2"), roll=Decimal("0.3"))
        self.assertEqual(AngleUnit.DEG, orientation.unit)
        self.assertEqual(Decimal("0.1"), orientation.pitch)
        self.assertEqual(Decimal("0.2"), orientation.yaw)
        self.assertEqual(Decimal("0.3"), orientation.roll)


class TestModuleOrientation2d(unittest.TestCase):
    """Tests ModuleOrientation2d"""

    def test_module_orientation_2d(self):
        """Test for model construction"""

        orientation = ModuleOrientation2d(arc_angle=Decimal("0.1"), module_angle=Decimal("0.2"))
        self.assertEqual(AngleUnit.DEG, orientation.unit)
        self.assertEqual(Decimal("0.1"), orientation.arc_angle)
        self.assertEqual(Decimal("0.2"), orientation.module_angle)


class TestModuleOrientation3d(unittest.TestCase):
    """Tests ModuleOrientation3d"""

    def test_module_orientation_3d(self):
        """Test for model construction"""

        orientation = ModuleOrientation3d(
            arc_angle=Decimal("0.1"), module_angle=Decimal("0.2"), rotation_angle=Decimal("0.3")
        )
        self.assertEqual(AngleUnit.DEG, orientation.unit)
        self.assertEqual(Decimal("0.1"), orientation.arc_angle)
        self.assertEqual(Decimal("0.2"), orientation.module_angle)
        self.assertEqual(Decimal("0.3"), orientation.rotation_angle)


class TestCoordinates3d(unittest.TestCase):
    """Tests Coordinates3d"""

    def test_coordinates_3d(self):
        """Test for model construction"""

        coordinates = Coordinates3d(x=Decimal("0.1"), y=Decimal("0.2"), z=Decimal("0.3"))
        self.assertEqual(SizeUnit.UM, coordinates.unit)
        self.assertEqual(Decimal("0.1"), coordinates.x)
        self.assertEqual(Decimal("0.2"), coordinates.y)
        self.assertEqual(Decimal("0.3"), coordinates.z)


class TestCcfCoords(unittest.TestCase):
    """Tests CcfCoords"""

    def test_ccf_coords(self):
        """Test for model construction"""

        coordinates = CcfCoords(ml=Decimal("0.1"), ap=Decimal("0.2"), dv=Decimal("0.3"))
        self.assertEqual(SizeUnit.UM, coordinates.unit)
        self.assertEqual(CcfVersion.CCFv3, coordinates.ccf_version)
        self.assertEqual(Decimal("0.1"), coordinates.ml)
        self.assertEqual(Decimal("0.2"), coordinates.ap)
        self.assertEqual(Decimal("0.3"), coordinates.dv)


class TestAxis(unittest.TestCase):
    """Tests Axis"""

    def test_axis(self):
        """Test for model construction"""

        axis = Axis(name=AxisName.X, direction="Positive")
        self.assertEqual(AxisName.X, axis.name)
        self.assertEqual("Positive", axis.direction)


class TestImageAxis(unittest.TestCase):
    """Tests ImageAxis"""

    def test_image_axis(self):
        """Test for model construction"""

        axis = ImageAxis(name=AxisName.X, direction=AnatomicalDirection.LR, dimension=1)
        self.assertEqual(AxisName.X, axis.name)
        self.assertEqual(AnatomicalDirection.LR, axis.direction)
        self.assertEqual(1, axis.dimension)


class TestRelativePosition(unittest.TestCase):
    """Tests RelativePosition"""

    def test_relative_position(self):
        """Test for model construction"""

        given_rotation = [
            Decimal("0.0"),
            Decimal("0.1"),
            Decimal("0.2"),
            Decimal("1.0"),
            Decimal("1.1"),
            Decimal("1.2"),
            Decimal("2.0"),
            Decimal("2.1"),
            Decimal("2.2"),
        ]
        rotation_transform = Rotation3dTransform(rotation=given_rotation)
        translation_transform = Translation3dTransform(translation=[Decimal("0.5"), Decimal("0.6"), Decimal("0.7")])

        device_position_transformations = [
            translation_transform,
            rotation_transform,
        ]
        device_axes = [
            Axis(name=AxisName.X, direction="Left to Right"),
            Axis(name=AxisName.Y, direction="Front to Back"),
            Axis(name=AxisName.Z, direction="Down to Up"),
        ]

        position = RelativePosition(
            device_position_transformations=device_position_transformations,
            device_origin="Center",
            device_axes=device_axes,
        )
        self.assertIsNone(position.notes)
        self.assertEqual("Center", position.device_origin)
        self.assertEqual(device_position_transformations, position.device_position_transformations)
        self.assertEqual(device_axes, position.device_axes)


if __name__ == "__main__":
    unittest.main()
