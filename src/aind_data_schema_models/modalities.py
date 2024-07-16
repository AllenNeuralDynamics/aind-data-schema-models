"""Module for Modality definitions"""

from pydantic import ConfigDict, Field

from aind_data_schema_models.pid_names import BaseName
from aind_data_schema_models.utils import create_literal_class, read_csv


class Modality(BaseName):
    """Base model config"""

    model_config = ConfigDict(frozen=True)
    name: str = Field(..., title="Modality name")
    abbreviation: str = Field(..., title="Modality abbreviation")


Modalities = create_literal_class(
    objects=read_csv("models/modalities.csv"),
    class_name="Modalities",
    base_model=Modality,
    discriminator="abbreviation",
    class_module=__name__,
)


@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map[abbreviation]


Modalities._abbreviation_map = {m().abbreviation: m() for m in Modalities._ALL}
Modalities.from_abbreviation = from_abbreviation
