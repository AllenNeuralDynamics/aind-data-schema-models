"""Module for Organization definitions, including manufacturers, institutions, and vendors"""

from typing import Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.registries import Registry, map_registry
from aind_data_schema_models.utils import create_literal_class, read_csv


class Organization(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str
    abbreviation: str = None
    registry: Registry = None
    registry_identifier: str = None


Organizations = create_literal_class(
    objects=read_csv("models/organizations.csv"),
    class_name="Organizations",
    base_model=Organization,
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


Organizations._abbreviation_map = {m().abbreviation: m() for m in Organizations._ALL}
Organizations._name_map = {m().name: m() for m in Organizations._ALL}
Organizations.from_abbreviation = from_abbreviation
Organizations.from_name = from_name


Organizations.DETECTOR_MANUFACTURERS = Annotated[
    Union[
        Organizations.AilipuTechnologyCo,
        Organizations.Allied,
        Organizations.Basler,
        Organizations.Dodotronic,
        Organizations.EdmundOptics,
        Organizations.Hamamatsu,
        Organizations.Spinnaker,
        Organizations.TeledyneFlir,
        Organizations.TheImagingSource,
        Organizations.Thorlabs,
        Organizations.Vieworks,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]

Organizations.FILTER_MANUFACTURERS = Annotated[
    Union[
        Organizations.Chroma,
        Organizations.EdmundOptics,
        Organizations.MidwestOpticalSystemsInc,
        Organizations.Semrock,
        Organizations.Thorlabs,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]

Organizations.LENS_MANUFACTURERS = Annotated[
    Union[
        Organizations.Computar,
        Organizations.EdmundOptics,
        Organizations.Fujinon,
        Organizations.Hamamatsu,
        Organizations.InfinityPhotoOptical,
        Organizations.Leica,
        Organizations.Mitutuyo,
        Organizations.Navitar,
        Organizations.Nikon,
        Organizations.Olympus,
        Organizations.SchneiderKreuznach,
        Organizations.Thorlabs,
        Organizations.CarlZeiss,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]

Organizations.DAQ_DEVICE_MANUFACTURERS = Annotated[
    Union[
        Organizations.AllenInstituteForNeuralDynamics,
        Organizations.ChampalimaudFoundation,
        Organizations.NationalInstruments,
        Organizations.InteruniversityMicroelectronicsCenter,
        Organizations.OpenEphysProductionSite,
        Organizations.SecondOrderEffects,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]

Organizations.LASER_MANUFACTURERS = Annotated[
    Union[
        Organizations.CoherentScientific,
        Organizations.Hamamatsu,
        Organizations.Oxxius,
        Organizations.Quantifi,
        Organizations.Vortran,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]

Organizations.LED_MANUFACTURERS = Annotated[
    Union[
        Organizations.AmsOsram,
        Organizations.Doric,
        Organizations.Prizmatix,
        Organizations.Thorlabs,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]

Organizations.MANIPULATOR_MANUFACTURERS = Annotated[
    Union[Organizations.NewScaleTechnologies, Organizations.Other], Field(discriminator="name")
]

Organizations.MONITOR_MANUFACTURERS = Annotated[
    Union[Organizations.Asus, Organizations.Lg, Organizations.Other], Field(discriminator="name")
]

Organizations.SPEAKER_MANUFACTURERS = Annotated[
    Union[Organizations.Tymphany, Organizations.IslProductsInternational, Organizations.Other],
    Field(discriminator="name"),
]

Organizations.FUNDERS = Annotated[
    Union[
        Organizations.AllenInstitute,
        Organizations.ChanZuckerbergInitiative,
        Organizations.MbfBioscience,
        Organizations.MichaelJFoxFoundationForParkinsonsResearch,
        Organizations.NationalCenterForComplementaryAndIntegrativeHealth,
        Organizations.NationalInstituteOfMentalHealth,
        Organizations.NationalInstituteOfNeurologicalDisordersAndStroke,
        Organizations.SimonsFoundation,
        Organizations.TempletonWorldCharityFoundation,
    ],
    Field(discriminator="name"),
]

Organizations.RESEARCH_INSTITUTIONS = Annotated[
    Union[
        Organizations.AllenInstituteForBrainScience,
        Organizations.AllenInstituteForNeuralDynamics,
        Organizations.ColumbiaUniversity,
        Organizations.HuazhongUniversityOfScienceAndTechnology,
        Organizations.JaneliaResearchCampus,
        Organizations.NewYorkUniversity,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]

Organizations.SUBJECT_SOURCES = Annotated[
    Union[
        Organizations.AllenInstitute,
        Organizations.ColumbiaUniversity,
        Organizations.HuazhongUniversityOfScienceAndTechnology,
        Organizations.JaneliaResearchCampus,
        Organizations.JacksonLaboratory,
        Organizations.NewYorkUniversity,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]
