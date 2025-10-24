"""Genes"""

import re

import requests
from pydantic import BaseModel, ConfigDict

from aind_data_schema_models.registries import Registry


class NucleotideModel(BaseModel):
    """Nucleotide model"""

    model_config = ConfigDict(frozen=True)
    description: str
    registry: Registry = Registry.GENBANK
    registry_identifier: str = ""


def fetch_genbank_record(accession_id: str) -> NucleotideModel:
    """Helper function to fetch GenBank record by accession ID"""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "nuccore", "id": accession_id, "rettype": "gb", "retmode": "text"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    text = response.text
    # Extract DEFINITION line (may span multiple lines until next all-caps field)
    pattern = (
        r"^DEFINITION  (.*?)(?:\n[A-Z][A-Z ]+|"
        r"\nACCESSION|\nVERSION|\nKEYWORDS|\nSOURCE|"
        r"\nFEATURES|\nORIGIN|\nREFERENCE|\n$)"
    )
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if match:
        definition = match.group(1).replace("\n", " ").replace("  ", " ").strip()
    else:
        raise ValueError("DEFINITION line not found in GenBank record")
    return NucleotideModel(description=definition, registry_identifier=accession_id)


class Gene:
    """Gene model"""

    def from_genbank_accession_id(self, accession_id: str) -> NucleotideModel:
        """Fetch gene information from GenBank by accession ID"""
        return fetch_genbank_record(accession_id)
