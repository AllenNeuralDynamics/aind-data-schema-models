"""Registries"""

from enum import Enum


class Registry(str, Enum):
    """Registries"""

    ADDGENE = "ADDGENE"
    EMAPA = "EMAPA"
    MGI = "MGI"
    NCBI = "NCBI"
    ORCID = "ORCID"
    ROR = "ROR"
    RRID = "RRID"
    UNIPROT = "UNIPROT"
