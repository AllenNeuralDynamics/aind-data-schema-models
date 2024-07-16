"""Common registries"""

from typing import Union

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.pid_names import BaseName
from aind_data_schema_models.utils import create_literal_class, read_csv


class RegistryModel(BaseName):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str = Field(..., title="Registry name")
    abbreviation: str = Field(..., title="Registry abbreviation")


Registry = create_literal_class(
    objects=read_csv("models/registries.csv"),
    class_name="Registry",
    base_model=RegistryModel,
    discriminator="abbreviation",
    class_module=__name__,
)


def map_registry(abbreviation: str, record: dict):
    registry = Registry.from_abbreviation(abbreviation)
    if registry:
        record["registry"] = Annotated[Union[registry], Field(default=registry, discriminator="name")]
    else:
        record["registry"] = Annotated[None, Field(None)]


@classmethod
def from_abbreviation(cls, abbreviation: str):
    """Get class from abbreviation"""
    return cls._abbreviation_map.get(abbreviation, None)


Registry._abbreviation_map = {m().abbreviation: m() for m in Registry._ALL}
Registry.from_abbreviation = from_abbreviation
