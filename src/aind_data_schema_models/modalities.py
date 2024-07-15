"""Module for Modality definitions"""

from typing import Literal, Union

from pydantic import ConfigDict, Field
from typing_extensions import Annotated
import pandas as pd
from aind_data_schema_models.utils import create_literal_class
from aind_data_schema_models.pid_names import BaseName


class Modality(BaseName):
    """Base model config"""

    model_config = ConfigDict(frozen=True)
    name: str
    abbreviation: str


Modalities = create_literal_class(
    objects=pd.read_csv('models/modalities.csv').to_dict(orient='records'), 
    class_name='Modalities', 
    base_model=Modality, 
    discriminator='name'
)

@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map[abbreviation]

Modalities._abbreviation_map = {m().abbreviation: m() for m in Modalities._ALL}
Modalities.from_abbreviation = from_abbreviation
