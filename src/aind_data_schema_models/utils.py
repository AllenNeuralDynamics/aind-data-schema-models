""" General utilities for constructing models from CSV files """

import re


def to_class_name_underscored(name: str) -> str:
    """Convert a name to a valid class name by capitalizing and removing non-alphanumeric characters."""
    return "_" + re.sub(r"\W+", "_", name.title()).replace(" ", "")


def to_class_name(name: str) -> str:
    """Convert a name to a valid class name by capitalizing and removing non-alphanumeric characters."""
    return re.sub(r"\W|^(?=\d)", "_", name.title()).replace(" ", "")
