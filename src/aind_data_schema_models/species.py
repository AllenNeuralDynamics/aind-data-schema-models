"""Species"""
from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.registries import Registry


class StrainModel(BaseModel):
    """Base model for a strain"""
    model_config = ConfigDict(frozen=True)
    name: str
    species: str
    registry: Registry.ONE_OF
    registry_identifier: str


class _A(StrainModel):
    """Model a"""
    name: Literal["a"] = "a"
    species: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.A
    registry_identifier: Literal["nan"] = "nan"


class _A(StrainModel):
    """Model a"""
    name: Literal["a"] = "a"
    species: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.A
    registry_identifier: Literal["nan"] = "nan"


class _A(StrainModel):
    """Model a"""
    name: Literal["a"] = "a"
    species: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.A
    registry_identifier: Literal["nan"] = "nan"


class _A(StrainModel):
    """Model a"""
    name: Literal["a"] = "a"
    species: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.A
    registry_identifier: Literal["nan"] = "nan"


class _A(StrainModel):
    """Model a"""
    name: Literal["a"] = "a"
    species: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.A
    registry_identifier: Literal["nan"] = "nan"


class _A(StrainModel):
    """Model a"""
    name: Literal["a"] = "a"
    species: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.A
    registry_identifier: Literal["nan"] = "nan"


class Strain:
    """Strain"""

    A = _A()
    A = _A()
    A = _A()
    A = _A()
    A = _A()
    A = _A()

    ALL = tuple(StrainModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(StrainModel.__subclasses__())], Field(discriminator="name")]


class SpeciesModel(BaseModel):
    """Base model for species"""
    model_config = ConfigDict(frozen=True)
    name: str
    registry: Registry.ONE_OF
    registry_identifier: str


class _Ncbi(SpeciesModel):
    """Model NCBI"""
    name: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.NCBI:TXID9483
    registry_identifier: Literal["default"] = "default"


class _Ncbi(SpeciesModel):
    """Model NCBI"""
    name: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.NCBI:TXID9606
    registry_identifier: Literal["default"] = "default"


class _Ncbi(SpeciesModel):
    """Model NCBI"""
    name: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.NCBI:TXID9544
    registry_identifier: Literal["default"] = "default"


class _Ncbi(SpeciesModel):
    """Model NCBI"""
    name: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.NCBI:TXID10090
    registry_identifier: Literal["C57BL/6J"] = "C57BL/6J"


class _Ncbi(SpeciesModel):
    """Model NCBI"""
    name: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.NCBI:TXID10090
    registry_identifier: Literal["BALB/c"] = "BALB/c"


class _Ncbi(SpeciesModel):
    """Model NCBI"""
    name: Literal["NCBI"] = "NCBI"
    registry: Registry.ONE_OF = Registry.NCBI:TXID10116
    registry_identifier: Literal["default"] = "default"


class Species:
    """Species"""

    CALLITHRIX_JACCHUS = _Callithrix_Jacchus()
    HOMO_SAPIENS = _Homo_Sapiens()
    MACACA_MULATTA = _Macaca_Mulatta()
    MUS_MUSCULUS = _Mus_Musculus()
    MUS_MUSCULUS = _Mus_Musculus()
    RATTUS_NORVEGICUS = _Rattus_Norvegicus()

    ALL = tuple(SpeciesModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(SpeciesModel.__subclasses__())], Field(discriminator="name")]
