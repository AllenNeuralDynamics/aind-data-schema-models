"""Harp device types"""

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated


class HarpDeviceTypeModel(BaseModel):
    """Base model for platform"""

    model_config = ConfigDict(frozen=True)
    whoami: int = Field(..., title="Harp whoami value")
    name: str = Field(..., title="Harp device type name")


class _Usbhub(HarpDeviceTypeModel):
    """Model USBHub"""

    name: Literal["USBHub"] = "USBHub"
    whoami: Literal[256] = 256


class _Poke(HarpDeviceTypeModel):
    """Model Poke"""

    name: Literal["Poke"] = "Poke"
    whoami: Literal[1024] = 1024


class _Multipwmgenerator(HarpDeviceTypeModel):
    """Model MultiPwmGenerator"""

    name: Literal["MultiPwmGenerator"] = "MultiPwmGenerator"
    whoami: Literal[1040] = 1040


class _Wear(HarpDeviceTypeModel):
    """Model Wear"""

    name: Literal["Wear"] = "Wear"
    whoami: Literal[1056] = 1056


class _Wearbasestationgen2(HarpDeviceTypeModel):
    """Model WearBaseStationGen2"""

    name: Literal["WearBaseStationGen2"] = "WearBaseStationGen2"
    whoami: Literal[1058] = 1058


class _Driver12Volts(HarpDeviceTypeModel):
    """Model Driver12Volts"""

    name: Literal["Driver12Volts"] = "Driver12Volts"
    whoami: Literal[1072] = 1072


class _Ledcontroller(HarpDeviceTypeModel):
    """Model LedController"""

    name: Literal["LedController"] = "LedController"
    whoami: Literal[1088] = 1088


class _Synchronizer(HarpDeviceTypeModel):
    """Model Synchronizer"""

    name: Literal["Synchronizer"] = "Synchronizer"
    whoami: Literal[1104] = 1104


class _Inputexpander(HarpDeviceTypeModel):
    """Model InputExpander"""

    name: Literal["InputExpander"] = "InputExpander"
    whoami: Literal[1106] = 1106


class _Outputexpander(HarpDeviceTypeModel):
    """Model OutputExpander"""

    name: Literal["OutputExpander"] = "OutputExpander"
    whoami: Literal[1108] = 1108


class _Simpleanaloggenerator(HarpDeviceTypeModel):
    """Model SimpleAnalogGenerator"""

    name: Literal["SimpleAnalogGenerator"] = "SimpleAnalogGenerator"
    whoami: Literal[1121] = 1121


class _Stepperdriver(HarpDeviceTypeModel):
    """Model StepperDriver"""

    name: Literal["StepperDriver"] = "StepperDriver"
    whoami: Literal[1130] = 1130


class _Archimedes(HarpDeviceTypeModel):
    """Model Archimedes"""

    name: Literal["Archimedes"] = "Archimedes"
    whoami: Literal[1136] = 1136


class _Olfactometer(HarpDeviceTypeModel):
    """Model Olfactometer"""

    name: Literal["Olfactometer"] = "Olfactometer"
    whoami: Literal[1140] = 1140


class _Clocksynchronizer(HarpDeviceTypeModel):
    """Model ClockSynchronizer"""

    name: Literal["ClockSynchronizer"] = "ClockSynchronizer"
    whoami: Literal[1152] = 1152


class _Timestampgeneratorgen1(HarpDeviceTypeModel):
    """Model TimestampGeneratorGen1"""

    name: Literal["TimestampGeneratorGen1"] = "TimestampGeneratorGen1"
    whoami: Literal[1154] = 1154


class _Timestampgeneratorgen3(HarpDeviceTypeModel):
    """Model TimestampGeneratorGen3"""

    name: Literal["TimestampGeneratorGen3"] = "TimestampGeneratorGen3"
    whoami: Literal[1158] = 1158


class _Cameracontroller(HarpDeviceTypeModel):
    """Model CameraController"""

    name: Literal["CameraController"] = "CameraController"
    whoami: Literal[1168] = 1168


class _Cameracontrollergen2(HarpDeviceTypeModel):
    """Model CameraControllerGen2"""

    name: Literal["CameraControllerGen2"] = "CameraControllerGen2"
    whoami: Literal[1170] = 1170


class _Pycontroladapter(HarpDeviceTypeModel):
    """Model PyControlAdapter"""

    name: Literal["PyControlAdapter"] = "PyControlAdapter"
    whoami: Literal[1184] = 1184


class _Behavior(HarpDeviceTypeModel):
    """Model Behavior"""

    name: Literal["Behavior"] = "Behavior"
    whoami: Literal[1216] = 1216


class _Vestibularh1(HarpDeviceTypeModel):
    """Model VestibularH1"""

    name: Literal["VestibularH1"] = "VestibularH1"
    whoami: Literal[1224] = 1224


class _Vestibularh2(HarpDeviceTypeModel):
    """Model VestibularH2"""

    name: Literal["VestibularH2"] = "VestibularH2"
    whoami: Literal[1225] = 1225


class _Loadcells(HarpDeviceTypeModel):
    """Model LoadCells"""

    name: Literal["LoadCells"] = "LoadCells"
    whoami: Literal[1232] = 1232


class _Analoginput(HarpDeviceTypeModel):
    """Model AnalogInput"""

    name: Literal["AnalogInput"] = "AnalogInput"
    whoami: Literal[1236] = 1236


class _Rgbarray(HarpDeviceTypeModel):
    """Model RgbArray"""

    name: Literal["RgbArray"] = "RgbArray"
    whoami: Literal[1248] = 1248


class _Flypad(HarpDeviceTypeModel):
    """Model FlyPad"""

    name: Literal["FlyPad"] = "FlyPad"
    whoami: Literal[1200] = 1200


class _Soundcard(HarpDeviceTypeModel):
    """Model SoundCard"""

    name: Literal["SoundCard"] = "SoundCard"
    whoami: Literal[1280] = 1280


class _Syringepump(HarpDeviceTypeModel):
    """Model SyringePump"""

    name: Literal["SyringePump"] = "SyringePump"
    whoami: Literal[1296] = 1296


class _Neurophotometricsfp3002(HarpDeviceTypeModel):
    """Model NeurophotometricsFP3002"""

    name: Literal["NeurophotometricsFP3002"] = "NeurophotometricsFP3002"
    whoami: Literal[2064] = 2064


class _Ibl_Behavior_Control(HarpDeviceTypeModel):
    """Model Ibl_behavior_control"""

    name: Literal["Ibl_behavior_control"] = "Ibl_behavior_control"
    whoami: Literal[2080] = 2080


class _Rfidreader(HarpDeviceTypeModel):
    """Model RfidReader"""

    name: Literal["RfidReader"] = "RfidReader"
    whoami: Literal[2094] = 2094


class _Pluma(HarpDeviceTypeModel):
    """Model Pluma"""

    name: Literal["Pluma"] = "Pluma"
    whoami: Literal[2110] = 2110


class _Licketysplit(HarpDeviceTypeModel):
    """Model LicketySplit"""

    name: Literal["LicketySplit"] = "LicketySplit"
    whoami: Literal[1400] = 1400


class _Sniffdetector(HarpDeviceTypeModel):
    """Model SniffDetector"""

    name: Literal["SniffDetector"] = "SniffDetector"
    whoami: Literal[1401] = 1401


class _Treadmill(HarpDeviceTypeModel):
    """Model Treadmill"""

    name: Literal["Treadmill"] = "Treadmill"
    whoami: Literal[1402] = 1402


class _Cuttlefish(HarpDeviceTypeModel):
    """Model cuTTLefish"""

    name: Literal["cuTTLefish"] = "cuTTLefish"
    whoami: Literal[1403] = 1403


class _Whiterabbit(HarpDeviceTypeModel):
    """Model WhiteRabbit"""

    name: Literal["WhiteRabbit"] = "WhiteRabbit"
    whoami: Literal[1404] = 1404


class _Environmentsensor(HarpDeviceTypeModel):
    """Model EnvironmentSensor"""

    name: Literal["EnvironmentSensor"] = "EnvironmentSensor"
    whoami: Literal[1405] = 1405


class HarpDeviceType:
    """Harp device types"""

    USBHUB = _Usbhub()
    POKE = _Poke()
    MULTIPWMGENERATOR = _Multipwmgenerator()
    WEAR = _Wear()
    WEARBASESTATIONGEN2 = _Wearbasestationgen2()
    DRIVER12VOLTS = _Driver12Volts()
    LEDCONTROLLER = _Ledcontroller()
    SYNCHRONIZER = _Synchronizer()
    TIMESTAMP_GENERATOR_GEN_1 = _Timestamp_Generator_Gen_1()
    TIMESTAMP_GENERATOR_GEN_3 = _Timestamp_Generator_Gen_3()
    TREADMILL = _Treadmill()
    CUTTLEFISH = _Cuttlefish()
    WHITERABBIT = _Whiterabbit()
    ENVIRONMENTSENSOR = _Environmentsensor()

    ALL = tuple(HarpDeviceTypeModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(HarpDeviceTypeModel.__subclasses__())], Field(discriminator="name")]
