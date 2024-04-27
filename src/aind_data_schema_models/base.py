"""Module to hold common parent classes"""

from typing import Any, Generic, TypeVar

from pydantic import (
    AwareDatetime,
    BaseModel,
    ConfigDict,
    NaiveDatetime,
    ValidationError,
    ValidatorFunctionWrapHandler,
    create_model,
)
from pydantic.functional_validators import WrapValidator
from typing_extensions import Annotated


def _coerce_naive_datetime(v: Any, handler: ValidatorFunctionWrapHandler) -> AwareDatetime:
    """Validator to wrap around AwareDatetime to set a default timezone as user's locale"""
    try:
        return handler(v)
    except ValidationError:
        # Try to parse the input as a naive datetime object and attach timezone info
        return (
            create_model("_TempNaiveDatetimeModel", dt=(NaiveDatetime, ...)).model_validate({"dt": v}).dt.astimezone()
        )


AwareDatetimeWithDefault = Annotated[AwareDatetime, WrapValidator(_coerce_naive_datetime)]


class AindGeneric(BaseModel, extra="allow"):
    """Base class for generic types that can be used in AIND schema"""

    # extra="allow" is needed because BaseModel by default drops extra parameters.
    # Alternatively, consider using 'SerializeAsAny' once this issue is resolved
    # https://github.com/pydantic/pydantic/issues/6423
    pass


AindGenericType = TypeVar("AindGenericType", bound=AindGeneric)


class AindModel(BaseModel, Generic[AindGenericType]):
    """BaseModel that disallows extra fields"""

    model_config = ConfigDict(extra="forbid", use_enum_values=True)
