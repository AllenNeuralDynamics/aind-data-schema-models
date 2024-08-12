"""Module for Mouse Anatomy"""

from importlib_resources import files
from pydantic import BaseModel, ConfigDict, Field

from aind_data_schema_models.registries import RegistryModel, map_registry
from aind_data_schema_models.utils import create_literal_class, read_csv, one_of_instance


class MouseAnatomyModel(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    id: int = Field(..., title="Structure EMAPA ID")
    name: str = Field(..., title="Structure name")
    registry: RegistryModel = None
    registry_identifier: str = None


mouse_objects = read_csv(str(files("aind_data_schema_models.models").joinpath("mouse_dev_anat_ontology.csv")))

MouseAnatomicalStructure = create_literal_class(
    objects=mouse_objects,
    class_name="MouseAnatomyType",
    base_model=MouseAnatomyModel,
    discriminator="id",
    field_handlers={"registry_abbreviation": map_registry},
    class_module=__name__,
)

MouseAnatomicalStructure.EMG_MUSCLES = one_of_instance([
    MouseAnatomicalStructure.DELTOID,
    MouseAnatomicalStructure.PECTORALIS_MAJOR,
    MouseAnatomicalStructure.TRICEPS_BRACHII,
    MouseAnatomicalStructure.BICEPS_BRACHII,
    MouseAnatomicalStructure.PARS_SCAPULARIS_OF_DELTOID,
    MouseAnatomicalStructure.EXTENSOR_CARPI_RADIALIS_LONGUS,
    MouseAnatomicalStructure.EXTENSOR_DIGITORUM_COMMUNIS,
    MouseAnatomicalStructure.EXTENSOR_DIGITORUM_LATERALIS,
    MouseAnatomicalStructure.EXTENSOR_CARPI_ULNARIS,
    MouseAnatomicalStructure.FLEXOR_CARPI_RADIALIS,
    MouseAnatomicalStructure.FLEXOR_CARPI_ULNARIS,
    MouseAnatomicalStructure.FLEXOR_DIGITORUM_PROFUNDUS,
])
