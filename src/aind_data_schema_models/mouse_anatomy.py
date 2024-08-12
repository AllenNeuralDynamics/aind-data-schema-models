"""Module for Mouse Anatomy"""

from importlib_resources import files
from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.utils import create_literal_class, read_csv, subset_from_column


class MouseAnatomyModel(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)
    emapa_id: int = Field(..., title="Structure EMAPA ID")
    name: str = Field(..., title="Structure name")


mouse_objects = read_csv(str(files("aind_data_schema_models.models").joinpath("mouse_dev_anat_ontology.csv")))

MouseAnatomicalStructure = create_literal_class(
    objects=mouse_objects,
    class_name="MouseAnatomyType",
    base_model=MouseAnatomyModel,
    discriminator="emapa_id",
    class_module=__name__,
)

MouseAnatomicalStructure.EMG_MUSCLES = subset_from_column(MouseAnatomicalStructure,
                   objects=mouse_objects,
                   column="EMG_MUSCLES")
