# generated by aind-data-schema-models:
#   filename:  species.csv
#   timestamp: 2024-09-01 10:13:40.321382


from typing import Annotated, Literal, Union

from pydantic import Field

from aind_data_schema_models._generated.registries import _Registry
from aind_data_schema_models.generators._base import _SpeciesModel


class CallithrixJacchus(_SpeciesModel):

    name: Literal["Callithrix jacchus"] = "Callithrix jacchus"
    registry: Literal[_Registry.NCBI] = _Registry.NCBI
    registry_identifier: Literal["NCBI:txid9483"] = "NCBI:txid9483"


class HomoSapiens(_SpeciesModel):

    name: Literal["Homo sapiens"] = "Homo sapiens"
    registry: Literal[_Registry.NCBI] = _Registry.NCBI
    registry_identifier: Literal["NCBI:txid9606"] = "NCBI:txid9606"


class MacacaMulatta(_SpeciesModel):

    name: Literal["Macaca mulatta"] = "Macaca mulatta"
    registry: Literal[_Registry.NCBI] = _Registry.NCBI
    registry_identifier: Literal["NCBI:txid9544"] = "NCBI:txid9544"


class MusMusculus(_SpeciesModel):

    name: Literal["Mus musculus"] = "Mus musculus"
    registry: Literal[_Registry.NCBI] = _Registry.NCBI
    registry_identifier: Literal["NCBI:txid10090"] = "NCBI:txid10090"


class RattusNorvegicus(_SpeciesModel):

    name: Literal["Rattus norvegicus"] = "Rattus norvegicus"
    registry: Literal[_Registry.NCBI] = _Registry.NCBI
    registry_identifier: Literal["NCBI:txid10116"] = "NCBI:txid10116"


class _Species:

    CALLITHRIX_JACCHUS = CallithrixJacchus()
    HOMO_SAPIENS = HomoSapiens()
    MACACA_MULATTA = MacacaMulatta()
    MUS_MUSCULUS = MusMusculus()
    RATTUS_NORVEGICUS = RattusNorvegicus()

    ALL = tuple(_SpeciesModel.__subclasses__())
    ONE_OF = Annotated[Union[ALL], Field(discriminator="name")]
