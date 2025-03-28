"""Module for computer system and architecture definitions"""

from enum import Enum


class License(str, Enum):
    """Licenses"""

    MIT = "MIT"
    CC_BY_40 = "CC-BY-4.0"
