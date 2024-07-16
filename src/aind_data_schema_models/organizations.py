"""Module for Organization definitions, including manufacturers, institutions, and vendors"""

from typing import Literal, Union

from pydantic import ConfigDict, Field, BaseModel
from typing_extensions import Annotated
import pandas as pd
from aind_data_schema_models.utils import create_literal_class
from aind_data_schema_models.registry import Registry, Registries, map_registry


class Organization(BaseModel):
    """Base model config"""

    model_config = ConfigDict(frozen=True)

    name: str
    abbreviation: str = None
    registry: Registry = None
    registry_identifier: str = None


Organizations = create_literal_class(
    objects=pd.read_csv('models/organizations.csv', keep_default_na=False).to_dict(orient='records'), 
    class_name='Organizations', 
    base_model=Organization, 
    discriminator='name',
    field_handlers={'registry_abbreviation': map_registry},
    class_module=__name__
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
        Organizations.TeledyneFLIR,
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
        Organizations.Other
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
        Organizations.AllenInstituteforNeuralDynamics,
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
        Organizations.Other
    ], 
    Field(discriminator="name")
]
    
Organizations.LED_MANUFACTURERS = Annotated[
    Union[
        Organizations.amsOSRAM, 
        Organizations.Doric, 
        Organizations.Prizmatix, 
        Organizations.Thorlabs, 
        Organizations.Other
    ], 
    Field(discriminator="name")]

Organizations.MANIPULATOR_MANUFACTURERS = Annotated[
    Union[
        Organizations.NewScaleTechnologies, 
        Organizations.Other
    ], 
    Field(discriminator="name")
]

Organizations.MONITOR_MANUFACTURERS = Annotated[
    Union[
        Organizations.ASUS, 
        Organizations.LG, 
        Organizations.Other
    ], 
Field(discriminator="name")]

Organizations.SPEAKER_MANUFACTURERS = Annotated[
    Union[
        Organizations.Tymphany, 
        Organizations.ISLProductsInternational, 
        Organizations.Other
    ], 
Field(discriminator="name")]

Organizations.FUNDERS = Annotated[
    Union[
        Organizations.AllenInstitute,
        Organizations.ChanZuckerbergInitiative,
        Organizations.MBFBioscience,
        Organizations.MichaelJFoxFoundationforParkinsonsResearch,
        Organizations.NationalCenterforComplementaryandIntegrativeHealth,
        Organizations.NationalInstituteofMentalHealth,
        Organizations.NationalInstituteofNeurologicalDisordersandStroke,
        Organizations.SimonsFoundation,
        Organizations.TempletonWorldCharityFoundation,
    ],
    Field(discriminator="name"),
]

Organizations.RESEARCH_INSTITUTIONS = Annotated[
    Union[
        Organizations.AllenInstituteforBrainScience,
        Organizations.AllenInstituteforNeuralDynamics,
        Organizations.ColumbiaUniversity,
        Organizations.HuazhongUniversityofScienceandTechnology,
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
        Organizations.HuazhongUniversityofScienceandTechnology,
        Organizations.JaneliaResearchCampus,
        Organizations.JacksonLaboratory,
        Organizations.NewYorkUniversity,
        Organizations.Other,
    ],
    Field(discriminator="name"),
]