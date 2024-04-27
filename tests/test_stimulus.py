"""Test classes in stimulus module"""

import unittest
from decimal import Decimal

from aind_data_schema_models.stimulus import (
    AuditoryStimulation,
    FilterType,
    OlfactometerChannelConfig,
    OlfactoryStimulation,
    OptoStimulation,
    PhotoStimulation,
    PhotoStimulationGroup,
    PulseShape,
    VisualStimulation,
)
from aind_data_schema_models.units import PowerUnit


class TestPulseShape(unittest.TestCase):
    """Tests PulseShape"""

    def test_pulse_shape(self):
        """Tests enum can be instantiated with a string"""
        self.assertEqual(PulseShape.RAMP, PulseShape("Ramp"))


class TestFilterType(unittest.TestCase):
    """Tests FilterType"""

    def test_filter_type(self):
        """Tests enum can be instantiated with a string"""
        self.assertEqual(FilterType.BUTTERWORTH, FilterType("Butterworth"))


class TestOptoStimulation(unittest.TestCase):
    """Tests OptoStimulation"""

    def test_opto_stimulation(self):
        """Tests model construction"""
        opto_stimulation = OptoStimulation(
            stimulus_name="opto stim",
            pulse_shape=PulseShape.RAMP,
            pulse_frequency=[Decimal("15"), Decimal("15")],
            number_pulse_trains=[1, 1],
            pulse_width=[1, 2],
            pulse_train_duration=[Decimal("5"), Decimal("5")],
            baseline_duration=Decimal("10"),
            fixed_pulse_train_interval=False,
        )
        self.assertEqual("opto stim", opto_stimulation.stimulus_name)
        self.assertEqual(PulseShape.RAMP, opto_stimulation.pulse_shape)
        self.assertEqual([Decimal("15"), Decimal("15")], opto_stimulation.pulse_frequency)
        self.assertEqual([1, 1], opto_stimulation.number_pulse_trains)
        self.assertEqual([1, 2], opto_stimulation.pulse_width)
        self.assertEqual([Decimal("5"), Decimal("5")], opto_stimulation.pulse_train_duration)
        self.assertEqual(Decimal("10"), opto_stimulation.baseline_duration)
        self.assertFalse(opto_stimulation.fixed_pulse_train_interval)


class TestVisualStimulation(unittest.TestCase):
    """Tests VisualStimulation"""

    def test_visual_stimulation(self):
        """Tests model construction"""
        visual_stimulation = VisualStimulation(stimulus_name="visual stim")
        self.assertEqual("visual stim", visual_stimulation.stimulus_name)


class TestPhotoStimulationGroup(unittest.TestCase):
    """Tests PhotoStimulationGroup"""

    def test_photo_stimulation_group(self):
        """Tests model construction"""

        photo_stimulation_group = PhotoStimulationGroup(
            group_index=0,
            number_of_neurons=1,
            stimulation_laser_power=Decimal("50"),
            stimulation_laser_power_unit=PowerUnit.PERCENT,
            number_trials=1,
            number_spirals=1,
            spiral_duration=Decimal("5"),
            inter_spiral_interval=Decimal("10"),
        )

        self.assertEqual(0, photo_stimulation_group.group_index)
        self.assertEqual(1, photo_stimulation_group.number_of_neurons)
        self.assertEqual(Decimal("50"), photo_stimulation_group.stimulation_laser_power)
        self.assertEqual(PowerUnit.PERCENT, photo_stimulation_group.stimulation_laser_power_unit)
        self.assertEqual(1, photo_stimulation_group.number_trials)
        self.assertEqual(1, photo_stimulation_group.number_spirals)
        self.assertEqual(Decimal("5"), photo_stimulation_group.spiral_duration)
        self.assertEqual(Decimal("10"), photo_stimulation_group.inter_spiral_interval)


class TestPhotoStimulation(unittest.TestCase):
    """Tests PhotoStimulation"""

    def test_photo_stimulation(self):
        """Tests model construction"""

        photo_stimulation = PhotoStimulation(
            stimulus_name="photo stim", number_groups=0, groups=[], inter_trial_interval=Decimal("0.0")
        )
        self.assertEqual("photo stim", photo_stimulation.stimulus_name)
        self.assertEqual(0, photo_stimulation.number_groups)
        self.assertEqual([], photo_stimulation.groups)
        self.assertEqual(Decimal("0.0"), photo_stimulation.inter_trial_interval)


class TestOlfactometerChannelConfig(unittest.TestCase):
    """Tests OlfactometerChannelConfig"""

    def test_olfactometer_channel_config(self):
        """Tests model construction"""

        olfactometer_channel_config = OlfactometerChannelConfig(
            channel_index=0, odorant="none", odorant_dilution=Decimal("0.0")
        )
        self.assertEqual(0, olfactometer_channel_config.channel_index)
        self.assertEqual("none", olfactometer_channel_config.odorant)
        self.assertEqual(Decimal("0.0"), olfactometer_channel_config.odorant_dilution)


class TestOlfactoryStimulation(unittest.TestCase):
    """Tests OlfactoryStimulation"""

    def test_olfactory_stimulation(self):
        """Tests model construction"""

        olfactory_stimulation = OlfactoryStimulation(channels=[], stimulus_name="olfactory stim")

        self.assertEqual([], olfactory_stimulation.channels)
        self.assertEqual("olfactory stim", olfactory_stimulation.stimulus_name)


class TestAuditoryStimulation(unittest.TestCase):
    """Tests AuditoryStimulation"""

    def test_auditory_stimulation(self):
        """Tests model construction"""

        auditory_stimulation = AuditoryStimulation(stimulus_name="audio stim", sample_frequency=Decimal("0.0"))

        self.assertEqual("audio stim", auditory_stimulation.stimulus_name)
        self.assertEqual(Decimal("0.0"), auditory_stimulation.sample_frequency)


if __name__ == "__main__":
    unittest.main()
