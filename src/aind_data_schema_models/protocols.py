"""Protocols"""

from typing import Literal, Union

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.pid_names import BaseName
from aind_data_schema_models.registries import Registry


class ProtocolModel(BaseName):
    """Base model for protocol"""

    model_config = ConfigDict(frozen=True)
    title: str
    authors: list[str]
    registry: Registry
    registry_identifier: str


class _Solenoid_Valve_Calibration_For_Behavior_Rigs_Utilizing_Water_Reward(ProtocolModel):
    """Model Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"""

    title: Literal["Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"] = (
        "Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"
    )
    authors: list[str] = [
        "Ella Hilton-VanOsdall",
        "Heston Smith",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.261gerq7dl47/v1"] = "10.17504/protocols.io.261gerq7dl47/v1"


class _Stereotaxic_Injection_By_Iontophoresis(ProtocolModel):
    """Model Stereotaxic Injection by Iontophoresis"""

    title: Literal["Stereotaxic Injection by Iontophoresis"] = "Stereotaxic Injection by Iontophoresis"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.14egn8ewzg5d/v6"] = "10.17504/protocols.io.14egn8ewzg5d/v6"


class _Stereotaxic_Injection_By_Nanoject_Protocol(ProtocolModel):
    """Model Stereotaxic Injection by Nanoject Protocol"""

    title: Literal["Stereotaxic Injection by Nanoject Protocol"] = "Stereotaxic Injection by Nanoject Protocol"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.bp2l6nr7kgqe/v6"] = "10.17504/protocols.io.bp2l6nr7kgqe/v6"


class _Plug_Removal_For_Acute_In_Vivo_Electrophysiology_Experiments(ProtocolModel):
    """Model Plug Removal for acute in vivo Electrophysiology Experiments"""

    title: Literal["Plug Removal for acute in vivo Electrophysiology Experiments"] = (
        "Plug Removal for acute in vivo Electrophysiology Experiments"
    )
    authors: list[str] = [
        "Ryan Gillis",
        "Mikayla Carlson",
        "Severine Durand",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.eq2lywz8qvx9/v1"] = "10.17504/protocols.io.eq2lywz8qvx9/v1"


class _Dual_Hemisphere_Craniotomy_For_Electrophysiology(ProtocolModel):
    """Model Dual Hemisphere Craniotomy for Electrophysiology"""

    title: Literal["Dual Hemisphere Craniotomy for Electrophysiology"] = (
        "Dual Hemisphere Craniotomy for Electrophysiology"
    )
    authors: list[str] = [
        "Anna Lakunina",
        "Conor Grasso",
        "Benjamin Barad",
        "Avalon Amaya",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.rm7vzjoe2lx1/v1"] = "10.17504/protocols.io.rm7vzjoe2lx1/v1"


class _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery(ProtocolModel):
    """Model General Setup and Takedown Procedures for Rodent Neurosurgery"""

    title: Literal["General Setup and Takedown Procedures for Rodent Neurosurgery"] = (
        "General Setup and Takedown Procedures for Rodent Neurosurgery"
    )
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
        "Ali Williford",
        "Robert E Howard",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.kqdg392o7g25/v2"] = "10.17504/protocols.io.kqdg392o7g25/v2"


class _Multiplexed_Rna_Fish_On_Expanded_Mouse_Brain_Slices(ProtocolModel):
    """Model Multiplexed RNA FISH on Expanded Mouse Brain Slices"""

    title: Literal["Multiplexed RNA FISH on Expanded Mouse Brain Slices"] = (
        "Multiplexed RNA FISH on Expanded Mouse Brain Slices"
    )
    authors: list[str] = [
        "Rachel Flannery",
        "Molly Logsdon",
        "Laura Roy",
        "Kevin Cao",
        "Jayaram Chandrashekar",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.dm6gpzj28lzp/v1"] = "10.17504/protocols.io.dm6gpzj28lzp/v1"


class _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Hardware(ProtocolModel):
    """Model Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"""

    title: Literal["Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"] = (
        "Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"
    )
    authors: list[str] = [
        "Kenta M. Hagihara",
        "Bryan J MacLennan",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.261ge39edl47/v2"] = "10.17504/protocols.io.261ge39edl47/v2"


class _Mouse_Water_Restriction(ProtocolModel):
    """Model Mouse Water Restriction"""

    title: Literal["Mouse Water Restriction"] = "Mouse Water Restriction"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.x54v9pn34g3e/v1"] = "10.17504/protocols.io.x54v9pn34g3e/v1"


class _Mouse_Habituation_Head_Fixation_Into_Tube(ProtocolModel):
    """Model Mouse Habituation - Head Fixation into Tube"""

    title: Literal["Mouse Habituation - Head Fixation into Tube"] = "Mouse Habituation - Head Fixation into Tube"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.rm7vzxd74gx1/v1"] = "10.17504/protocols.io.rm7vzxd74gx1/v1"


class Protocols:
    """Protocols"""

    SOLENOID_VALVE_CALIBRATION_FOR_BEHAVIOR_RIGS_UTILIZING_WATER_REWARD = (
        _Solenoid_Valve_Calibration_For_Behavior_Rigs_Utilizing_Water_Reward()
    )
    STEREOTAXIC_INJECTION_BY_IONTOPHORESIS = _Stereotaxic_Injection_By_Iontophoresis()
    STEREOTAXIC_INJECTION_BY_NANOJECT_PROTOCOL = _Stereotaxic_Injection_By_Nanoject_Protocol()
    PLUG_REMOVAL_FOR_ACUTE_IN_VIVO_ELECTROPHYSIOLOGY_EXPERIMENTS = (
        _Plug_Removal_For_Acute_In_Vivo_Electrophysiology_Experiments()
    )
    DUAL_HEMISPHERE_CRANIOTOMY_FOR_ELECTROPHYSIOLOGY = _Dual_Hemisphere_Craniotomy_For_Electrophysiology()
    GENERAL_SETUP_AND_TAKEDOWN_PROCEDURES_FOR_RODENT_NEUROSURGERY = (
        _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery()
    )
    MULTIPLEXED_RNA_FISH_ON_EXPANDED_MOUSE_BRAIN_SLICES = _Multiplexed_Rna_Fish_On_Expanded_Mouse_Brain_Slices()
    MODIFIED_FRAME_PROJECTED__INDEPENDENT_FIBER__PHOTOMETRY__FIP__SYSTEM_HARDWARE = (
        _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Hardware()
    )
    MOUSE_WATER_RESTRICTION = _Mouse_Water_Restriction()
    MOUSE_HABITUATION___HEAD_FIXATION_INTO_TUBE = _Mouse_Habituation_Head_Fixation_Into_Tube()

    ALL = tuple(ProtocolModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(ProtocolModel.__subclasses__())], Field(discriminator="title")]
