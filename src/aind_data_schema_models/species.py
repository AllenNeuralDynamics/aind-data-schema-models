"""Module for species definitions"""

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.registry import Registry, map_registry
from aind_data_schema_models.utils import create_literal_class


class SpeciesModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str = Field(..., title="Species name")
    registry: Registry = Field(..., title="Species registry")
    registry_identifier: str = Field(..., title="Species registry identifier")


Species = create_literal_class(
    objects=pd.read_csv("models/species.csv", keep_default_na=False).to_dict(orient="records"),
    class_name="Species",
    base_model=SpeciesModel,
    discriminator="name",
    field_handlers={"registry_abbreviation": map_registry},
    class_module=__name__,
)
