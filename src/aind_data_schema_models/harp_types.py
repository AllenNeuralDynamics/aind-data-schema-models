"""Module for Harp Device Types"""

from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.utils import create_literal_class, read_csv


class HarpDeviceType(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)
    name: str = Field(..., title="Harp device type name")
    whoami: int = Field(..., title="Harp whoami value")


HarpDeviceTypes = create_literal_class(
    objects=read_csv("models/harp_types.csv"),
    class_name="HarpDeviceTypes",
    base_model=HarpDeviceType,
    discriminator="name",
    class_module=__name__,
)
