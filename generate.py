from pathlib import Path

from aind_data_schema_models.generators._base import (
    _HarpDeviceTypeModel,
    _ModalityModel,
    _PlatformModel,
    _RegistryModel,
    _SpeciesModel,
)
from aind_data_schema_models.generators.generators import GeneratorContext, MappableReferenceField, ModelGenerator
from aind_data_schema_models.generators.parsers import csv_parser, get_who_am_i_list
from aind_data_schema_models.registries import Registry

if __name__ == "__main__":

    root = Path(__file__).parent / r"src/aind_data_schema_models/models"
    target_folder = Path(r".\src\aind_data_schema_models\_generated")

    platforms = ModelGenerator(
        enum_like_class_name="_Platform",
        parent_model_type=_PlatformModel,
        discriminator="name",
        data_source_identifier="platforms.csv",
        parser=lambda: csv_parser(root / "platforms.csv"),
    )

    modalities = ModelGenerator(
        enum_like_class_name="_Modality",
        parent_model_type=_ModalityModel,
        discriminator="name",
        data_source_identifier="modalities.csv",
        parser=lambda: csv_parser(root / "modalities.csv"),
    )

    harp_device_types = ModelGenerator(
        enum_like_class_name="_HarpDeviceType",
        parent_model_type=_HarpDeviceTypeModel,
        discriminator="name",
        data_source_identifier="https://raw.githubusercontent.com/harp-tech/protocol/97ded281bd1d0d7537f90ebf545d74cf8ba8805e/whoami.yml",
        parser=lambda: get_who_am_i_list(
            url="https://raw.githubusercontent.com/harp-tech/protocol/97ded281bd1d0d7537f90ebf545d74cf8ba8805e/whoami.yml"
        ),
        render_abbreviation_map=False,
    )

    registry = ModelGenerator(
        enum_like_class_name="_Registry",
        parent_model_type=_RegistryModel,
        discriminator="name",
        data_source_identifier="registries.csv",
        parser=lambda: csv_parser(root / "registries.csv"),
    )

    species = ModelGenerator(
        enum_like_class_name="_Species",
        parent_model_type=_SpeciesModel,
        discriminator="name",
        data_source_identifier="species.csv",
        parser=lambda: csv_parser(root / "species.csv"),
        render_abbreviation_map=False,
        mappable_references=[
            MappableReferenceField(
                typeof=Registry,
                field_name="registry",
                parsed_source_keys_handlers=["registry_abbreviation"],
                pattern="_Registry.{}",
            ),
            MappableReferenceField(
                typeof=str,
                field_name="registry_identifier",
                parsed_source_keys_handlers=["registry_identifier"],
                pattern='"{}"',
            ),
        ],
    )

    with GeneratorContext() as ctx:
        ctx.add_generator(harp_device_types, "harp_types.py")
        ctx.add_generator(platforms, "platforms.py")
        ctx.add_generator(modalities, "modalities.py")
        ctx.add_generator(registry, "registries.py")
        ctx.add_generator(species, "species.py")
        ctx.write_all(target_folder)