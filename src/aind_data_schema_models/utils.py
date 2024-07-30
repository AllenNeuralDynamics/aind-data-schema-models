""" General utilities for constructing models from CSV files """

import csv
import re
import sys
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, create_model
from typing_extensions import Annotated

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from backports.strenum import StrEnum


def create_literal_model(
    obj: dict, base_model: BaseModel, discriminator: str, field_handlers: Optional[dict] = None, class_module=None
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
    base_model: BaseModel = BaseModel,
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

    setattr(cls, "_ALL", tuple(all_models))

    setattr(cls, "ONE_OF", Annotated[Union[cls._ALL], Field(discriminator=discriminator)])

    # add the model instances as class variables
    for m in all_models:
        setattr(cls, m.__name__, m())

    return cls


def read_csv(file_path: str):
    """read a csv file and return the contents as a list of dictionaries"""
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def one_of_instance(instances, discriminator="name"):
    """make an annotated union of class instances"""
    return Annotated[Union[tuple(type(i) for i in instances)], Field(discriminator=discriminator)]


def create_string_enum(name, objects, value_key="name"):
    """create a string enum from a list of objects"""

    return StrEnum(name, {create_model_class_name(obj[value_key]): obj[value_key] for obj in objects})
