"""Module for Harp Device Types"""

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated
import pandas as pd
from aind_data_schema_models.utils import create_literal_class


class HarpDeviceType(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)
    name: str
    whoami: int

HarpDeviceTypes = create_literal_class(
    objects=pd.read_csv('models/harp_types.csv').to_dict(orient='records'), 
    class_name='HarpDeviceTypes', 
    base_model=HarpDeviceType, 
    discriminator='name',
    class_module=__name__)