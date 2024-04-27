"""Tests methods in base module."""

import unittest
from datetime import datetime, timezone

from pydantic import create_model

from aind_data_schema_models.base import AwareDatetimeWithDefault


class BaseTests(unittest.TestCase):
    """tests for the base module"""

    def test_aware_datetime_with_default(self):
        """Tests AwareDatetimeWithDefault adds tzinfo as default"""

        test_model = create_model("TempModel", dt=(AwareDatetimeWithDefault, ...))
        datetime_without_tz = datetime(2020, 10, 10, 1, 2, 3)
        expected_dt = datetime(2020, 10, 10, 1, 2, 3).astimezone()
        model_instance = test_model(dt=datetime_without_tz)

        # Verify that a timezone was attached if not supplied.
        self.assertEqual(expected_dt, model_instance.dt)

    def test_aware_datetime_with_setting(self):
        """Tests AwareDatetimeWithDefault honors timezone input by user"""

        test_model = create_model("TempModel", dt=(AwareDatetimeWithDefault, ...))
        datetime_with_tz = datetime(2020, 10, 10, 1, 2, 3, tzinfo=timezone.utc)
        model_instance = test_model(dt=datetime_with_tz)

        expected_json = '{"dt":"2020-10-10T01:02:03Z"}'
        self.assertEqual(expected_json, model_instance.model_dump_json())


if __name__ == "__main__":
    unittest.main()
