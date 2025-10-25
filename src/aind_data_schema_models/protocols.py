"""Protocols"""

from typing import Literal, Union

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.pid_names import BaseName
from aind_data_schema_models.registries import Registry


class ProtocolModel(BaseName):
    """Base model for protocol"""

    model_config = ConfigDict(frozen=True)
    name: str
    authors: list[str]
    registry: Registry
    registry_identifier: str


class _Solenoid_Valve_Calibration_For_Behavior_Rigs_Utilizing_Water_Reward(ProtocolModel):
    """Model Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"""

    name: Literal["Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"] = (
        "Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"
    )
    authors: list[str] = [
        "Ella Hilton-VanOsdall",
        "Heston Smith",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.261gerq7dl47/v1"] = "10.17504/protocols.io.261gerq7dl47/v1"


class _Stereotaxic_Injection_By_Nanoject_Protocol(ProtocolModel):
    """Model Stereotaxic Injection by Nanoject Protocol"""

    name: Literal["Stereotaxic Injection by Nanoject Protocol"] = "Stereotaxic Injection by Nanoject Protocol"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.bp2l6nr7kgqe/v6"] = "10.17504/protocols.io.bp2l6nr7kgqe/v6"


class _Stereotaxic_Injection_By_Iontophoresis(ProtocolModel):
    """Model Stereotaxic Injection by Iontophoresis"""

    name: Literal["Stereotaxic Injection by Iontophoresis"] = "Stereotaxic Injection by Iontophoresis"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.14egn8ewzg5d/v6"] = "10.17504/protocols.io.14egn8ewzg5d/v6"


class _Mouse_Habituation_Head_Fixation_On_Disk(ProtocolModel):
    """Model Mouse Habituation - Head Fixation on Disk"""

    name: Literal["Mouse Habituation - Head Fixation on Disk"] = "Mouse Habituation - Head Fixation on Disk"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.j8nlkojmxv5r/v1"] = "10.17504/protocols.io.j8nlkojmxv5r/v1"


class _Mouse_Water_Restriction(ProtocolModel):
    """Model Mouse Water Restriction"""

    name: Literal["Mouse Water Restriction"] = "Mouse Water Restriction"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.x54v9pn34g3e/v1"] = "10.17504/protocols.io.x54v9pn34g3e/v1"


class _Mouse_Habituation_Head_Fixation_Into_Tube(ProtocolModel):
    """Model Mouse Habituation - Head Fixation into Tube"""

    name: Literal["Mouse Habituation - Head Fixation into Tube"] = "Mouse Habituation - Head Fixation into Tube"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.rm7vzxd74gx1/v1"] = "10.17504/protocols.io.rm7vzxd74gx1/v1"


class _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Hardware(ProtocolModel):
    """Model Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"""

    name: Literal["Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"] = (
        "Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"
    )
    authors: list[str] = [
        "Kenta M. Hagihara",
        "Bryan J MacLennan",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.261ge39edl47/v2"] = "10.17504/protocols.io.261ge39edl47/v2"


class _Making_Agarose_For_Use_In_Acute_In_Vivo_Electrophysiology_Experiments_(ProtocolModel):
    """Model Making Agarose for use in acute in vivo Electrophysiology Experiments"""

    name: Literal["Making Agarose for use in acute in vivo Electrophysiology Experiments "] = (
        "Making Agarose for use in acute in vivo Electrophysiology Experiments "
    )
    authors: list[str] = [
        "Ryan Gillis",
        "Mikayla Carlson",
        "Severine Durand",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.5jyl8py89g2w/v1"] = "10.17504/protocols.io.5jyl8py89g2w/v1"


class _Plug_Removal_For_Acute_In_Vivo_Electrophysiology_Experiments(ProtocolModel):
    """Model Plug Removal for acute in vivo Electrophysiology Experiments"""

    name: Literal["Plug Removal for acute in vivo Electrophysiology Experiments"] = (
        "Plug Removal for acute in vivo Electrophysiology Experiments"
    )
    authors: list[str] = [
        "Ryan Gillis",
        "Mikayla Carlson",
        "Severine Durand",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.eq2lywz8qvx9/v1"] = "10.17504/protocols.io.eq2lywz8qvx9/v1"


class _Intraperitoneal_Injection_In_An_Adult_Mouse(ProtocolModel):
    """Model Intraperitoneal Injection in an Adult Mouse"""

    name: Literal["Intraperitoneal Injection in an Adult Mouse"] = "Intraperitoneal Injection in an Adult Mouse"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.5qpvo5w8dl4o/v2"] = "10.17504/protocols.io.5qpvo5w8dl4o/v2"


class _Multiplexed_Rna_Fish_On_Expanded_Mouse_Brain_Slices(ProtocolModel):
    """Model Multiplexed RNA FISH on Expanded Mouse Brain Slices"""

    name: Literal["Multiplexed RNA FISH on Expanded Mouse Brain Slices"] = (
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


class _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery(ProtocolModel):
    """Model General Setup and Takedown Procedures for Rodent Neurosurgery"""

    name: Literal["General Setup and Takedown Procedures for Rodent Neurosurgery"] = (
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


class _Dual_Hemisphere_Craniotomy_For_Electrophysiology(ProtocolModel):
    """Model Dual Hemisphere Craniotomy for Electrophysiology"""

    name: Literal["Dual Hemisphere Craniotomy for Electrophysiology"] = (
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


class _Aqueous_Sbip_Delipidation_For_Whole_Mouse_Brain_After_Morphofish_Perfusion_(ProtocolModel):
    """Model Aqueous (SBiP) Delipidation for Whole Mouse Brain After morphoFISH Perfusion"""

    name: Literal["Aqueous (SBiP) Delipidation for Whole Mouse Brain After morphoFISH Perfusion "] = (
        "Aqueous (SBiP) Delipidation for Whole Mouse Brain After morphoFISH Perfusion "
    )
    authors: list[str] = [
        "Monique Copeland",
        "MouseLight Project Team",
        "Tiago A Ferreira",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.rm7vzjz54lx1/v1"] = "10.17504/protocols.io.rm7vzjz54lx1/v1"


class _Mouse_Habituation_Head_Fixation_On_Disk(ProtocolModel):
    """Model Mouse Habituation - Head Fixation on Disk"""

    name: Literal["Mouse Habituation - Head Fixation on Disk"] = "Mouse Habituation - Head Fixation on Disk"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.j8nlkojmxv5r/v2"] = "10.17504/protocols.io.j8nlkojmxv5r/v2"


class _Preparation_Of_Lipopolysaccharide_For_Intraperitoneal_Injection(ProtocolModel):
    """Model Preparation of Lipopolysaccharide for Intraperitoneal Injection"""

    name: Literal["Preparation of Lipopolysaccharide for Intraperitoneal Injection"] = (
        "Preparation of Lipopolysaccharide for Intraperitoneal Injection"
    )
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.14egn9y1ml5d/v1"] = "10.17504/protocols.io.14egn9y1ml5d/v1"


class _Temporal_Assessment_Of_Immune_Response(ProtocolModel):
    """Model Temporal Assessment of Immune Response"""

    name: Literal["Temporal Assessment of Immune Response"] = "Temporal Assessment of Immune Response"
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.5jyl8dqx6g2w/v1"] = "10.17504/protocols.io.5jyl8dqx6g2w/v1"


class _Mouse_Vab_Catheter_Maintenance(ProtocolModel):
    """Model Mouse VAB Catheter Maintenance"""

    name: Literal["Mouse VAB Catheter Maintenance"] = "Mouse VAB Catheter Maintenance"
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.8epv52o5dv1b/v1"] = "10.17504/protocols.io.8epv52o5dv1b/v1"


class _Processing_Blood_Intended_For_Olink_Assay(ProtocolModel):
    """Model Processing Blood Intended for Olink Assay"""

    name: Literal["Processing Blood Intended for Olink Assay"] = "Processing Blood Intended for Olink Assay"
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.261ger81jl47/v1"] = "10.17504/protocols.io.261ger81jl47/v1"


class _Barseq_2_5(ProtocolModel):
    """Model BARseq 2.5"""

    name: Literal["BARseq 2.5"] = "BARseq 2.5"
    authors: list[str] = [
        "Jonathan Wang",
        "Yoh Isogai",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.kqdg3ke9qv25/v1"] = "10.17504/protocols.io.kqdg3ke9qv25/v1"


class _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain(ProtocolModel):
    """Model Aqueous (SBiP) Delipidation of a Whole Mouse Brain"""

    name: Literal["Aqueous (SBiP) Delipidation of a Whole Mouse Brain"] = (
        "Aqueous (SBiP) Delipidation of a Whole Mouse Brain"
    )
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Judith Baka",
        "Jayaram Chandrashekar",
        "Rajvi Javeri",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.n2bvj81mwgk5/v2"] = "10.17504/protocols.io.n2bvj81mwgk5/v2"


class _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain(ProtocolModel):
    """Model Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"""

    name: Literal["Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"] = (
        "Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"
    )
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Jayaram Chandrashekar",
        "Rajvi Javeri",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.36wgqj1kxvk5/v2"] = "10.17504/protocols.io.36wgqj1kxvk5/v2"


class _Imaging_Cleared_Mouse_Brains_On_Smartspim(ProtocolModel):
    """Model Imaging cleared mouse brains on SmartSPIM"""

    name: Literal["Imaging cleared mouse brains on SmartSPIM"] = "Imaging cleared mouse brains on SmartSPIM"
    authors: list[str] = [
        "John Rohde",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.3byl4jo1rlo5/v1"] = "10.17504/protocols.io.3byl4jo1rlo5/v1"


class _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery(ProtocolModel):
    """Model General Setup and Takedown Procedures for Rodent Neurosurgery"""

    name: Literal["General Setup and Takedown Procedures for Rodent Neurosurgery"] = (
        "General Setup and Takedown Procedures for Rodent Neurosurgery"
    )
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
        "Ali Williford",
        "Robert E Howard",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.kqdg392o7g25/v1"] = "10.17504/protocols.io.kqdg392o7g25/v1"


class _Whole_Mouse_Brain_Delipidation_Immunolabeling_And_Expansion_Microscopy(ProtocolModel):
    """Model Whole Mouse Brain Delipidation, Immunolabeling, and Expansion Microscopy"""

    name: Literal["Whole Mouse Brain Delipidation, Immunolabeling, and Expansion Microscopy"] = (
        "Whole Mouse Brain Delipidation, Immunolabeling, and Expansion Microscopy"
    )
    authors: list[str] = [
        "Naveen Ouellette",
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Jayaram Chandrashekar",
        "Molly Logsdon",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.n92ldpwjxl5b/v1"] = "10.17504/protocols.io.n92ldpwjxl5b/v1"


class _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain(ProtocolModel):
    """Model Aqueous (SBiP) Delipidation of a Whole Mouse Brain"""

    name: Literal["Aqueous (SBiP) Delipidation of a Whole Mouse Brain"] = (
        "Aqueous (SBiP) Delipidation of a Whole Mouse Brain"
    )
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Judith Baka",
        "Jayaram Chandrashekar",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.n2bvj81mwgk5/v1"] = "10.17504/protocols.io.n2bvj81mwgk5/v1"


class _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain(ProtocolModel):
    """Model Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"""

    name: Literal["Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"] = (
        "Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"
    )
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Jayaram Chandrashekar",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.36wgqj1kxvk5/v1"] = "10.17504/protocols.io.36wgqj1kxvk5/v1"


class _Immunolabeling_Of_A_Whole_Mouse_Brain(ProtocolModel):
    """Model Immunolabeling of a Whole Mouse Brain"""

    name: Literal["Immunolabeling of a Whole Mouse Brain"] = "Immunolabeling of a Whole Mouse Brain"
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Naveen Ouellette",
        "Jayaram Chandrashekar",
        "Molly Logsdon",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.ewov1okwylr2/v1"] = "10.17504/protocols.io.ewov1okwylr2/v1"


class _Structural_Mri_Using_The_University_Of_Washington_14T_Vertical_Bore_Bruker_Mri(ProtocolModel):
    """Model Structural MRI Using the University of Washington 14T Vertical Bore Bruker MRI"""

    name: Literal["Structural MRI Using the University of Washington 14T Vertical Bore Bruker MRI"] = (
        "Structural MRI Using the University of Washington 14T Vertical Bore Bruker MRI"
    )
    authors: list[str] = [
        "Yoni Browning",
        "Galen Lynch",
        "Josh Siegle",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.3byl4j8p2lo5/v1"] = "10.17504/protocols.io.3byl4j8p2lo5/v1"


class _Duragel_Application_For_Acute_Electrophysiology_Recordings(ProtocolModel):
    """Model Duragel Application for Acute Electrophysiology Recordings"""

    name: Literal["Duragel Application for Acute Electrophysiology Recordings"] = (
        "Duragel Application for Acute Electrophysiology Recordings"
    )
    authors: list[str] = [
        "Anna Lakunina",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.14egn2dwqg5d/v1"] = "10.17504/protocols.io.14egn2dwqg5d/v1"


class _Smartspim_Setup_And_Alignment(ProtocolModel):
    """Model SmartSPIM setup and alignment"""

    name: Literal["SmartSPIM setup and alignment"] = "SmartSPIM setup and alignment"
    authors: list[str] = [
        "John Rohde",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.5jyl8jyb7g2w/v1"] = "10.17504/protocols.io.5jyl8jyb7g2w/v1"


class _Refractive_Index_Matching_Easyindex(ProtocolModel):
    """Model Refractive Index Matching - EasyIndex"""

    name: Literal["Refractive Index Matching - EasyIndex"] = "Refractive Index Matching - EasyIndex"
    authors: list[str] = [
        "Holly Myers",
        "Daphne Toglia",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.kxygx965kg8j/v1"] = "10.17504/protocols.io.kxygx965kg8j/v1"


class _Preparing_A_3D_Printed_Implant_For_Acute_In_Vivo_Electrophysiology(ProtocolModel):
    """Model Preparing a 3D Printed Implant for Acute In Vivo Electrophysiology"""

    name: Literal["Preparing a 3D Printed Implant for Acute In Vivo Electrophysiology"] = (
        "Preparing a 3D Printed Implant for Acute In Vivo Electrophysiology"
    )
    authors: list[str] = [
        "Xinxin Yin",
        "Anna Lakunina",
        "Josh Siegle",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.6qpvr4jmogmk/v1"] = "10.17504/protocols.io.6qpvr4jmogmk/v1"


class _Mouse_Cardiac_Perfusion_Fixation_And_Brain_Collection(ProtocolModel):
    """Model Mouse Cardiac Perfusion Fixation and Brain Collection"""

    name: Literal["Mouse Cardiac Perfusion Fixation and Brain Collection"] = (
        "Mouse Cardiac Perfusion Fixation and Brain Collection"
    )
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.bg5vjy66"] = "10.17504/protocols.io.bg5vjy66"


class _Whole_Mouse_Brain_Delipidation_Dichloromethane(ProtocolModel):
    """Model Whole Mouse Brain Delipidation - Dichloromethane"""

    name: Literal["Whole Mouse Brain Delipidation - Dichloromethane"] = (
        "Whole Mouse Brain Delipidation - Dichloromethane"
    )
    authors: list[str] = [
        "Holly Myers",
        "Daphne Toglia",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.dm6gpj7n5gzp/v1"] = "10.17504/protocols.io.dm6gpj7n5gzp/v1"


class _Refractive_Index_Matching_Ethyl_Cinnamate(ProtocolModel):
    """Model Refractive Index Matching - Ethyl Cinnamate"""

    name: Literal["Refractive Index Matching - Ethyl Cinnamate"] = "Refractive Index Matching - Ethyl Cinnamate"
    authors: list[str] = [
        "Holly Myers",
        "Daphne Toglia",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.n2bvj8k4bgk5/v1"] = "10.17504/protocols.io.n2bvj8k4bgk5/v1"


class _Dapi_Staining_Mouse_Brain_Sections(ProtocolModel):
    """Model DAPI Staining Mouse Brain Sections"""

    name: Literal["DAPI Staining Mouse Brain Sections"] = "DAPI Staining Mouse Brain Sections"
    authors: list[str] = [
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.3byl4jm6rlo5/v1"] = "10.17504/protocols.io.3byl4jm6rlo5/v1"


class _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Triggering_System(ProtocolModel):
    """Model Modified Frame-projected Independent Fiber Photometry (FIP) System_Triggering system"""

    name: Literal["Modified Frame-projected Independent Fiber Photometry (FIP) System_Triggering system"] = (
        "Modified Frame-projected Independent Fiber Photometry (FIP) System_Triggering system"
    )
    authors: list[str] = [
        "Kenta M. Hagihara",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.kxygx3e6wg8j/v1"] = "10.17504/protocols.io.kxygx3e6wg8j/v1"


class _Multi_Site_Optic_Fiber_Implants(ProtocolModel):
    """Model Multi-Site Optic Fiber Implants"""

    name: Literal["Multi-Site Optic Fiber Implants"] = "Multi-Site Optic Fiber Implants"
    authors: list[str] = [
        "Avalon Amaya",
        "Kenta M. Hagihara",
        "Benjamin Ouellette",
        "Conor Grasso",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.6qpvr3dqovmk/v1"] = "10.17504/protocols.io.6qpvr3dqovmk/v1"


class _Immunohistochemistry_Ihc_Staining_Mouse_Brain_Sections(ProtocolModel):
    """Model Immunohistochemistry (IHC) Staining Mouse Brain Sections"""

    name: Literal["Immunohistochemistry (IHC) Staining Mouse Brain Sections"] = (
        "Immunohistochemistry (IHC) Staining Mouse Brain Sections"
    )
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.5qpvo3b7bv4o/v1"] = "10.17504/protocols.io.5qpvo3b7bv4o/v1"


class _Sectioning_Mouse_Brain_With_Sliding_Microtome(ProtocolModel):
    """Model Sectioning Mouse Brain with Sliding Microtome"""

    name: Literal["Sectioning Mouse Brain with Sliding Microtome"] = "Sectioning Mouse Brain with Sliding Microtome"
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.5jyl8p97rg2w/v1"] = "10.17504/protocols.io.5jyl8p97rg2w/v1"


class _Mounting_And_Coverslipping_Mouse_Brain_Sections(ProtocolModel):
    """Model Mounting and Coverslipping Mouse Brain Sections"""

    name: Literal["Mounting and Coverslipping Mouse Brain Sections"] = "Mounting and Coverslipping Mouse Brain Sections"
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.n92ldmpy7l5b/v1"] = "10.17504/protocols.io.n92ldmpy7l5b/v1"


class _Stereotactic_Injections_With_Headframe_Implant(ProtocolModel):
    """Model Stereotactic Injections with Headframe Implant"""

    name: Literal["Stereotactic Injections with Headframe Implant"] = "Stereotactic Injections with Headframe Implant"
    authors: list[str] = [
        "Avalon Amaya",
        "Katrina Nguyen",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.eq2lyj72elx9/v1"] = "10.17504/protocols.io.eq2lyj72elx9/v1"


class _Protocol_Collection_Perfusing_Sectioning_Ihc_Mounting_And_Coverslipping_Mouse_Brain_Specimens(ProtocolModel):
    """Model Protocol Collection: Perfusing, Sectioning, IHC, Mounting and Coverslipping Mouse Brain Specimens"""

    name: Literal[
        "Protocol Collection: Perfusing, Sectioning, IHC, Mounting and Coverslipping Mouse Brain Specimens"
    ] = "Protocol Collection: Perfusing, Sectioning, IHC, Mounting and Coverslipping Mouse Brain Specimens"
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Literal[Registry.DOI] = Registry.DOI
    registry_identifier: Literal["10.17504/protocols.io.kxygx3yxkg8j/v1"] = "10.17504/protocols.io.kxygx3yxkg8j/v1"


class Protocols:
    """Protocols"""

    SOLENOID_VALVE_CALIBRATION_FOR_BEHAVIOR_RIGS_UTILIZING_WATER_REWARD = (
        _Solenoid_Valve_Calibration_For_Behavior_Rigs_Utilizing_Water_Reward()
    )
    STEREOTAXIC_INJECTION_BY_NANOJECT_PROTOCOL = _Stereotaxic_Injection_By_Nanoject_Protocol()
    STEREOTAXIC_INJECTION_BY_IONTOPHORESIS = _Stereotaxic_Injection_By_Iontophoresis()
    MOUSE_HABITUATION___HEAD_FIXATION_ON_DISK = _Mouse_Habituation_Head_Fixation_On_Disk()
    MOUSE_WATER_RESTRICTION = _Mouse_Water_Restriction()
    MOUSE_HABITUATION___HEAD_FIXATION_INTO_TUBE = _Mouse_Habituation_Head_Fixation_Into_Tube()
    MODIFIED_FRAME_PROJECTED__INDEPENDENT_FIBER__PHOTOMETRY__FIP__SYSTEM_HARDWARE = (
        _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Hardware()
    )
    MAKING_AGAROSE_FOR_USE_IN_ACUTE_IN_VIVO_ELECTROPHYSIOLOGY_EXPERIMENTS_ = (
        _Making_Agarose_For_Use_In_Acute_In_Vivo_Electrophysiology_Experiments_()
    )
    PLUG_REMOVAL_FOR_ACUTE_IN_VIVO_ELECTROPHYSIOLOGY_EXPERIMENTS = (
        _Plug_Removal_For_Acute_In_Vivo_Electrophysiology_Experiments()
    )
    INTRAPERITONEAL_INJECTION_IN_AN_ADULT_MOUSE = _Intraperitoneal_Injection_In_An_Adult_Mouse()
    MULTIPLEXED_RNA_FISH_ON_EXPANDED_MOUSE_BRAIN_SLICES = _Multiplexed_Rna_Fish_On_Expanded_Mouse_Brain_Slices()
    GENERAL_SETUP_AND_TAKEDOWN_PROCEDURES_FOR_RODENT_NEUROSURGERY = (
        _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery()
    )
    DUAL_HEMISPHERE_CRANIOTOMY_FOR_ELECTROPHYSIOLOGY = _Dual_Hemisphere_Craniotomy_For_Electrophysiology()
    AQUEOUS__SBIP__DELIPIDATION_FOR_WHOLE_MOUSE_BRAIN_AFTER_MORPHOFISH_PERFUSION_ = (
        _Aqueous_Sbip_Delipidation_For_Whole_Mouse_Brain_After_Morphofish_Perfusion_()
    )
    MOUSE_HABITUATION___HEAD_FIXATION_ON_DISK = _Mouse_Habituation_Head_Fixation_On_Disk()
    PREPARATION_OF_LIPOPOLYSACCHARIDE_FOR_INTRAPERITONEAL_INJECTION = (
        _Preparation_Of_Lipopolysaccharide_For_Intraperitoneal_Injection()
    )
    TEMPORAL_ASSESSMENT_OF_IMMUNE_RESPONSE = _Temporal_Assessment_Of_Immune_Response()
    MOUSE_VAB_CATHETER_MAINTENANCE = _Mouse_Vab_Catheter_Maintenance()
    PROCESSING_BLOOD_INTENDED_FOR_OLINK_ASSAY = _Processing_Blood_Intended_For_Olink_Assay()
    BARSEQ_2_5 = _Barseq_2_5()
    AQUEOUS__SBIP__DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN = _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain()
    TETRAHYDROFURAN_AND_DICHLOROMETHANE_DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN = (
        _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain()
    )
    IMAGING_CLEARED_MOUSE_BRAINS_ON_SMARTSPIM = _Imaging_Cleared_Mouse_Brains_On_Smartspim()
    GENERAL_SETUP_AND_TAKEDOWN_PROCEDURES_FOR_RODENT_NEUROSURGERY = (
        _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery()
    )
    WHOLE_MOUSE_BRAIN_DELIPIDATION__IMMUNOLABELING__AND_EXPANSION_MICROSCOPY = (
        _Whole_Mouse_Brain_Delipidation_Immunolabeling_And_Expansion_Microscopy()
    )
    AQUEOUS__SBIP__DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN = _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain()
    TETRAHYDROFURAN_AND_DICHLOROMETHANE_DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN = (
        _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain()
    )
    IMMUNOLABELING_OF_A_WHOLE_MOUSE_BRAIN = _Immunolabeling_Of_A_Whole_Mouse_Brain()
    STRUCTURAL_MRI_USING_THE_UNIVERSITY_OF_WASHINGTON_14T_VERTICAL_BORE_BRUKER_MRI = (
        _Structural_Mri_Using_The_University_Of_Washington_14T_Vertical_Bore_Bruker_Mri()
    )
    DURAGEL_APPLICATION_FOR_ACUTE_ELECTROPHYSIOLOGY_RECORDINGS = (
        _Duragel_Application_For_Acute_Electrophysiology_Recordings()
    )
    SMARTSPIM_SETUP_AND_ALIGNMENT = _Smartspim_Setup_And_Alignment()
    REFRACTIVE_INDEX_MATCHING___EASYINDEX = _Refractive_Index_Matching_Easyindex()
    PREPARING_A_3D_PRINTED_IMPLANT_FOR_ACUTE_IN_VIVO_ELECTROPHYSIOLOGY = (
        _Preparing_A_3D_Printed_Implant_For_Acute_In_Vivo_Electrophysiology()
    )
    MOUSE_CARDIAC_PERFUSION_FIXATION_AND_BRAIN_COLLECTION = _Mouse_Cardiac_Perfusion_Fixation_And_Brain_Collection()
    WHOLE_MOUSE_BRAIN_DELIPIDATION___DICHLOROMETHANE = _Whole_Mouse_Brain_Delipidation_Dichloromethane()
    REFRACTIVE_INDEX_MATCHING___ETHYL_CINNAMATE = _Refractive_Index_Matching_Ethyl_Cinnamate()
    DAPI_STAINING_MOUSE_BRAIN_SECTIONS = _Dapi_Staining_Mouse_Brain_Sections()
    MODIFIED_FRAME_PROJECTED_INDEPENDENT_FIBER_PHOTOMETRY__FIP__SYSTEM_TRIGGERING_SYSTEM = (
        _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Triggering_System()
    )
    MULTI_SITE_OPTIC_FIBER_IMPLANTS = _Multi_Site_Optic_Fiber_Implants()
    IMMUNOHISTOCHEMISTRY__IHC__STAINING_MOUSE_BRAIN_SECTIONS = _Immunohistochemistry_Ihc_Staining_Mouse_Brain_Sections()
    SECTIONING_MOUSE_BRAIN_WITH_SLIDING_MICROTOME = _Sectioning_Mouse_Brain_With_Sliding_Microtome()
    MOUNTING_AND_COVERSLIPPING_MOUSE_BRAIN_SECTIONS = _Mounting_And_Coverslipping_Mouse_Brain_Sections()
    STEREOTACTIC_INJECTIONS_WITH_HEADFRAME_IMPLANT = _Stereotactic_Injections_With_Headframe_Implant()
    PROTOCOL_COLLECTION__PERFUSING__SECTIONING__IHC__MOUNTING_AND_COVERSLIPPING_MOUSE_BRAIN_SPECIMENS = (
        _Protocol_Collection_Perfusing_Sectioning_Ihc_Mounting_And_Coverslipping_Mouse_Brain_Specimens()
    )

    ALL = tuple(ProtocolModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(ProtocolModel.__subclasses__())], Field(discriminator="title")]
