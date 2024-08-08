"""Module for Mouse Anatomy"""

from importlib_resources import files
from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.utils import create_literal_class, read_csv


class MouseAnatomyModel(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)
    emapa_id: int = Field(..., title="Structure EMAPA ID")
    name: str = Field(..., title="Structure name")


MouseAnatomicalStructure = create_literal_class(
    objects=read_csv(str(files("aind_data_schema_models.models").joinpath("mouse_dev_anat_ontology.csv"))),
    class_name="MouseAnatomyType",
    base_model=MouseAnatomyModel,
    discriminator="emapa_id",
    class_module=__name__,
)
