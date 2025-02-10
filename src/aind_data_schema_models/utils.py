""" General utilities for constructing models from CSV files """

import re
from pydantic import BaseModel, Field
from typing import Union, List, Type, Any
from typing_extensions import Annotated
import pandas as pd


def unique_rows(value, key):
    """Generate a unique subset of a dataframe based on a key column.

    Parameters
    ----------
    data : pd.DataFrame
      The data to filter.
    key : str
      The column to filter on.
    """
    seen = set()
    unique_rows = []
    for _, row in value.iterrows():
        if row[key] not in seen:
            seen.add(row[key])
            unique_rows.append(row)
    return pd.DataFrame(unique_rows)


def to_class_name_underscored(name: str) -> str:
    """Convert a name to a valid class name by capitalizing and removing non-alphanumeric characters."""
    name = str(name)
    return "_" + re.sub(r"\W+", "_", name.title()).replace(" ", "")


def to_class_name(name: str) -> str:
    """Convert a name to a valid class name by capitalizing and removing non-alphanumeric characters."""
    name = str(name)
    return re.sub(r"\W|^(?=\d)", "_", name.title()).replace(" ", "")


def one_of_instance(instances: List[Type[BaseModel]], discriminator="name") -> Annotated[Union[Any], Field]:
    """
    Make an annotated union of class instances
    Parameters
    ----------
    instances : List[Type[BaseModel]]
      A list of class instances.
    discriminator : str
      Each model in instances should have a common field name where each item
      is unique to the model. This will allow pydantic to know which class
      should be deserialized. Default is 'name'.

    Returns
    -------
    Annotated[Union[Any], Field]
      An annotated field that can be used to define a type where a choice from a
      possible set of classes can be selected.

    """
    return Annotated[Union[tuple(type(i) for i in instances)], Field(discriminator=discriminator)]
