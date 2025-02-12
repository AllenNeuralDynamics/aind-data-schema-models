""" Dev utilities for constructing models from CSV files """

import re


def unique_rows(data, key):
    """Generate a unique subset of a dataframe based on a key column.

    Parameters
    ----------
    data : pd.DataFrame
      The data to filter.
    key : str
      The column to filter on.
    """
    return data.drop_duplicates(subset=key)


def to_class_name_underscored(name: str) -> str:
    """Convert a name to a class name by capitalizing and removing non-alphanumeric characters.

    Always prefixes the string with an underscore."""
    name = str(name)
    return "_" + re.sub(r"\W", "_", name.title()).replace(" ", "")


def to_class_name(name: str) -> str:
    """Convert a name to a valid class name by capitalizing and removing non-alphanumeric characters.

    Replace any non alphanumeric characters at the beginning of the string with a single _."""
    name = str(name)
    return re.sub(r"\W|^(?=\d)", "_", name.title()).replace(" ", "")
