"""Test classes in devices module"""

import unittest

from aind_data_schema_models.devices import (
    AdditionalImagingDevice,
    DataInterface,
    Detector,
    DetectorType,
    Device,
    HarpDevice,
    ImagingDeviceType,
    ImmersionMedium,
    Objective,
    RewardSpout,
    SpoutSide,
)
from aind_data_schema_models.harp_types import HarpDeviceType
from aind_data_schema_models.organizations import Organization
from tests import PYD_VERSION


class TestDevices(unittest.TestCase):
    """tests device schemas"""

    def test_other_validators(self):
        """tests validators which require notes when an instance of 'other' is used"""

        with self.assertRaises(ValueError) as e1:
            RewardSpout(
                name="test_reward_spout",
                spout_diameter=0.5,
                solenoid_valve=Device(
                    device_type="solenoid",
                    name="test_solenoid",
                ),
                side=SpoutSide.OTHER,
            )

        expected_e1 = (
            "1 validation error for RewardSpout\n"
            "  Value error, Notes cannot be empty if spout side is Other."
            " Describe the spout side in the notes field."
            " [type=value_error, input_value={'name': 'test_reward_spo...outSide.OTHER: 'Other'>}, input_type=dict]\n"
            f"    For further information visit https://errors.pydantic.dev/{PYD_VERSION}/v/value_error"
        )

        self.assertEqual(repr(e1.exception), expected_e1)

        with self.assertRaises(ValueError) as e2:
            Detector(
                name="test_detector",
                manufacturer=Organization.HAMAMATSU,
                detector_type=DetectorType.OTHER,
                immersion=ImmersionMedium.OTHER,
                data_interface=DataInterface.OTHER,
            )

        expected_e2 = (
            "1 validation error for Detector\n"
            "  Value error, Notes cannot be empty while any of the following fields"
            " are set to 'other': ['immersion', 'detector_type', 'data_interface']"
            " [type=value_error, input_value={'name': 'test_detector',...terface.OTHER: 'Other'>}, input_type=dict]\n"
            f"    For further information visit https://errors.pydantic.dev/{PYD_VERSION}/v/value_error"
        )

        self.assertEqual(repr(e2.exception), expected_e2)

        with self.assertRaises(ValueError) as e3:
            HarpDevice(
                name="test_harp",
                computer_name="test_harp_computer",
                harp_device_type=HarpDeviceType.BEHAVIOR,
                data_interface=DataInterface.OTHER,
                is_clock_generator=False,
            )

        expected_e3 = (
            "1 validation error for HarpDevice\n"
            "  Value error, Notes cannot be empty if data_interface is Other."
            " Describe the data interface in the notes field."
            " [type=value_error, input_value={'name': 'test_harp', 'co...clock_generator': False}, input_type=dict]\n"
            f"    For further information visit https://errors.pydantic.dev/{PYD_VERSION}/v/value_error"
        )

        self.assertEqual(repr(e3.exception), expected_e3)

        HarpDevice(
            name="test_harp",
            computer_name="test_harp_computer",
            harp_device_type=HarpDeviceType.BEHAVIOR,
            data_interface=DataInterface.USB,
            is_clock_generator=False,
        )

        with self.assertRaises(ValueError) as e4:
            Objective(name="test_objective", numerical_aperture=0.5, magnification=10, immersion=ImmersionMedium.OTHER)

        expected_e4 = (
            "1 validation error for Objective\n"
            "  Value error, Notes cannot be empty if immersion is Other. Describe the immersion in the notes field."
            " [type=value_error, input_value={'name': 'test_objective'...nMedium.OTHER: 'other'>}, input_type=dict]\n"
            f"    For further information visit https://errors.pydantic.dev/{PYD_VERSION}/v/value_error"
        )

        self.assertEqual(repr(e4.exception), expected_e4)

        with self.assertRaises(ValueError) as e5:
            AdditionalImagingDevice(name="test_additional_imaging", imaging_device_type=ImagingDeviceType.OTHER)

        expected_e5 = (
            "1 validation error for AdditionalImagingDevice\n"
            "  Value error, Notes cannot be empty if imaging_device_type is Other. "
            "Describe the imaging device type in the notes field."
            " [type=value_error, input_value={'name': 'test_additional...iceType.OTHER: 'Other'>}, input_type=dict]\n"
            f"    For further information visit https://errors.pydantic.dev/{PYD_VERSION}/v/value_error"
        )

        self.assertEqual(repr(e5.exception), expected_e5)

    def test_detector(self):
        """Tests class constructor for detector class"""

        detector = Detector(
            name="test_detector",
            manufacturer=Organization.HAMAMATSU,
            detector_type=DetectorType.CAMERA,
            immersion=ImmersionMedium.AIR,
            data_interface=DataInterface.USB,
        )
        self.assertEqual("test_detector", detector.name)
        self.assertEqual(Organization.HAMAMATSU, detector.manufacturer)
        self.assertEqual(DetectorType.CAMERA, detector.detector_type)
        self.assertEqual(ImmersionMedium.AIR, detector.immersion)
        self.assertEqual(DataInterface.USB, detector.data_interface)

    def test_objective(self):
        """Tests class constructor for objective class"""

        objective = Objective(
            name="test_objective", numerical_aperture=0.5, magnification=10, immersion=ImmersionMedium.AIR
        )
        self.assertEqual("test_objective", objective.name)
        self.assertEqual(0.5, objective.numerical_aperture)
        self.assertEqual(10, objective.magnification)
        self.assertEqual(ImmersionMedium.AIR, objective.immersion)

    def test_reward_spout(self):
        """Tests class constructor for RewardSpout class"""

        solenoid_valve = Device(
            device_type="solenoid",
            name="test_solenoid",
        )

        reward_spout = RewardSpout(
            name="test_reward_spout",
            spout_diameter=0.5,
            solenoid_valve=Device(
                device_type="solenoid",
                name="test_solenoid",
            ),
            side=SpoutSide.LEFT,
        )
        self.assertEqual("test_reward_spout", reward_spout.name)
        self.assertEqual(0.5, reward_spout.spout_diameter)
        self.assertEqual(solenoid_valve, reward_spout.solenoid_valve)
        self.assertEqual(SpoutSide.LEFT, reward_spout.side)

    def test_additional_imaging_device(self):
        """Tests class constructor for AdditionalImagingDevice class"""

        imaging_device = AdditionalImagingDevice(
            name="test_additional_imaging", imaging_device_type=ImagingDeviceType.GALVO
        )
        self.assertEqual("test_additional_imaging", imaging_device.name)
        self.assertEqual(ImagingDeviceType.GALVO, imaging_device.imaging_device_type)


if __name__ == "__main__":
    unittest.main()
