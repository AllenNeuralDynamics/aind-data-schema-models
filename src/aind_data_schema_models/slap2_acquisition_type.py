"""Stimulus modalities"""

from enum import Enum


class Slap2AcquisitionType(str, Enum):
    """Stimulus modalities"""

    INTEGRATION_SCAN = "integration scan"
    RASTER_SCAN = "raster scan"
