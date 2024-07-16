"""Module for Platform definitions"""

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.utils import create_literal_class


class Platform(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str = Field(..., title="Platform name")
    abbreviation: str = Field(..., title="Platform abbreviation")


Platforms = create_literal_class(
    objects=pd.read_csv("models/platforms.csv").to_dict(orient="records"),
    class_name="Platforms",
    base_model=Platform,
    discriminator="name",
    class_module=__name__,
)


@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map[abbreviation]


Platforms._abbreviation_map = {p().abbreviation: p() for p in Platforms._ALL}
Platforms.from_abbreviation = from_abbreviation
