"""Platforms generator"""

from jinja2 import Environment
import pandas as pd
from aind_data_schema_models.utils import to_class_name

data = pd.read_csv("./src/aind_data_schema_models/models/platforms.csv")

template = """
\"\"\"Platforms\"\"\"
from pydantic import BaseModel, Field
from typing import Literal, Annotated, Union


class _PlatformModel(BaseModel):
    \"\"\"Base model for platform\"\"\"
    name: Literal[str]
    abbreviation: Literal[str]

{% for _, row in data.iterrows() %}
class _{{ row['abbreviation'] | to_class_name }}(_PlatformModel):
    \"\"\"Model {{row['abbreviation']}}\"\"\"
    name: Literal["{{ row['name'] }}"] = "{{ row['name'] }}"
    abbreviation: Literal["{{ row['abbreviation'] }}"] = "{{ row['abbreviation'] }}"

{% endfor %}
class Platform:
    \"\"\"Platforms\"\"\"
{% for _, row in data.iterrows() %}
    {{ row['abbreviation'] | to_class_name | upper }} = _{{ row['abbreviation'] | to_class_name }}()
{% endfor %}
    ALL = tuple(_PlatformModel.__subclasses__())

    ONE_OF = Annotated[Union[tuple(_PlatformModel.__subclasses__())], Field(discriminator="name")]

    abbreviation_map = {m().abbreviation: m() for m in ALL}

    @classmethod
    def from_abbreviation(cls, abbreviation: str):
        \"\"\"Get platform from abbreviation\"\"\"
        return cls.abbreviation_map.get(abbreviation, None)
"""

env = Environment()
env.filters["to_class_name"] = to_class_name

rendered_template = env.from_string(template)
rendered_code = rendered_template.render(data=data)

# Output the generated code to a file or print it
with open("./src/aind_data_schema_models/platforms.py", "w") as f:
    f.write(rendered_code)

print("Code generated in 'platforms.py'")
