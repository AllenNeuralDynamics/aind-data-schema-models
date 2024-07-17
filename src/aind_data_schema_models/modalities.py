"""Module for Modality definitions"""

from importlib_resources import files
from pydantic import ConfigDict, Field

from aind_data_schema_models.pid_names import BaseName
from aind_data_schema_models.utils import create_literal_class, read_csv


class ModalityModel(BaseName):
    """Base model config"""

    model_config = ConfigDict(frozen=True)
    name: str = Field(..., title="Modality name")
    abbreviation: str = Field(..., title="Modality abbreviation")


Modality = create_literal_class(
    objects=read_csv(files("aind_data_schema_models.models").joinpath("modalities.csv")),
    class_name="Modality",
    base_model=ModalityModel,
    discriminator="abbreviation",
    class_module=__name__,
)


@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map[abbreviation]


Modality._abbreviation_map = {m().abbreviation: m() for m in Modality._ALL}
Modality.from_abbreviation = from_abbreviation
