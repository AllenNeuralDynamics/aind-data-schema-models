"""Module for Platform definitions"""

from importlib_resources import files
from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.utils import create_literal_class, read_csv


class PlatformModel(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str = Field(..., title="Platform name")
    abbreviation: str = Field(..., title="Platform abbreviation")


Platform = create_literal_class(
    objects=read_csv(files("aind_data_schema_models.models").joinpath("platforms.csv")),
    class_name="Platform",
    base_model=PlatformModel,
    discriminator="name",
    class_module=__name__,
)


@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map[abbreviation]


Platform._abbreviation_map = {p().abbreviation: p() for p in Platform._ALL}
Platform.from_abbreviation = from_abbreviation
