"""Stimulus modalities"""

from enum import Enum


class Slap2AcquisitionType(str, Enum):
    """Stimulus modalities"""

    BAND_SCAN = "band scan"
    FULL_FIELD_RASTER_SCAN = "full-field raster scan"
    INTEGRATION_SCAN = "integration scan"
    MULTI_ROI_RASTER_SCAN = "multi-roi raster scan"
