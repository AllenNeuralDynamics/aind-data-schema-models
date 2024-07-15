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
    discriminator='abbreviation'
)