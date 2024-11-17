"""Module for computer system and architecture definitions"""

from enum import Enum


class OperatingSystem(str, Enum):
    """Operating systems"""

    DEBIAN_11 = "Debian 11"
    DEBIAN_12 = "Debian 12"
    MACOS_BIG_SUR = "MacOS Big Sur"
    MACOS_MONTEREY = "MacOS Monterey"
    MACOS_VENTURA = "MacOS Ventura"
    MACOS_SONOMA = "MacOS Sonoma"
    MACOS_SEQUOIA = "MacOS Sequoia"
    MINT_20 = "Linux Mint 20"
    MINT_21 = "Linux Mint 21"
    MINT_22 = "Linux Mint 22"
    OTHER = "Other"
    RHEL_6 = "Red Hat Enterprise Linux 6"
    RHEL_7 = "Red Hat Enterprise Linux 7"
    RHEL_8 = "Red Hat Enterprise Linux 8"
    RHEL_9 = "Red Hat Enterprise Linux 9"
    ROCKY_8 = "Rocky Linux 8"
    ROCKY_9 = "Rocky Linux 9"
    UBUNTU_20_04 = "Ubuntu 20.04"
    UBUNTU_22_04 = "Ubuntu 22.04"
    UBUNTU_24_04 = "Ubuntu 24.04"
    WINDOWS_8 = "Windows 8"
    WINDOWS_10 = "Windows 10"
    WINDOWS_11 = "Windows 11"


class CPUArchitecture(str, Enum):
    """CPU architectures"""

    ARM = "Arm32"
    ARM64 = "Arm64"
    OTHER = "Other"
    RISC_V = "RISC-V"
    X86_32 = "x86-32"
    X86_64 = "x86-64"


class ModelBackbone(str, Enum):
    """Model backbones"""

    ALEXNET = "AlexNet"
    CUSTOM = "Custom"
    RESNET = "ResNet"
    VGGNET = "VGGNet"
    UNET = "UNet"
