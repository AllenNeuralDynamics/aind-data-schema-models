"""Module for Organization definitions, including manufacturers, institutions, and vendors"""

from typing import Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.registries import RegistryModel, map_registry
from aind_data_schema_models.utils import create_literal_class, read_csv


class OrganizationModel(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str
    abbreviation: str = None
    registry: RegistryModel = None
    registry_identifier: str = None


Organization = create_literal_class(
    objects=read_csv("models/organizations.csv"),
    class_name="Organization",
    base_model=OrganizationModel,
    discriminator="name",
    field_handlers={"registry_abbreviation": map_registry},
    class_module=__name__,
)


@classmethod
def from_abbreviation(cls, abbreviation: str):
    return cls._abbreviation_map[abbreviation]


@classmethod
def from_name(cls, name: str):
    return cls._name_map[name]


Organization._abbreviation_map = {m().abbreviation: m() for m in Organization._ALL}
Organization._name_map = {m().name: m() for m in Organization._ALL}
Organization.from_abbreviation = from_abbreviation
Organization.from_name = from_name


Organization.DETECTOR_MANUFACTURERS = Annotated[
    Union[
        Organization.AilipuTechnologyCo,
        Organization.Allied,
        Organization.Basler,
        Organization.Dodotronic,
        Organization.EdmundOptics,
        Organization.Hamamatsu,
        Organization.Spinnaker,
        Organization.TeledyneFlir,
        Organization.TheImagingSource,
        Organization.Thorlabs,
        Organization.Vieworks,
        Organization.Other,
    ],
    Field(discriminator="name"),
]

Organization.FILTER_MANUFACTURERS = Annotated[
    Union[
        Organization.Chroma,
        Organization.EdmundOptics,
        Organization.MidwestOpticalSystemsInc,
        Organization.Semrock,
        Organization.Thorlabs,
        Organization.Other,
    ],
    Field(discriminator="name"),
]

Organization.LENS_MANUFACTURERS = Annotated[
    Union[
        Organization.Computar,
        Organization.EdmundOptics,
        Organization.Fujinon,
        Organization.Hamamatsu,
        Organization.InfinityPhotoOptical,
        Organization.Leica,
        Organization.Mitutuyo,
        Organization.Navitar,
        Organization.Nikon,
        Organization.Olympus,
        Organization.SchneiderKreuznach,
        Organization.Thorlabs,
        Organization.CarlZeiss,
        Organization.Other,
    ],
    Field(discriminator="name"),
]

Organization.DAQ_DEVICE_MANUFACTURERS = Annotated[
    Union[
        Organization.AllenInstituteForNeuralDynamics,
        Organization.ChampalimaudFoundation,
        Organization.NationalInstruments,
        Organization.InteruniversityMicroelectronicsCenter,
        Organization.OpenEphysProductionSite,
        Organization.SecondOrderEffects,
        Organization.Other,
    ],
    Field(discriminator="name"),
]

Organization.LASER_MANUFACTURERS = Annotated[
    Union[
        Organization.CoherentScientific,
        Organization.Hamamatsu,
        Organization.Oxxius,
        Organization.Quantifi,
        Organization.Vortran,
        Organization.Other,
    ],
    Field(discriminator="name"),
]

Organization.LED_MANUFACTURERS = Annotated[
    Union[
        Organization.AmsOsram,
        Organization.Doric,
        Organization.Prizmatix,
        Organization.Thorlabs,
        Organization.Other,
    ],
    Field(discriminator="name"),
]

Organization.MANIPULATOR_MANUFACTURERS = Annotated[
    Union[Organization.NewScaleTechnologies, Organization.Other], Field(discriminator="name")
]

Organization.MONITOR_MANUFACTURERS = Annotated[
    Union[Organization.Asus, Organization.Lg, Organization.Other], Field(discriminator="name")
]

Organization.SPEAKER_MANUFACTURERS = Annotated[
    Union[Organization.Tymphany, Organization.IslProductsInternational, Organization.Other],
    Field(discriminator="name"),
]

Organization.FUNDERS = Annotated[
    Union[
        Organization.AllenInstitute,
        Organization.ChanZuckerbergInitiative,
        Organization.MbfBioscience,
        Organization.MichaelJFoxFoundationForParkinsonsResearch,
        Organization.NationalCenterForComplementaryAndIntegrativeHealth,
        Organization.NationalInstituteOfMentalHealth,
        Organization.NationalInstituteOfNeurologicalDisordersAndStroke,
        Organization.SimonsFoundation,
        Organization.TempletonWorldCharityFoundation,
    ],
    Field(discriminator="name"),
]

Organization.RESEARCH_INSTITUTIONS = Annotated[
    Union[
        Organization.AllenInstituteForBrainScience,
        Organization.AllenInstituteForNeuralDynamics,
        Organization.ColumbiaUniversity,
        Organization.HuazhongUniversityOfScienceAndTechnology,
        Organization.JaneliaResearchCampus,
        Organization.NewYorkUniversity,
        Organization.Other,
    ],
    Field(discriminator="name"),
]

Organization.SUBJECT_SOURCES = Annotated[
    Union[
        Organization.AllenInstitute,
        Organization.ColumbiaUniversity,
        Organization.HuazhongUniversityOfScienceAndTechnology,
        Organization.JaneliaResearchCampus,
        Organization.JacksonLaboratory,
        Organization.NewYorkUniversity,
        Organization.Other,
    ],
    Field(discriminator="name"),
]
