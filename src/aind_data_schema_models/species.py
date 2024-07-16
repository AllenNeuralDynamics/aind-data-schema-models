"""Module for species definitions"""

from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.registry import Registry, map_registry
from aind_data_schema_models.utils import create_literal_class, read_csv


class SpeciesModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str = Field(..., title="Species name")
    registry: Registry = Field(..., title="Species registry")
    registry_identifier: str = Field(..., title="Species registry identifier")


Species = create_literal_class(
    objects=read_csv("models/species.csv"),
    class_name="Species",
    base_model=SpeciesModel,
    discriminator="name",
    field_handlers={"registry_abbreviation": map_registry},
    class_module=__name__,
)
