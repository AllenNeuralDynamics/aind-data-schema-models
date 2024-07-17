"""Module for Organization definitions, including manufacturers, institutions, and vendors"""

from typing import Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.registries import RegistryModel, map_registry
from aind_data_schema_models.utils import create_literal_class, one_of_instance, read_csv


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
    """look up an Organization by its abbreviation"""
    return cls._abbreviation_map[abbreviation]


@classmethod
def from_name(cls, name: str):
    """look up an Organization by its name"""
    return cls._name_map[name]


Organization._abbreviation_map = {m().abbreviation: m() for m in Organization._ALL}
Organization._name_map = {m().name: m() for m in Organization._ALL}
Organization.from_abbreviation = from_abbreviation
Organization.from_name = from_name


Organization.DETECTOR_MANUFACTURERS = one_of_instance(
    [
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
    ]
)

Organization.FILTER_MANUFACTURERS = one_of_instance(
    [
        Organization.Chroma,
        Organization.EdmundOptics,
        Organization.MidwestOpticalSystemsInc,
        Organization.Semrock,
        Organization.Thorlabs,
        Organization.Other,
    ]
)

Organization.LENS_MANUFACTURERS = one_of_instance(
    [
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
    ]
)

Organization.DAQ_DEVICE_MANUFACTURERS = one_of_instance(
    [
        Organization.AllenInstituteForNeuralDynamics,
        Organization.ChampalimaudFoundation,
        Organization.NationalInstruments,
        Organization.InteruniversityMicroelectronicsCenter,
        Organization.OpenEphysProductionSite,
        Organization.SecondOrderEffects,
        Organization.Other,
    ]
)

Organization.LASER_MANUFACTURERS = one_of_instance(
    [
        Organization.CoherentScientific,
        Organization.Hamamatsu,
        Organization.Oxxius,
        Organization.Quantifi,
        Organization.Vortran,
        Organization.Other,
    ]
)

Organization.LED_MANUFACTURERS = one_of_instance(
    [Organization.AmsOsram, Organization.Doric, Organization.Prizmatix, Organization.Thorlabs, Organization.Other]
)

Organization.MANIPULATOR_MANUFACTURERS = one_of_instance([Organization.NewScaleTechnologies, Organization.Other])

Organization.MONITOR_MANUFACTURERS = one_of_instance([Organization.Asus, Organization.Lg, Organization.Other])

Organization.SPEAKER_MANUFACTURERS = one_of_instance(
    [Organization.Tymphany, Organization.IslProductsInternational, Organization.Other]
)

Organization.FUNDERS = one_of_instance(
    [
        Organization.AllenInstitute,
        Organization.ChanZuckerbergInitiative,
        Organization.MbfBioscience,
        Organization.MichaelJFoxFoundationForParkinsonsResearch,
        Organization.NationalCenterForComplementaryAndIntegrativeHealth,
        Organization.NationalInstituteOfMentalHealth,
        Organization.NationalInstituteOfNeurologicalDisordersAndStroke,
        Organization.SimonsFoundation,
        Organization.TempletonWorldCharityFoundation,
    ]
)

Organization.RESEARCH_INSTITUTIONS = one_of_instance(
    [
        Organization.AllenInstituteForBrainScience,
        Organization.AllenInstituteForNeuralDynamics,
        Organization.ColumbiaUniversity,
        Organization.HuazhongUniversityOfScienceAndTechnology,
        Organization.JaneliaResearchCampus,
        Organization.NewYorkUniversity,
        Organization.Other,
    ]
)

Organization.SUBJECT_SOURCES = one_of_instance(
    [
        Organization.AllenInstitute,
        Organization.ColumbiaUniversity,
        Organization.HuazhongUniversityOfScienceAndTechnology,
        Organization.JaneliaResearchCampus,
        Organization.JacksonLaboratory,
        Organization.NewYorkUniversity,
        Organization.Other,
    ]
)
