""" General utilities for constructing models from CSV files """

import csv
import re
from pathlib import Path
from typing import List, Literal, Optional, Type, Union

from pydantic import BaseModel, ConfigDict, Field, create_model
from typing_extensions import Annotated


def create_literal_model(
    obj: dict, base_model: Type[BaseModel], discriminator: str, field_handlers: Optional[dict] = None, class_module=None
):
    """make a dynamic pydantic literal model"""

    field_handlers = field_handlers or {}

    fields = {}
    for k, v in obj.items():
        if k in field_handlers:
            field_handlers[k](v, fields)
        else:
            fields[k] = (Literal[v], Field(v))

    class_name = create_model_class_name(obj[discriminator])
    m = create_model(class_name, model_config=ConfigDict(frozen=True), __base__=base_model, **fields)

    if class_module:
        m.__module__ = class_module

    return m


def create_model_class_name(class_name: str):
    """lint class name"""

    # remove punctuation
    punctuation = re.compile(r'[.,!?;:\'"-()]')
    class_name = punctuation.sub("", class_name)

    # remove whitespace from title case
    pattern = re.compile(r"[\W_]+")
    return pattern.sub("", class_name.title())


def create_literal_class(
    objects: List[dict],
    class_name: str,
    class_module=None,
    base_model: Type[BaseModel] = BaseModel,
    discriminator: str = "name",
    field_handlers: Optional[dict] = None,
):
    """make a dynamic pydantic literal class"""

    cls = type(class_name, (object,), {})

    # add a "ALL" class variable
    all_models = tuple(
        create_literal_model(
            obj=obj,
            base_model=base_model,
            discriminator=discriminator,
            field_handlers=field_handlers,
            class_module=class_module,
        )
        for obj in objects
    )

    setattr(cls, "ALL", tuple(all_models))

    # Older versions of flake8 raise errors about 'ALL' being undefined
    setattr(cls, "ONE_OF", Annotated[Union[getattr(cls, "ALL")], Field(discriminator=discriminator)])  # noqa: F821

    # add the model instances as class variables
    for m in all_models:
        setattr(cls, m.__name__, m())

    return cls


def read_csv(file_path: Union[str, Path]):
    """read a csv file and return the contents as a list of dictionaries"""
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def one_of_instance(instances, discriminator="name"):
    """
    Make an annotated union of class instances
    Parameters
    ----------
    instances :
    discriminator :

    Returns
    -------

    """
    return Annotated[Union[tuple(type(i) for i in instances)], Field(discriminator=discriminator)]
