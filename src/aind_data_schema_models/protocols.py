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


class _Solenoid_Valve_Calibration_For_Behavior_Rigs_Utilizing_Water_Reward_V1(ProtocolModel):
    """Model Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"""

    name: str = "Solenoid Valve Calibration for Behavior Rigs Utilizing Water Reward"
    authors: list[str] = [
        "Ella Hilton-VanOsdall",
        "Heston Smith",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.261gerq7dl47/v1"


class _Stereotaxic_Injection_By_Nanoject_Protocol_V6(ProtocolModel):
    """Model Stereotaxic Injection by Nanoject Protocol"""

    name: str = "Stereotaxic Injection by Nanoject Protocol"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.bp2l6nr7kgqe/v6"


class _Stereotaxic_Injection_By_Iontophoresis_V6(ProtocolModel):
    """Model Stereotaxic Injection by Iontophoresis"""

    name: str = "Stereotaxic Injection by Iontophoresis"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.14egn8ewzg5d/v6"


class _Mouse_Habituation_Head_Fixation_On_Disk_V1(ProtocolModel):
    """Model Mouse Habituation - Head Fixation on Disk"""

    name: str = "Mouse Habituation - Head Fixation on Disk"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.j8nlkojmxv5r/v1"


class _Mouse_Water_Restriction_V1(ProtocolModel):
    """Model Mouse Water Restriction"""

    name: str = "Mouse Water Restriction"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.x54v9pn34g3e/v1"


class _Mouse_Habituation_Head_Fixation_Into_Tube_V1(ProtocolModel):
    """Model Mouse Habituation - Head Fixation into Tube"""

    name: str = "Mouse Habituation - Head Fixation into Tube"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.rm7vzxd74gx1/v1"


class _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Hardware_V2(ProtocolModel):
    """Model Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"""

    name: str = "Modified Frame-projected  Independent Fiber  Photometry (FIP) System_Hardware"
    authors: list[str] = [
        "Kenta M. Hagihara",
        "Bryan J MacLennan",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.261ge39edl47/v2"


class _Making_Agarose_For_Use_In_Acute_In_Vivo_Electrophysiology_Experiments__V1(ProtocolModel):
    """Model Making Agarose for use in acute in vivo Electrophysiology Experiments"""

    name: str = "Making Agarose for use in acute in vivo Electrophysiology Experiments "
    authors: list[str] = [
        "Ryan Gillis",
        "Mikayla Carlson",
        "Severine Durand",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.5jyl8py89g2w/v1"


class _Plug_Removal_For_Acute_In_Vivo_Electrophysiology_Experiments_V1(ProtocolModel):
    """Model Plug Removal for acute in vivo Electrophysiology Experiments"""

    name: str = "Plug Removal for acute in vivo Electrophysiology Experiments"
    authors: list[str] = [
        "Ryan Gillis",
        "Mikayla Carlson",
        "Severine Durand",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.eq2lywz8qvx9/v1"


class _Intraperitoneal_Injection_In_An_Adult_Mouse_V2(ProtocolModel):
    """Model Intraperitoneal Injection in an Adult Mouse"""

    name: str = "Intraperitoneal Injection in an Adult Mouse"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.5qpvo5w8dl4o/v2"


class _Multiplexed_Rna_Fish_On_Expanded_Mouse_Brain_Slices_V1(ProtocolModel):
    """Model Multiplexed RNA FISH on Expanded Mouse Brain Slices"""

    name: str = "Multiplexed RNA FISH on Expanded Mouse Brain Slices"
    authors: list[str] = [
        "Rachel Flannery",
        "Molly Logsdon",
        "Laura Roy",
        "Kevin Cao",
        "Jayaram Chandrashekar",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.dm6gpzj28lzp/v1"


class _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery_V2(ProtocolModel):
    """Model General Setup and Takedown Procedures for Rodent Neurosurgery"""

    name: str = "General Setup and Takedown Procedures for Rodent Neurosurgery"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
        "Ali Williford",
        "Robert E Howard",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.kqdg392o7g25/v2"


class _Dual_Hemisphere_Craniotomy_For_Electrophysiology_V1(ProtocolModel):
    """Model Dual Hemisphere Craniotomy for Electrophysiology"""

    name: str = "Dual Hemisphere Craniotomy for Electrophysiology"
    authors: list[str] = [
        "Anna Lakunina",
        "Conor Grasso",
        "Benjamin Barad",
        "Avalon Amaya",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.rm7vzjoe2lx1/v1"


class _Aqueous_Sbip_Delipidation_For_Whole_Mouse_Brain_After_Morphofish_Perfusion__V1(ProtocolModel):
    """Model Aqueous (SBiP) Delipidation for Whole Mouse Brain After morphoFISH Perfusion"""

    name: str = "Aqueous (SBiP) Delipidation for Whole Mouse Brain After morphoFISH Perfusion "
    authors: list[str] = [
        "Monique Copeland",
        "MouseLight Project Team",
        "Tiago A Ferreira",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.rm7vzjz54lx1/v1"


class _Mouse_Habituation_Head_Fixation_On_Disk_V2(ProtocolModel):
    """Model Mouse Habituation - Head Fixation on Disk"""

    name: str = "Mouse Habituation - Head Fixation on Disk"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.j8nlkojmxv5r/v2"


class _Preparation_Of_Lipopolysaccharide_For_Intraperitoneal_Injection_V1(ProtocolModel):
    """Model Preparation of Lipopolysaccharide for Intraperitoneal Injection"""

    name: str = "Preparation of Lipopolysaccharide for Intraperitoneal Injection"
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.14egn9y1ml5d/v1"


class _Temporal_Assessment_Of_Immune_Response_V1(ProtocolModel):
    """Model Temporal Assessment of Immune Response"""

    name: str = "Temporal Assessment of Immune Response"
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.5jyl8dqx6g2w/v1"


class _Mouse_Vab_Catheter_Maintenance_V1(ProtocolModel):
    """Model Mouse VAB Catheter Maintenance"""

    name: str = "Mouse VAB Catheter Maintenance"
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.8epv52o5dv1b/v1"


class _Processing_Blood_Intended_For_Olink_Assay_V1(ProtocolModel):
    """Model Processing Blood Intended for Olink Assay"""

    name: str = "Processing Blood Intended for Olink Assay"
    authors: list[str] = [
        "Adrien Stanley",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.261ger81jl47/v1"


class _Barseq_2_5_V1(ProtocolModel):
    """Model BARseq 2.5"""

    name: str = "BARseq 2.5"
    authors: list[str] = [
        "Jonathan Wang",
        "Yoh Isogai",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.kqdg3ke9qv25/v1"


class _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain_V2(ProtocolModel):
    """Model Aqueous (SBiP) Delipidation of a Whole Mouse Brain"""

    name: str = "Aqueous (SBiP) Delipidation of a Whole Mouse Brain"
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Judith Baka",
        "Jayaram Chandrashekar",
        "Rajvi Javeri",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.n2bvj81mwgk5/v2"


class _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain_V2(ProtocolModel):
    """Model Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"""

    name: str = "Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Jayaram Chandrashekar",
        "Rajvi Javeri",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.36wgqj1kxvk5/v2"


class _Imaging_Cleared_Mouse_Brains_On_Smartspim_V1(ProtocolModel):
    """Model Imaging cleared mouse brains on SmartSPIM"""

    name: str = "Imaging cleared mouse brains on SmartSPIM"
    authors: list[str] = [
        "John Rohde",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.3byl4jo1rlo5/v1"


class _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery_V1(ProtocolModel):
    """Model General Setup and Takedown Procedures for Rodent Neurosurgery"""

    name: str = "General Setup and Takedown Procedures for Rodent Neurosurgery"
    authors: list[str] = [
        "Avalon Amaya",
        "Jackie Swapp",
        "Ali Williford",
        "Robert E Howard",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.kqdg392o7g25/v1"


class _Whole_Mouse_Brain_Delipidation_Immunolabeling_And_Expansion_Microscopy_V1(ProtocolModel):
    """Model Whole Mouse Brain Delipidation, Immunolabeling, and Expansion Microscopy"""

    name: str = "Whole Mouse Brain Delipidation, Immunolabeling, and Expansion Microscopy"
    authors: list[str] = [
        "Naveen Ouellette",
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Jayaram Chandrashekar",
        "Molly Logsdon",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.n92ldpwjxl5b/v1"


class _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain_V1(ProtocolModel):
    """Model Aqueous (SBiP) Delipidation of a Whole Mouse Brain"""

    name: str = "Aqueous (SBiP) Delipidation of a Whole Mouse Brain"
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Judith Baka",
        "Jayaram Chandrashekar",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.n2bvj81mwgk5/v1"


class _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain_V1(ProtocolModel):
    """Model Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"""

    name: str = "Tetrahydrofuran and Dichloromethane Delipidation of a Whole Mouse Brain"
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Naveen Ouellette",
        "Molly Logsdon",
        "Jayaram Chandrashekar",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.36wgqj1kxvk5/v1"


class _Immunolabeling_Of_A_Whole_Mouse_Brain_V1(ProtocolModel):
    """Model Immunolabeling of a Whole Mouse Brain"""

    name: str = "Immunolabeling of a Whole Mouse Brain"
    authors: list[str] = [
        "Andrew Recknagel",
        "Kevin Cao",
        "Judith Baka",
        "Naveen Ouellette",
        "Jayaram Chandrashekar",
        "Molly Logsdon",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.ewov1okwylr2/v1"


class _Structural_Mri_Using_The_University_Of_Washington_14T_Vertical_Bore_Bruker_Mri_V1(ProtocolModel):
    """Model Structural MRI Using the University of Washington 14T Vertical Bore Bruker MRI"""

    name: str = "Structural MRI Using the University of Washington 14T Vertical Bore Bruker MRI"
    authors: list[str] = [
        "Yoni Browning",
        "Galen Lynch",
        "Josh Siegle",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.3byl4j8p2lo5/v1"


class _Duragel_Application_For_Acute_Electrophysiology_Recordings_V1(ProtocolModel):
    """Model Duragel Application for Acute Electrophysiology Recordings"""

    name: str = "Duragel Application for Acute Electrophysiology Recordings"
    authors: list[str] = [
        "Anna Lakunina",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.14egn2dwqg5d/v1"


class _Smartspim_Setup_And_Alignment_V1(ProtocolModel):
    """Model SmartSPIM setup and alignment"""

    name: str = "SmartSPIM setup and alignment"
    authors: list[str] = [
        "John Rohde",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.5jyl8jyb7g2w/v1"


class _Refractive_Index_Matching_Easyindex_V1(ProtocolModel):
    """Model Refractive Index Matching - EasyIndex"""

    name: str = "Refractive Index Matching - EasyIndex"
    authors: list[str] = [
        "Holly Myers",
        "Daphne Toglia",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.kxygx965kg8j/v1"


class _Preparing_A_3D_Printed_Implant_For_Acute_In_Vivo_Electrophysiology_V1(ProtocolModel):
    """Model Preparing a 3D Printed Implant for Acute In Vivo Electrophysiology"""

    name: str = "Preparing a 3D Printed Implant for Acute In Vivo Electrophysiology"
    authors: list[str] = [
        "Xinxin Yin",
        "Anna Lakunina",
        "Josh Siegle",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.6qpvr4jmogmk/v1"


class _Mouse_Cardiac_Perfusion_Fixation_And_Brain_Collection(ProtocolModel):
    """Model Mouse Cardiac Perfusion Fixation and Brain Collection"""

    name: str = "Mouse Cardiac Perfusion Fixation and Brain Collection"
    authors: list[str] = [
        "Allen Institute for Brain Science",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.bg5vjy66"


class _Whole_Mouse_Brain_Delipidation_Dichloromethane_V1(ProtocolModel):
    """Model Whole Mouse Brain Delipidation - Dichloromethane"""

    name: str = "Whole Mouse Brain Delipidation - Dichloromethane"
    authors: list[str] = [
        "Holly Myers",
        "Daphne Toglia",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.dm6gpj7n5gzp/v1"


class _Refractive_Index_Matching_Ethyl_Cinnamate_V1(ProtocolModel):
    """Model Refractive Index Matching - Ethyl Cinnamate"""

    name: str = "Refractive Index Matching - Ethyl Cinnamate"
    authors: list[str] = [
        "Holly Myers",
        "Daphne Toglia",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.n2bvj8k4bgk5/v1"


class _Dapi_Staining_Mouse_Brain_Sections_V1(ProtocolModel):
    """Model DAPI Staining Mouse Brain Sections"""

    name: str = "DAPI Staining Mouse Brain Sections"
    authors: list[str] = [
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.3byl4jm6rlo5/v1"


class _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Triggering_System_V1(ProtocolModel):
    """Model Modified Frame-projected Independent Fiber Photometry (FIP) System_Triggering system"""

    name: str = "Modified Frame-projected Independent Fiber Photometry (FIP) System_Triggering system"
    authors: list[str] = [
        "Kenta M. Hagihara",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.kxygx3e6wg8j/v1"


class _Multi_Site_Optic_Fiber_Implants_V1(ProtocolModel):
    """Model Multi-Site Optic Fiber Implants"""

    name: str = "Multi-Site Optic Fiber Implants"
    authors: list[str] = [
        "Avalon Amaya",
        "Kenta M. Hagihara",
        "Benjamin Ouellette",
        "Conor Grasso",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.6qpvr3dqovmk/v1"


class _Immunohistochemistry_Ihc_Staining_Mouse_Brain_Sections_V1(ProtocolModel):
    """Model Immunohistochemistry (IHC) Staining Mouse Brain Sections"""

    name: str = "Immunohistochemistry (IHC) Staining Mouse Brain Sections"
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.5qpvo3b7bv4o/v1"


class _Sectioning_Mouse_Brain_With_Sliding_Microtome_V1(ProtocolModel):
    """Model Sectioning Mouse Brain with Sliding Microtome"""

    name: str = "Sectioning Mouse Brain with Sliding Microtome"
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.5jyl8p97rg2w/v1"


class _Mounting_And_Coverslipping_Mouse_Brain_Sections_V1(ProtocolModel):
    """Model Mounting and Coverslipping Mouse Brain Sections"""

    name: str = "Mounting and Coverslipping Mouse Brain Sections"
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.n92ldmpy7l5b/v1"


class _Stereotactic_Injections_With_Headframe_Implant_V1(ProtocolModel):
    """Model Stereotactic Injections with Headframe Implant"""

    name: str = "Stereotactic Injections with Headframe Implant"
    authors: list[str] = [
        "Avalon Amaya",
        "Katrina Nguyen",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.eq2lyj72elx9/v1"


class _Protocol_Collection_Perfusing_Sectioning_Ihc_Mounting_And_Coverslipping_Mouse_Brain_Specimens_V1(ProtocolModel):
    """Model Protocol Collection: Perfusing, Sectioning, IHC, Mounting and Coverslipping Mouse Brain Specimens"""

    name: str = "Protocol Collection: Perfusing, Sectioning, IHC, Mounting and Coverslipping Mouse Brain Specimens"
    authors: list[str] = [
        "Naveen Ouellette",
        "Daphne Toglia",
        "Holly Myers",
    ]
    registry: Registry = Registry.DOI
    registry_identifier: str = "10.17504/protocols.io.kxygx3yxkg8j/v1"


class Protocols:
    """Protocols"""

    SOLENOID_VALVE_CALIBRATION_FOR_BEHAVIOR_RIGS_UTILIZING_WATER_REWARD_V1 = (
        _Solenoid_Valve_Calibration_For_Behavior_Rigs_Utilizing_Water_Reward_V1()
    )

    STEREOTAXIC_INJECTION_BY_NANOJECT_PROTOCOL_V6 = _Stereotaxic_Injection_By_Nanoject_Protocol_V6()

    STEREOTAXIC_INJECTION_BY_IONTOPHORESIS_V6 = _Stereotaxic_Injection_By_Iontophoresis_V6()

    MOUSE_HABITUATION___HEAD_FIXATION_ON_DISK_V1 = _Mouse_Habituation_Head_Fixation_On_Disk_V1()

    MOUSE_WATER_RESTRICTION_V1 = _Mouse_Water_Restriction_V1()

    MOUSE_HABITUATION___HEAD_FIXATION_INTO_TUBE_V1 = _Mouse_Habituation_Head_Fixation_Into_Tube_V1()

    MODIFIED_FRAME_PROJECTED__INDEPENDENT_FIBER__PHOTOMETRY__FIP__SYSTEM_HARDWARE_V2 = (
        _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Hardware_V2()
    )

    MAKING_AGAROSE_FOR_USE_IN_ACUTE_IN_VIVO_ELECTROPHYSIOLOGY_EXPERIMENTS__V1 = (
        _Making_Agarose_For_Use_In_Acute_In_Vivo_Electrophysiology_Experiments__V1()
    )

    PLUG_REMOVAL_FOR_ACUTE_IN_VIVO_ELECTROPHYSIOLOGY_EXPERIMENTS_V1 = (
        _Plug_Removal_For_Acute_In_Vivo_Electrophysiology_Experiments_V1()
    )

    INTRAPERITONEAL_INJECTION_IN_AN_ADULT_MOUSE_V2 = _Intraperitoneal_Injection_In_An_Adult_Mouse_V2()

    MULTIPLEXED_RNA_FISH_ON_EXPANDED_MOUSE_BRAIN_SLICES_V1 = _Multiplexed_Rna_Fish_On_Expanded_Mouse_Brain_Slices_V1()

    GENERAL_SETUP_AND_TAKEDOWN_PROCEDURES_FOR_RODENT_NEUROSURGERY_V2 = (
        _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery_V2()
    )

    DUAL_HEMISPHERE_CRANIOTOMY_FOR_ELECTROPHYSIOLOGY_V1 = _Dual_Hemisphere_Craniotomy_For_Electrophysiology_V1()

    AQUEOUS__SBIP__DELIPIDATION_FOR_WHOLE_MOUSE_BRAIN_AFTER_MORPHOFISH_PERFUSION__V1 = (
        _Aqueous_Sbip_Delipidation_For_Whole_Mouse_Brain_After_Morphofish_Perfusion__V1()
    )

    MOUSE_HABITUATION___HEAD_FIXATION_ON_DISK_V2 = _Mouse_Habituation_Head_Fixation_On_Disk_V2()

    PREPARATION_OF_LIPOPOLYSACCHARIDE_FOR_INTRAPERITONEAL_INJECTION_V1 = (
        _Preparation_Of_Lipopolysaccharide_For_Intraperitoneal_Injection_V1()
    )

    TEMPORAL_ASSESSMENT_OF_IMMUNE_RESPONSE_V1 = _Temporal_Assessment_Of_Immune_Response_V1()

    MOUSE_VAB_CATHETER_MAINTENANCE_V1 = _Mouse_Vab_Catheter_Maintenance_V1()

    PROCESSING_BLOOD_INTENDED_FOR_OLINK_ASSAY_V1 = _Processing_Blood_Intended_For_Olink_Assay_V1()

    BARSEQ_2_5_V1 = _Barseq_2_5_V1()

    AQUEOUS__SBIP__DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN_V2 = _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain_V2()

    TETRAHYDROFURAN_AND_DICHLOROMETHANE_DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN_V2 = (
        _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain_V2()
    )

    IMAGING_CLEARED_MOUSE_BRAINS_ON_SMARTSPIM_V1 = _Imaging_Cleared_Mouse_Brains_On_Smartspim_V1()

    GENERAL_SETUP_AND_TAKEDOWN_PROCEDURES_FOR_RODENT_NEUROSURGERY_V1 = (
        _General_Setup_And_Takedown_Procedures_For_Rodent_Neurosurgery_V1()
    )

    WHOLE_MOUSE_BRAIN_DELIPIDATION__IMMUNOLABELING__AND_EXPANSION_MICROSCOPY_V1 = (
        _Whole_Mouse_Brain_Delipidation_Immunolabeling_And_Expansion_Microscopy_V1()
    )

    AQUEOUS__SBIP__DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN_V1 = _Aqueous_Sbip_Delipidation_Of_A_Whole_Mouse_Brain_V1()

    TETRAHYDROFURAN_AND_DICHLOROMETHANE_DELIPIDATION_OF_A_WHOLE_MOUSE_BRAIN_V1 = (
        _Tetrahydrofuran_And_Dichloromethane_Delipidation_Of_A_Whole_Mouse_Brain_V1()
    )

    IMMUNOLABELING_OF_A_WHOLE_MOUSE_BRAIN_V1 = _Immunolabeling_Of_A_Whole_Mouse_Brain_V1()

    STRUCTURAL_MRI_USING_THE_UNIVERSITY_OF_WASHINGTON_14T_VERTICAL_BORE_BRUKER_MRI_V1 = (
        _Structural_Mri_Using_The_University_Of_Washington_14T_Vertical_Bore_Bruker_Mri_V1()
    )

    DURAGEL_APPLICATION_FOR_ACUTE_ELECTROPHYSIOLOGY_RECORDINGS_V1 = (
        _Duragel_Application_For_Acute_Electrophysiology_Recordings_V1()
    )

    SMARTSPIM_SETUP_AND_ALIGNMENT_V1 = _Smartspim_Setup_And_Alignment_V1()

    REFRACTIVE_INDEX_MATCHING___EASYINDEX_V1 = _Refractive_Index_Matching_Easyindex_V1()

    PREPARING_A_3D_PRINTED_IMPLANT_FOR_ACUTE_IN_VIVO_ELECTROPHYSIOLOGY_V1 = (
        _Preparing_A_3D_Printed_Implant_For_Acute_In_Vivo_Electrophysiology_V1()
    )

    MOUSE_CARDIAC_PERFUSION_FIXATION_AND_BRAIN_COLLECTION = _Mouse_Cardiac_Perfusion_Fixation_And_Brain_Collection()

    WHOLE_MOUSE_BRAIN_DELIPIDATION___DICHLOROMETHANE_V1 = _Whole_Mouse_Brain_Delipidation_Dichloromethane_V1()

    REFRACTIVE_INDEX_MATCHING___ETHYL_CINNAMATE_V1 = _Refractive_Index_Matching_Ethyl_Cinnamate_V1()

    DAPI_STAINING_MOUSE_BRAIN_SECTIONS_V1 = _Dapi_Staining_Mouse_Brain_Sections_V1()

    MODIFIED_FRAME_PROJECTED_INDEPENDENT_FIBER_PHOTOMETRY__FIP__SYSTEM_TRIGGERING_SYSTEM_V1 = (
        _Modified_Frame_Projected_Independent_Fiber_Photometry_Fip_System_Triggering_System_V1()
    )

    MULTI_SITE_OPTIC_FIBER_IMPLANTS_V1 = _Multi_Site_Optic_Fiber_Implants_V1()

    IMMUNOHISTOCHEMISTRY__IHC__STAINING_MOUSE_BRAIN_SECTIONS_V1 = (
        _Immunohistochemistry_Ihc_Staining_Mouse_Brain_Sections_V1()
    )

    SECTIONING_MOUSE_BRAIN_WITH_SLIDING_MICROTOME_V1 = _Sectioning_Mouse_Brain_With_Sliding_Microtome_V1()

    MOUNTING_AND_COVERSLIPPING_MOUSE_BRAIN_SECTIONS_V1 = _Mounting_And_Coverslipping_Mouse_Brain_Sections_V1()

    STEREOTACTIC_INJECTIONS_WITH_HEADFRAME_IMPLANT_V1 = _Stereotactic_Injections_With_Headframe_Implant_V1()

    PROTOCOL_COLLECTION__PERFUSING__SECTIONING__IHC__MOUNTING_AND_COVERSLIPPING_MOUSE_BRAIN_SPECIMENS_V1 = (
        _Protocol_Collection_Perfusing_Sectioning_Ihc_Mounting_And_Coverslipping_Mouse_Brain_Specimens_V1()
    )

    ALL = tuple(ProtocolModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(ProtocolModel.__subclasses__())], Field(discriminator="title")]

    doi_map = {m().registry_identifier: m() for m in ALL if getattr(m(), "registry_identifier", None)}

    @classmethod
    def from_doi(cls, doi: str) -> ProtocolModel:
        """Return protocol model by DOI."""
        return cls.doi_map.get(doi, None)

    @classmethod
    def from_url(cls, url: str) -> ProtocolModel:
        """Return protocol model by DOI, stripping URL prefixes."""
        prefixes = [
            "https://dx.doi.org/",
            "dx.doi.org/",
            "https://doi.org/",
            "doi.org/",
            "http://dx.doi.org/",
            "http://doi.org/",
        ]
        doi = url
        for prefix in prefixes:
            if doi.startswith(prefix):
                doi = doi[len(prefix) :]
        return cls.from_doi(doi)
