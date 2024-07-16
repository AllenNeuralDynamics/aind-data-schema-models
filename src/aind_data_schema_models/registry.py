"""Common registries"""

from typing import Annotated, Union

import pandas as pd
from pydantic import ConfigDict, Field

from aind_data_schema_models.pid_names import BaseName
from aind_data_schema_models.utils import create_literal_class


class Registry(BaseName):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str = Field(..., title="Registry name")
    abbreviation: str = Field(..., title="Registry abbreviation")


Registries = create_literal_class(
    objects=pd.read_csv("models/registries.csv").to_dict(orient="records"),
    class_name="Registries",
    base_model=Registry,
    discriminator="abbreviation",
    class_module=__name__,
)


def map_registry(abbreviation: str, record: dict):
    registry = Registries.from_abbreviation(abbreviation)
    if registry:
        record["registry"] = Annotated[Union[registry], Field(default=registry, discriminator="name")]
    else:
        record["registry"] = Annotated[None, Field(None)]


@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map.get(abbreviation, None)


Registries._abbreviation_map = {m().abbreviation: m() for m in Registries._ALL}
Registries.from_abbreviation = from_abbreviation
