"""Process names"""

from enum import Enum


class ProcessName(str, Enum):
    """Process names"""

    ANALYSIS = "Analysis"
    COMPRESSION = "Compression"
    DENOISING = "Denoising"
    DF_F_ESTIMATION = "dF/F estimation"
    EPHYS_CURATION = "Ephys curation"
    EPHYS_POSTPROCESSING = "Ephys postprocessing"
    EPHYS_PREPROCESSING = "Ephys preprocessing"
    EPHYS_VISUALIZATION = "Ephys visualization"
    FIDUCIAL_SEGMENTATION = "Fiducial segmentation"
    FILE_FORMAT_CONVERSION = "File format conversion"
    FLUORESCENCE_EVENT_DETECTION = "Fluorescence event detection"
    IMAGE_ATLAS_ALIGNMENT = "Image atlas alignment"
    IMAGE_BACKGROUND_SUBTRACTION = "Image background subtraction"
    IMAGE_CELL_CLASSIFICATION = "Image cell classification"
    IMAGE_CELL_QUANTIFICATION = "Image cell quantification"
    IMAGE_CELL_SEGMENTATION = "Image cell segmentation"
    IMAGE_DESTRIPING = "Image destriping"
    IMAGE_FLAT_FIELD_CORRECTION = "Image flat-field correction"
    IMAGE_IMPORTING = "Image importing"
    IMAGE_MIP_VISUALIZATION = "Image mip visualization"
    IMAGE_THRESHOLDING = "Image thresholding"
    IMAGE_TILE_ALIGNMENT = "Image tile alignment"
    IMAGE_TILE_FUSING = "Image tile fusing"
    IMAGE_TILE_PROJECTION = "Image tile projection"
    NEUROPIL_SUBTRACTION = "Neuropil subtraction"
    OTHER = "Other"
    SIMULATION = "Simulation"
    SKULL_STRIPPING = "Skull stripping"
    SPATIAL_TIMESERIES_DEMIXING = "Spatial timeseries demixing"
    SPIKE_SORTING = "Spike sorting"
    VIDEO_MOTION_CORRECTION = "Video motion correction"
    VIDEO_PLANE_DECROSSTALK = "Video plane decrosstalk"
    VIDEO_ROI_CLASSIFICATION = "Video ROI classification"
    VIDEO_ROI_CROSS_SESSION_MATCHING = "Video ROI cross session matching"
    VIDEO_ROI_SEGMENTATION = "Video ROI segmentation"
    VIDEO_ROI_TIMESERIES_EXTRACTION = "Video ROI timeseries extraction"
