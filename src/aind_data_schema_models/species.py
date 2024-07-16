"""Module for species definitions"""

from typing import Literal, Union

from pydantic import ConfigDict, Field, BaseModel
from typing_extensions import Annotated
import pandas as pd
from aind_data_schema_models.utils import create_literal_class
from aind_data_schema_models.registry import Registry, Registries, map_registry

class SpeciesModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    registry: Registry
    registry_identifier: str
    

Species = create_literal_class(
    objects=pd.read_csv('models/species.csv', keep_default_na=False).to_dict(orient='records'), 
    class_name='Species', 
    base_model=SpeciesModel, 
    discriminator='name',
    field_handlers={'registry_abbreviation': map_registry},
    class_module=__name__
)
