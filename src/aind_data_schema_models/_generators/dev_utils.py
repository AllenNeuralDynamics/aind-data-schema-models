""" Dev utilities for constructing models from CSV files """

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
