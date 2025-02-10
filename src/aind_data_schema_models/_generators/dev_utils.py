""" Dev utilities for constructing models from CSV files """


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
