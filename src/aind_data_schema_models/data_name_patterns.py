"""Module for defining our data naming conventions"""

from datetime import datetime
from enum import Enum
import warnings


class RegexParts(str, Enum):
    """Regular expression components to be re-used elsewhere"""

    DATE = r"\d{4}-\d{2}-\d{2}"
    TIME = r"\d{2}-\d{2}-\d{2}"
    DATETIME = r"\d{4}-\d{2}-\d{2}T\d{2}\d{2}\d{2}"


class DataRegex(str, Enum):
    """Regular expression patterns for different kinds of data and their properties"""

    DATA_OLD = f"^(?P<label>.+?)_(?P<c_date>{RegexParts.DATE.value})_(?P<c_time>{RegexParts.TIME.value})$"
    DATA = f"^(?P<label>.+?)_(?P<c_date>{RegexParts.DATETIME.value})$"
    RAW_OLD = (
        f"^(?P<platform_abbreviation>.+?)_(?P<subject_id>.+?)_(?P<c_date>{RegexParts.DATE.value})_(?P<c_time>"
        f"{RegexParts.TIME.value})$"
    )
    DERIVED_OLD = (
        f"^(?P<input>.+?_{RegexParts.DATE.value}_{RegexParts.TIME.value})_(?P<process_name>.+?)_(?P<c_date>"
        f"{RegexParts.DATE.value})_(?P<c_time>{RegexParts.TIME.value})"
    )
    ANALYZED_OLD = (
        f"^(?P<project_abbreviation>.+?)_(?P<analysis_name>.+?)_(?P<c_date>"
        f"{RegexParts.DATE.value})_(?P<c_time>{RegexParts.TIME.value})$"
    )
    RAW = (
        f"^(?P<platform_abbreviation>.+?)_(?P<subject_id>.+?)_(?P<c_date>{RegexParts.DATETIME.value})$"
    )
    DERIVED = (
        f"^(?P<input>.+?_{RegexParts.DATETIME.value})_(?P<process_name>.+?)_(?P<c_date>"
        f"{RegexParts.DATETIME.value})"
    )
    ANALYZED = (
        f"^(?P<project_abbreviation>.+?)_(?P<analysis_name>.+?)_(?P<c_date>"
        f"{RegexParts.DATETIME.value})$"
    )
    NO_UNDERSCORES = r"^[^_]+$"
    NO_SPECIAL_CHARS = r'^[^<>:;"/|? \\_]+$'
    NO_SPECIAL_CHARS_EXCEPT_SPACE = r'^[^<>:;"/|?\\_]+$'


class DataLevel(str, Enum):
    """Data level name"""

    DERIVED = "derived"
    RAW = "raw"
    SIMULATED = "simulated"


class Group(str, Enum):
    """Data collection group name"""

    BEHAVIOR = "behavior"
    EPHYS = "ephys"
    MSMA = "MSMA"
    OPHYS = "ophys"
    NBA = "NBA"


def datetime_to_name_string(dt: datetime) -> str:
    """
    Take a datetime object, format it as a string
    Parameters
    ----------
    dt : datetime
      For example, datetime(2020, 12, 29, 10, 04, 59, 567000)

    Returns
    -------
    str
      For example, '2020-12-29T100459.567'

    """
    return dt.strftime("%Y-%m-%dT%H%M%S")


def datetime_from_name_string(d: str, t: str) -> datetime:
    """
    DEPRECATED

    Take date and time strings, generate datetime object
    Parameters
    ----------
    d : str
      Date string formatted as %Y-%m-%d
    t : str
      Time string formatted as %H-%M-%S

    Returns
    -------
    datetime

    """
    warnings.warn("This function is deprecated. Use datetime.fromisoformat() instead.")
    d = datetime.strptime(d, "%Y-%m-%d").date()
    t = datetime.strptime(t, "%H-%M-%S").time()
    return datetime.combine(d, t)


def build_data_name(subject_id: str, creation_datetime: datetime) -> str:
    """
    Construct a data description name from a label and datetime object
    Parameters
    ----------
    subject_id : str
      For example, '123456'
    creation_datetime : datetime
      For example, datetime(2020, 12, 29, 10, 04, 59)

    Returns
    -------
    str
      For example, '123456_2020-12-29T100459'

    """
    dt_str = datetime_to_name_string(creation_datetime)
    return f"{subject_id}_{dt_str}"
