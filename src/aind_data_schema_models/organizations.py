"""Organizations"""

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from aind_data_schema_models.registries import Registry
from aind_data_schema_models.utils import one_of_instance


class _OrganizationModel(BaseModel):
    """Base model for organizations"""

    model_config = ConfigDict(frozen=True)
    name: str
    abbreviation: str
    registry: Registry.ONE_OF
    registry_identifier: str


class _Aa_Opto_Electronic(_OrganizationModel):
    """Model AA Opto Electronic"""

    name: Literal["AA Opto Electronic"] = "AA Opto Electronic"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Asus(_OrganizationModel):
    """Model ASUS"""

    name: Literal["ASUS"] = "ASUS"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00bxkz165"] = "00bxkz165"


class _Abcam(_OrganizationModel):
    """Model Abcam"""

    name: Literal["Abcam"] = "Abcam"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02e1wjw63"] = "02e1wjw63"


class _Addgene(_OrganizationModel):
    """Model Addgene"""

    name: Literal["Addgene"] = "Addgene"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01nn1pw54"] = "01nn1pw54"


class _Ailipu_Technology_Co(_OrganizationModel):
    """Model Ailipu Technology Co"""

    name: Literal["Ailipu Technology Co"] = "Ailipu Technology Co"
    abbreviation: Literal["Ailipu"] = "Ailipu"
    registry: None = None
    registry_identifier: None = None


class _Aligning_Science_Across_Parkinson_S(_OrganizationModel):
    """Model Aligning Science Across Parkinson's"""

    name: Literal["Aligning Science Across Parkinson's"] = "Aligning Science Across Parkinson's"
    abbreviation: Literal["ASAP"] = "ASAP"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03zj4c476"] = "03zj4c476"


class _Allen_Institute(_OrganizationModel):
    """Model Allen Institute"""

    name: Literal["Allen Institute"] = "Allen Institute"
    abbreviation: Literal["AI"] = "AI"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03cpe7c52"] = "03cpe7c52"


class _Allen_Institute_For_Brain_Science(_OrganizationModel):
    """Model Allen Institute for Brain Science"""

    name: Literal["Allen Institute for Brain Science"] = "Allen Institute for Brain Science"
    abbreviation: Literal["AIBS"] = "AIBS"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00dcv1019"] = "00dcv1019"


class _Allen_Institute_For_Neural_Dynamics(_OrganizationModel):
    """Model Allen Institute for Neural Dynamics"""

    name: Literal["Allen Institute for Neural Dynamics"] = "Allen Institute for Neural Dynamics"
    abbreviation: Literal["AIND"] = "AIND"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["04szwah67"] = "04szwah67"


class _Allied(_OrganizationModel):
    """Model Allied"""

    name: Literal["Allied"] = "Allied"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Antibodies_Inc(_OrganizationModel):
    """Model Antibodies Inc"""

    name: Literal["Antibodies Inc"] = "Antibodies Inc"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Applied_Scientific_Instrumentation(_OrganizationModel):
    """Model Applied Scientific Instrumentation"""

    name: Literal["Applied Scientific Instrumentation"] = "Applied Scientific Instrumentation"
    abbreviation: Literal["ASI"] = "ASI"
    registry: None = None
    registry_identifier: None = None


class _Arecont_Vision_Costar(_OrganizationModel):
    """Model Arecont Vision Costar"""

    name: Literal["Arecont Vision Costar"] = "Arecont Vision Costar"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Basler(_OrganizationModel):
    """Model Basler"""

    name: Literal["Basler"] = "Basler"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Cambridge_Technology(_OrganizationModel):
    """Model Cambridge Technology"""

    name: Literal["Cambridge Technology"] = "Cambridge Technology"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Carl_Zeiss(_OrganizationModel):
    """Model Carl Zeiss"""

    name: Literal["Carl Zeiss"] = "Carl Zeiss"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01xk5xs43"] = "01xk5xs43"


class _Champalimaud_Foundation(_OrganizationModel):
    """Model Champalimaud Foundation"""

    name: Literal["Champalimaud Foundation"] = "Champalimaud Foundation"
    abbreviation: Literal["Champalimaud"] = "Champalimaud"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03g001n57"] = "03g001n57"


class _Chan_Zuckerberg_Initiative(_OrganizationModel):
    """Model Chan Zuckerberg Initiative"""

    name: Literal["Chan Zuckerberg Initiative"] = "Chan Zuckerberg Initiative"
    abbreviation: Literal["CZI"] = "CZI"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02qenvm24"] = "02qenvm24"


class _Charles_River_Laboratories(_OrganizationModel):
    """Model Charles River Laboratories"""

    name: Literal["Charles River Laboratories"] = "Charles River Laboratories"
    abbreviation: Literal["CRL"] = "CRL"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03ndmsg87"] = "03ndmsg87"


class _Chroma(_OrganizationModel):
    """Model Chroma"""

    name: Literal["Chroma"] = "Chroma"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Coherent_Scientific(_OrganizationModel):
    """Model Coherent Scientific"""

    name: Literal["Coherent Scientific"] = "Coherent Scientific"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["031tysd23"] = "031tysd23"


class _Columbia_University(_OrganizationModel):
    """Model Columbia University"""

    name: Literal["Columbia University"] = "Columbia University"
    abbreviation: Literal["Columbia"] = "Columbia"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00hj8s172"] = "00hj8s172"


class _Computar(_OrganizationModel):
    """Model Computar"""

    name: Literal["Computar"] = "Computar"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Conoptics(_OrganizationModel):
    """Model Conoptics"""

    name: Literal["Conoptics"] = "Conoptics"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Custom(_OrganizationModel):
    """Model Custom"""

    name: Literal["Custom"] = "Custom"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Digikey(_OrganizationModel):
    """Model DigiKey"""

    name: Literal["DigiKey"] = "DigiKey"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Dodotronic(_OrganizationModel):
    """Model Dodotronic"""

    name: Literal["Dodotronic"] = "Dodotronic"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Doric(_OrganizationModel):
    """Model Doric"""

    name: Literal["Doric"] = "Doric"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["059n53q30"] = "059n53q30"


class _Ealing(_OrganizationModel):
    """Model Ealing"""

    name: Literal["Ealing"] = "Ealing"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Edmund_Optics(_OrganizationModel):
    """Model Edmund Optics"""

    name: Literal["Edmund Optics"] = "Edmund Optics"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01j1gwp17"] = "01j1gwp17"


class _Emory_University(_OrganizationModel):
    """Model Emory University"""

    name: Literal["Emory University"] = "Emory University"
    abbreviation: Literal["Emory"] = "Emory"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03czfpz43"] = "03czfpz43"


class _Esther_A_Joseph_Klingenstein_Fund(_OrganizationModel):
    """Model Esther A. & Joseph Klingenstein Fund"""

    name: Literal["Esther A. & Joseph Klingenstein Fund"] = "Esther A. & Joseph Klingenstein Fund"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01q222b25"] = "01q222b25"


class _Euresys(_OrganizationModel):
    """Model Euresys"""

    name: Literal["Euresys"] = "Euresys"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Fujinon(_OrganizationModel):
    """Model Fujinon"""

    name: Literal["Fujinon"] = "Fujinon"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _G_Harold_Leila_Y_Mathers_Foundation(_OrganizationModel):
    """Model G. Harold & Leila Y. Mathers Foundation"""

    name: Literal["G. Harold & Leila Y. Mathers Foundation"] = "G. Harold & Leila Y. Mathers Foundation"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02a7hjv13"] = "02a7hjv13"


class _Hamamatsu(_OrganizationModel):
    """Model Hamamatsu"""

    name: Literal["Hamamatsu"] = "Hamamatsu"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03natb733"] = "03natb733"


class _Hamilton(_OrganizationModel):
    """Model Hamilton"""

    name: Literal["Hamilton"] = "Hamilton"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Helen_Hay_Whitney_Foundation(_OrganizationModel):
    """Model Helen Hay Whitney Foundation"""

    name: Literal["Helen Hay Whitney Foundation"] = "Helen Hay Whitney Foundation"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["037ebw447"] = "037ebw447"


class _Huazhong_University_Of_Science_And_Technology(_OrganizationModel):
    """Model Huazhong University of Science and Technology"""

    name: Literal["Huazhong University of Science and Technology"] = "Huazhong University of Science and Technology"
    abbreviation: Literal["HUST"] = "HUST"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00p991c53"] = "00p991c53"


class _Ir_Robot_Co(_OrganizationModel):
    """Model IR Robot Co"""

    name: Literal["IR Robot Co"] = "IR Robot Co"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Isl_Products_International(_OrganizationModel):
    """Model ISL Products International"""

    name: Literal["ISL Products International"] = "ISL Products International"
    abbreviation: Literal["ISL"] = "ISL"
    registry: None = None
    registry_identifier: None = None


class _Infinity_Photo_Optical(_OrganizationModel):
    """Model Infinity Photo-Optical"""

    name: Literal["Infinity Photo-Optical"] = "Infinity Photo-Optical"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Integrated_Dna_Technologies(_OrganizationModel):
    """Model Integrated DNA Technologies"""

    name: Literal["Integrated DNA Technologies"] = "Integrated DNA Technologies"
    abbreviation: Literal["IDT"] = "IDT"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["009jvpf03"] = "009jvpf03"


class _Interuniversity_Microelectronics_Center(_OrganizationModel):
    """Model Interuniversity Microelectronics Center"""

    name: Literal["Interuniversity Microelectronics Center"] = "Interuniversity Microelectronics Center"
    abbreviation: Literal["IMEC"] = "IMEC"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02kcbn207"] = "02kcbn207"


class _Invitrogen(_OrganizationModel):
    """Model Invitrogen"""

    name: Literal["Invitrogen"] = "Invitrogen"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03x1ewr52"] = "03x1ewr52"


class _Item(_OrganizationModel):
    """Model Item"""

    name: Literal["Item"] = "Item"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Jackson_Laboratory(_OrganizationModel):
    """Model Jackson Laboratory"""

    name: Literal["Jackson Laboratory"] = "Jackson Laboratory"
    abbreviation: Literal["JAX"] = "JAX"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["021sy4w91"] = "021sy4w91"


class _Janelia_Research_Campus(_OrganizationModel):
    """Model Janelia Research Campus"""

    name: Literal["Janelia Research Campus"] = "Janelia Research Campus"
    abbreviation: Literal["Janelia"] = "Janelia"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["013sk6x84"] = "013sk6x84"


class _Julabo(_OrganizationModel):
    """Model Julabo"""

    name: Literal["Julabo"] = "Julabo"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Klingenstein_Third_Generation_Foundation(_OrganizationModel):
    """Model Klingenstein Third Generation Foundation"""

    name: Literal["Klingenstein Third Generation Foundation"] = "Klingenstein Third Generation Foundation"
    abbreviation: Literal["KTGF"] = "KTGF"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00cxc2y95"] = "00cxc2y95"


class _Kowa(_OrganizationModel):
    """Model Kowa"""

    name: Literal["Kowa"] = "Kowa"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03zbwg482"] = "03zbwg482"


class _Lg(_OrganizationModel):
    """Model LG"""

    name: Literal["LG"] = "LG"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02b948n83"] = "02b948n83"


class _Leica(_OrganizationModel):
    """Model Leica"""

    name: Literal["Leica"] = "Leica"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Lumen_Dynamics(_OrganizationModel):
    """Model Lumen Dynamics"""

    name: Literal["Lumen Dynamics"] = "Lumen Dynamics"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Lifecanvas(_OrganizationModel):
    """Model LifeCanvas"""

    name: Literal["LifeCanvas"] = "LifeCanvas"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Life_Sciences_Research_Foundation(_OrganizationModel):
    """Model Life Sciences Research Foundation"""

    name: Literal["Life Sciences Research Foundation"] = "Life Sciences Research Foundation"
    abbreviation: Literal["LSRF"] = "LSRF"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["0195dxj21"] = "0195dxj21"


class _Mbf_Bioscience(_OrganizationModel):
    """Model MBF Bioscience"""

    name: Literal["MBF Bioscience"] = "MBF Bioscience"
    abbreviation: Literal["MBF"] = "MBF"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02zynam48"] = "02zynam48"


class _Mcknight_Brain_Research_Foundation(_OrganizationModel):
    """Model McKnight Brain Research Foundation"""

    name: Literal["McKnight Brain Research Foundation"] = "McKnight Brain Research Foundation"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00vsf1v04"] = "00vsf1v04"


class _Mcknight_Foundation(_OrganizationModel):
    """Model McKnight Foundation"""

    name: Literal["McKnight Foundation"] = "McKnight Foundation"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["003ghvj67"] = "003ghvj67"


class _Mks_Newport(_OrganizationModel):
    """Model MKS Newport"""

    name: Literal["MKS Newport"] = "MKS Newport"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00k17f049"] = "00k17f049"


class _Mpi(_OrganizationModel):
    """Model MPI"""

    name: Literal["MPI"] = "MPI"
    abbreviation: Literal["MPI"] = "MPI"
    registry: None = None
    registry_identifier: None = None


class _Meadowlark_Optics(_OrganizationModel):
    """Model Meadowlark Optics"""

    name: Literal["Meadowlark Optics"] = "Meadowlark Optics"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00n8qbq54"] = "00n8qbq54"


class _Michael_J_Fox_Foundation_For_Parkinson_S_Research(_OrganizationModel):
    """Model Michael J. Fox Foundation for Parkinson's Research"""

    name: Literal["Michael J. Fox Foundation for Parkinson's Research"] = (
        "Michael J. Fox Foundation for Parkinson's Research"
    )
    abbreviation: Literal["MJFF"] = "MJFF"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03arq3225"] = "03arq3225"


class _Midwest_Optical_Systems_Inc_(_OrganizationModel):
    """Model Midwest Optical Systems, Inc."""

    name: Literal["Midwest Optical Systems, Inc."] = "Midwest Optical Systems, Inc."
    abbreviation: Literal["MidOpt"] = "MidOpt"
    registry: None = None
    registry_identifier: None = None


class _Mitutuyo(_OrganizationModel):
    """Model Mitutuyo"""

    name: Literal["Mitutuyo"] = "Mitutuyo"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Nresearch_Inc(_OrganizationModel):
    """Model NResearch Inc"""

    name: Literal["NResearch Inc"] = "NResearch Inc"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _National_Center_For_Complementary_And_Integrative_Health(_OrganizationModel):
    """Model National Center for Complementary and Integrative Health"""

    name: Literal["National Center for Complementary and Integrative Health"] = (
        "National Center for Complementary and Integrative Health"
    )
    abbreviation: Literal["NCCIH"] = "NCCIH"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00190t495"] = "00190t495"


class _National_Institute_Of_Mental_Health(_OrganizationModel):
    """Model National Institute of Mental Health"""

    name: Literal["National Institute of Mental Health"] = "National Institute of Mental Health"
    abbreviation: Literal["NIMH"] = "NIMH"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["04xeg9z08"] = "04xeg9z08"


class _National_Institute_Of_Neurological_Disorders_And_Stroke(_OrganizationModel):
    """Model National Institute of Neurological Disorders and Stroke"""

    name: Literal["National Institute of Neurological Disorders and Stroke"] = (
        "National Institute of Neurological Disorders and Stroke"
    )
    abbreviation: Literal["NINDS"] = "NINDS"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01s5ya894"] = "01s5ya894"


class _National_Institute_On_Aging(_OrganizationModel):
    """Model National Institute on Aging"""

    name: Literal["National Institute on Aging"] = "National Institute on Aging"
    abbreviation: Literal["NIA"] = "NIA"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["049v75w11"] = "049v75w11"


class _National_Instruments(_OrganizationModel):
    """Model National Instruments"""

    name: Literal["National Instruments"] = "National Instruments"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["026exqw73"] = "026exqw73"


class _U_S_National_Science_Foundation(_OrganizationModel):
    """Model U.S. National Science Foundation"""

    name: Literal["U.S. National Science Foundation"] = "U.S. National Science Foundation"
    abbreviation: Literal["NSF"] = "NSF"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["021nxhr62"] = "021nxhr62"


class _Navitar(_OrganizationModel):
    """Model Navitar"""

    name: Literal["Navitar"] = "Navitar"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Neurophotometrics(_OrganizationModel):
    """Model Neurophotometrics"""

    name: Literal["Neurophotometrics"] = "Neurophotometrics"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _New_Scale_Technologies(_OrganizationModel):
    """Model New Scale Technologies"""

    name: Literal["New Scale Technologies"] = "New Scale Technologies"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _New_York_University(_OrganizationModel):
    """Model New York University"""

    name: Literal["New York University"] = "New York University"
    abbreviation: Literal["NYU"] = "NYU"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["0190ak572"] = "0190ak572"


class _Nikon(_OrganizationModel):
    """Model Nikon"""

    name: Literal["Nikon"] = "Nikon"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["0280y9h11"] = "0280y9h11"


class _Olympus(_OrganizationModel):
    """Model Olympus"""

    name: Literal["Olympus"] = "Olympus"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02vcdte90"] = "02vcdte90"


class _Open_Ephys_Production_Site(_OrganizationModel):
    """Model Open Ephys Production Site"""

    name: Literal["Open Ephys Production Site"] = "Open Ephys Production Site"
    abbreviation: Literal["OEPS"] = "OEPS"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["007rkz355"] = "007rkz355"


class _Optotune(_OrganizationModel):
    """Model Optotune"""

    name: Literal["Optotune"] = "Optotune"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Other(_OrganizationModel):
    """Model Other"""

    name: Literal["Other"] = "Other"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Oxxius(_OrganizationModel):
    """Model Oxxius"""

    name: Literal["Oxxius"] = "Oxxius"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Pew_Charitable_Trusts(_OrganizationModel):
    """Model Pew Charitable Trusts"""

    name: Literal["Pew Charitable Trusts"] = "Pew Charitable Trusts"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02xhk2825"] = "02xhk2825"


class _Placid_Industries(_OrganizationModel):
    """Model Placid Industries"""

    name: Literal["Placid Industries"] = "Placid Industries"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Prizmatix(_OrganizationModel):
    """Model Prizmatix"""

    name: Literal["Prizmatix"] = "Prizmatix"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Quantifi(_OrganizationModel):
    """Model Quantifi"""

    name: Literal["Quantifi"] = "Quantifi"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Raspberry_Pi(_OrganizationModel):
    """Model Raspberry Pi"""

    name: Literal["Raspberry Pi"] = "Raspberry Pi"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Rockland_Immunochemicals(_OrganizationModel):
    """Model Rockland Immunochemicals"""

    name: Literal["Rockland Immunochemicals"] = "Rockland Immunochemicals"
    abbreviation: Literal["ROCKLAND"] = "ROCKLAND"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["02z2r2t61"] = "02z2r2t61"


class _Same_Sky(_OrganizationModel):
    """Model Same Sky"""

    name: Literal["Same Sky"] = "Same Sky"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Sicgen(_OrganizationModel):
    """Model SICGEN"""

    name: Literal["SICGEN"] = "SICGEN"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Schneider_Kreuznach(_OrganizationModel):
    """Model Schneider-Kreuznach"""

    name: Literal["Schneider-Kreuznach"] = "Schneider-Kreuznach"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Second_Order_Effects(_OrganizationModel):
    """Model Second Order Effects"""

    name: Literal["Second Order Effects"] = "Second Order Effects"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Semrock(_OrganizationModel):
    """Model Semrock"""

    name: Literal["Semrock"] = "Semrock"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Sigma_Aldrich(_OrganizationModel):
    """Model Sigma-Aldrich"""

    name: Literal["Sigma-Aldrich"] = "Sigma-Aldrich"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Simons_Foundation(_OrganizationModel):
    """Model Simons Foundation"""

    name: Literal["Simons Foundation"] = "Simons Foundation"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01cmst727"] = "01cmst727"


class _Spinnaker(_OrganizationModel):
    """Model Spinnaker"""

    name: Literal["Spinnaker"] = "Spinnaker"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Synaptic_Systems(_OrganizationModel):
    """Model Synaptic Systems"""

    name: Literal["Synaptic Systems"] = "Synaptic Systems"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Tamron(_OrganizationModel):
    """Model Tamron"""

    name: Literal["Tamron"] = "Tamron"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Technical_Manufacturing_Corporation(_OrganizationModel):
    """Model Technical Manufacturing Corporation"""

    name: Literal["Technical Manufacturing Corporation"] = "Technical Manufacturing Corporation"
    abbreviation: Literal["TMC"] = "TMC"
    registry: None = None
    registry_identifier: None = None


class _Teledyne_Flir(_OrganizationModel):
    """Model Teledyne FLIR"""

    name: Literal["Teledyne FLIR"] = "Teledyne FLIR"
    abbreviation: Literal["FLIR"] = "FLIR"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01j1gwp17"] = "01j1gwp17"


class _Templeton_World_Charity_Foundation(_OrganizationModel):
    """Model Templeton World Charity Foundation"""

    name: Literal["Templeton World Charity Foundation"] = "Templeton World Charity Foundation"
    abbreviation: Literal["TWCF"] = "TWCF"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["00x0z1472"] = "00x0z1472"


class _The_Imaging_Source(_OrganizationModel):
    """Model The Imaging Source"""

    name: Literal["The Imaging Source"] = "The Imaging Source"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _The_Lee_Company(_OrganizationModel):
    """Model The Lee Company"""

    name: Literal["The Lee Company"] = "The Lee Company"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Thermo_Fisher_Scientific(_OrganizationModel):
    """Model Thermo Fisher Scientific"""

    name: Literal["Thermo Fisher Scientific"] = "Thermo Fisher Scientific"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["03x1ewr52"] = "03x1ewr52"


class _Thorlabs(_OrganizationModel):
    """Model Thorlabs"""

    name: Literal["Thorlabs"] = "Thorlabs"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["04gsnvb07"] = "04gsnvb07"


class _Transducer_Techniques(_OrganizationModel):
    """Model Transducer Techniques"""

    name: Literal["Transducer Techniques"] = "Transducer Techniques"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Tymphany(_OrganizationModel):
    """Model Tymphany"""

    name: Literal["Tymphany"] = "Tymphany"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _United_States_Department_Of_Defense(_OrganizationModel):
    """Model United States Department of Defense"""

    name: Literal["United States Department of Defense"] = "United States Department of Defense"
    abbreviation: Literal["DOD"] = "DOD"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["0447fe631"] = "0447fe631"


class _United_States_Department_Of_Energy(_OrganizationModel):
    """Model United States Department of Energy"""

    name: Literal["United States Department of Energy"] = "United States Department of Energy"
    abbreviation: Literal["DOE"] = "DOE"
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["01bj3aw27"] = "01bj3aw27"


class _Vieworks(_OrganizationModel):
    """Model Vieworks"""

    name: Literal["Vieworks"] = "Vieworks"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _Vortran(_OrganizationModel):
    """Model Vortran"""

    name: Literal["Vortran"] = "Vortran"
    abbreviation: Literal[None] = None
    registry: None = None
    registry_identifier: None = None


class _W_M_Keck_Foundation(_OrganizationModel):
    """Model W. M. Keck Foundation"""

    name: Literal["W. M. Keck Foundation"] = "W. M. Keck Foundation"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["000dswa46"] = "000dswa46"


class _Warren_Alpert_Foundation(_OrganizationModel):
    """Model Warren Alpert Foundation"""

    name: Literal["Warren Alpert Foundation"] = "Warren Alpert Foundation"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["041ztcd61"] = "041ztcd61"


class _Ams_Osram(_OrganizationModel):
    """Model ams OSRAM"""

    name: Literal["ams OSRAM"] = "ams OSRAM"
    abbreviation: Literal[None] = None
    registry: Registry.ONE_OF = Registry.ROR
    registry_identifier: Literal["045d0h266"] = "045d0h266"


class Organization:
    """Organization"""

    AA_OPTO_ELECTRONIC = _Aa_Opto_Electronic()
    ASUS = _Asus()
    ABCAM = _Abcam()
    ADDGENE = _Addgene()
    AILIPU = _Ailipu_Technology_Co()
    ASAP = _Aligning_Science_Across_Parkinson_S()
    AI = _Allen_Institute()
    AIBS = _Allen_Institute_For_Brain_Science()
    AIND = _Allen_Institute_For_Neural_Dynamics()
    ALLIED = _Allied()
    ANTIBODIES_INC = _Antibodies_Inc()
    ASI = _Applied_Scientific_Instrumentation()
    ARECONT_VISION_COSTAR = _Arecont_Vision_Costar()
    BASLER = _Basler()
    CAMBRIDGE_TECHNOLOGY = _Cambridge_Technology()
    CARL_ZEISS = _Carl_Zeiss()
    CHAMPALIMAUD = _Champalimaud_Foundation()
    CZI = _Chan_Zuckerberg_Initiative()
    CRL = _Charles_River_Laboratories()
    CHROMA = _Chroma()
    COHERENT_SCIENTIFIC = _Coherent_Scientific()
    COLUMBIA = _Columbia_University()
    COMPUTAR = _Computar()
    CONOPTICS = _Conoptics()
    CUSTOM = _Custom()
    DIGIKEY = _Digikey()
    DODOTRONIC = _Dodotronic()
    DORIC = _Doric()
    EALING = _Ealing()
    EDMUND_OPTICS = _Edmund_Optics()
    EMORY = _Emory_University()
    ESTHER_A____JOSEPH_KLINGENSTEIN_FUND = _Esther_A_Joseph_Klingenstein_Fund()
    EURESYS = _Euresys()
    FUJINON = _Fujinon()
    G__HAROLD___LEILA_Y__MATHERS_FOUNDATION = _G_Harold_Leila_Y_Mathers_Foundation()
    HAMAMATSU = _Hamamatsu()
    HAMILTON = _Hamilton()
    HELEN_HAY_WHITNEY_FOUNDATION = _Helen_Hay_Whitney_Foundation()
    HUST = _Huazhong_University_Of_Science_And_Technology()
    IR_ROBOT_CO = _Ir_Robot_Co()
    ISL = _Isl_Products_International()
    INFINITY_PHOTO_OPTICAL = _Infinity_Photo_Optical()
    IDT = _Integrated_Dna_Technologies()
    IMEC = _Interuniversity_Microelectronics_Center()
    INVITROGEN = _Invitrogen()
    ITEM = _Item()
    JAX = _Jackson_Laboratory()
    JANELIA = _Janelia_Research_Campus()
    JULABO = _Julabo()
    KTGF = _Klingenstein_Third_Generation_Foundation()
    KOWA = _Kowa()
    LG = _Lg()
    LEICA = _Leica()
    LUMEN_DYNAMICS = _Lumen_Dynamics()
    LIFECANVAS = _Lifecanvas()
    LSRF = _Life_Sciences_Research_Foundation()
    MBF = _Mbf_Bioscience()
    MCKNIGHT_BRAIN_RESEARCH_FOUNDATION = _Mcknight_Brain_Research_Foundation()
    MCKNIGHT_FOUNDATION = _Mcknight_Foundation()
    MKS_NEWPORT = _Mks_Newport()
    MPI = _Mpi()
    MEADOWLARK_OPTICS = _Meadowlark_Optics()
    MJFF = _Michael_J_Fox_Foundation_For_Parkinson_S_Research()
    MIDOPT = _Midwest_Optical_Systems_Inc_()
    MITUTUYO = _Mitutuyo()
    NRESEARCH_INC = _Nresearch_Inc()
    NCCIH = _National_Center_For_Complementary_And_Integrative_Health()
    NIMH = _National_Institute_Of_Mental_Health()
    NINDS = _National_Institute_Of_Neurological_Disorders_And_Stroke()
    NIA = _National_Institute_On_Aging()
    NATIONAL_INSTRUMENTS = _National_Instruments()
    NSF = _U_S_National_Science_Foundation()
    NAVITAR = _Navitar()
    NEUROPHOTOMETRICS = _Neurophotometrics()
    NEW_SCALE_TECHNOLOGIES = _New_Scale_Technologies()
    NYU = _New_York_University()
    NIKON = _Nikon()
    OLYMPUS = _Olympus()
    OEPS = _Open_Ephys_Production_Site()
    OPTOTUNE = _Optotune()
    OTHER = _Other()
    OXXIUS = _Oxxius()
    PEW_CHARITABLE_TRUSTS = _Pew_Charitable_Trusts()
    PLACID_INDUSTRIES = _Placid_Industries()
    PRIZMATIX = _Prizmatix()
    QUANTIFI = _Quantifi()
    RASPBERRY_PI = _Raspberry_Pi()
    ROCKLAND = _Rockland_Immunochemicals()
    SAME_SKY = _Same_Sky()
    SICGEN = _Sicgen()
    SCHNEIDER_KREUZNACH = _Schneider_Kreuznach()
    SECOND_ORDER_EFFECTS = _Second_Order_Effects()
    SEMROCK = _Semrock()
    SIGMA_ALDRICH = _Sigma_Aldrich()
    SIMONS_FOUNDATION = _Simons_Foundation()
    SPINNAKER = _Spinnaker()
    SYNAPTIC_SYSTEMS = _Synaptic_Systems()
    TAMRON = _Tamron()
    TMC = _Technical_Manufacturing_Corporation()
    FLIR = _Teledyne_Flir()
    TWCF = _Templeton_World_Charity_Foundation()
    THE_IMAGING_SOURCE = _The_Imaging_Source()
    THE_LEE_COMPANY = _The_Lee_Company()
    THERMO_FISHER_SCIENTIFIC = _Thermo_Fisher_Scientific()
    THORLABS = _Thorlabs()
    TRANSDUCER_TECHNIQUES = _Transducer_Techniques()
    TYMPHANY = _Tymphany()
    DOD = _United_States_Department_Of_Defense()
    DOE = _United_States_Department_Of_Energy()
    VIEWORKS = _Vieworks()
    VORTRAN = _Vortran()
    W__M__KECK_FOUNDATION = _W_M_Keck_Foundation()
    WARREN_ALPERT_FOUNDATION = _Warren_Alpert_Foundation()
    AMS_OSRAM = _Ams_Osram()

    ALL = tuple(_OrganizationModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(_OrganizationModel.__subclasses__())], Field(discriminator="name")]

    abbreviation_map = {m().abbreviation: m() for m in ALL if m().abbreviation is not None}

    @classmethod
    def from_abbreviation(cls, abbreviation: str):
        """Get platform from abbreviation"""
        return cls.abbreviation_map.get(abbreviation, None)

    name_map = {m().name: m() for m in ALL}

    @classmethod
    def from_name(cls, name: str):
        """Get platform from name"""
        return cls.name_map.get(name, None)


Organization.DETECTOR_MANUFACTURERS = one_of_instance(
    [
        Organization.AILIPU,
        Organization.ALLIED,
        Organization.BASLER,
        Organization.DODOTRONIC,
        Organization.EDMUND_OPTICS,
        Organization.HAMAMATSU,
        Organization.SPINNAKER,
        Organization.FLIR,
        Organization.THE_IMAGING_SOURCE,
        Organization.THORLABS,
        Organization.VIEWORKS,
        Organization.OTHER,
    ]
)

Organization.FILTER_MANUFACTURERS = one_of_instance(
    [
        Organization.CHROMA,
        Organization.EDMUND_OPTICS,
        Organization.MIDOPT,
        Organization.SEMROCK,
        Organization.THORLABS,
        Organization.OTHER,
    ]
)

Organization.LENS_MANUFACTURERS = one_of_instance(
    [
        Organization.COMPUTAR,
        Organization.EDMUND_OPTICS,
        Organization.FUJINON,
        Organization.HAMAMATSU,
        Organization.INFINITY_PHOTO_OPTICAL,
        Organization.KOWA,
        Organization.LEICA,
        Organization.MITUTUYO,
        Organization.NAVITAR,
        Organization.NIKON,
        Organization.OLYMPUS,
        Organization.SCHNEIDER_KREUZNACH,
        Organization.TAMRON,
        Organization.THORLABS,
        Organization.CARL_ZEISS,
        Organization.OTHER,
    ]
)

Organization.DAQ_DEVICE_MANUFACTURERS = one_of_instance(
    [
        Organization.AIND,
        Organization.CHAMPALIMAUD,
        Organization.NATIONAL_INSTRUMENTS,
        Organization.IMEC,
        Organization.OEPS,
        Organization.SECOND_ORDER_EFFECTS,
        Organization.OTHER,
    ]
)

Organization.LASER_MANUFACTURERS = one_of_instance(
    [
        Organization.COHERENT_SCIENTIFIC,
        Organization.HAMAMATSU,
        Organization.OXXIUS,
        Organization.QUANTIFI,
        Organization.VORTRAN,
        Organization.OTHER,
    ]
)

Organization.LED_MANUFACTURERS = one_of_instance(
    [Organization.AMS_OSRAM, Organization.DORIC, Organization.PRIZMATIX, Organization.THORLABS, Organization.OTHER]
)

Organization.MANIPULATOR_MANUFACTURERS = one_of_instance([Organization.NEW_SCALE_TECHNOLOGIES, Organization.OTHER])

Organization.MONITOR_MANUFACTURERS = one_of_instance([Organization.ASUS, Organization.LG, Organization.OTHER])

Organization.SPEAKER_MANUFACTURERS = one_of_instance(
    [Organization.DIGIKEY, Organization.TYMPHANY, Organization.ISL, Organization.OTHER]
)

Organization.FUNDERS = one_of_instance(
    [
        Organization.AI,
        Organization.ASAP,
        Organization.CZI,
        Organization.ESTHER_A____JOSEPH_KLINGENSTEIN_FUND,
        Organization.G__HAROLD___LEILA_Y__MATHERS_FOUNDATION,
        Organization.HELEN_HAY_WHITNEY_FOUNDATION,
        Organization.KTGF,
        Organization.LSRF,
        Organization.MBF,
        Organization.MCKNIGHT_BRAIN_RESEARCH_FOUNDATION,
        Organization.MCKNIGHT_FOUNDATION,
        Organization.MJFF,
        Organization.NCCIH,
        Organization.NIA,
        Organization.NIMH,
        Organization.NINDS,
        Organization.NSF,
        Organization.PEW_CHARITABLE_TRUSTS,
        Organization.SIMONS_FOUNDATION,
        Organization.TWCF,
        Organization.DOD,
        Organization.DOE,
        Organization.W__M__KECK_FOUNDATION,
        Organization.WARREN_ALPERT_FOUNDATION,
    ]
)

Organization.RESEARCH_INSTITUTIONS = one_of_instance(
    [
        Organization.AIBS,
        Organization.AIND,
        Organization.COLUMBIA,
        Organization.HUST,
        Organization.JANELIA,
        Organization.NYU,
        Organization.OTHER,
    ]
)

Organization.SUBJECT_SOURCES = one_of_instance(
    [
        Organization.AI,
        Organization.COLUMBIA,
        Organization.HUST,
        Organization.JANELIA,
        Organization.JAX,
        Organization.NYU,
        Organization.OTHER,
    ]
)

Organization.CATHETER_IMPLANT_INSTITUTIONS = one_of_instance(
    [
        Organization.AIND,
        Organization.CRL,
        Organization.JAX,
        Organization.OTHER,
    ]
)
