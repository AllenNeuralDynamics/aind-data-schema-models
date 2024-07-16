"""Common registries"""

from typing import Literal

from pydantic import ConfigDict
import pandas as pd
from aind_data_schema_models.utils import create_literal_class
from aind_data_schema_models.pid_names import BaseName


class Registry(BaseName):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str
    abbreviation: str


Registries = create_literal_class(
    objects=pd.read_csv('models/registries.csv').to_dict(orient='records'), 
    class_name='Registries', 
    base_model=Registry,
    discriminator='abbreviation',
    class_module=__name__
)

@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map.get(abbreviation, None)

Registries._abbreviation_map = {m().abbreviation: m() for m in Registries._ALL}
Registries.from_abbreviation = from_abbreviation