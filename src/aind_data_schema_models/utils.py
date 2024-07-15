from pydantic import BaseModel, create_model, ConfigDict, Field
import json
from typing import List, Annotated, Union, Optional, Literal, Callable
import re


def create_literal_model(obj:dict, base_model:BaseModel, discriminator:str):
    """ make a dynamic pydantic literal model """
    
    literal_fields = { k: (Literal[v], v) for k,v in obj.items() }

    return create_model(create_model_class_name(obj[discriminator]),
                        model_config=ConfigDict(frozen=True),
                        __base__=base_model,
                        **literal_fields)


def create_model_class_name(class_name:str):
    """lint class name"""
    return re.sub(r'\s+', '', class_name)


def create_literal_class(objects:List[dict], class_name:str, base_model:BaseModel=BaseModel, discriminator:str='name'):    
    cls = type(class_name, (object,), {})

    # add a "ALL" class variable
    all_models = tuple(
        create_literal_model(obj=obj, base_model=base_model, discriminator=discriminator) 
        for obj in objects
    )
        
    setattr(
        cls, 
        '_ALL',
        Annotated[Union[all_models], Field(discriminator=discriminator)]
    )

    setattr(
        cls,
        'ONE_OF',
        Annotated[Union[cls._ALL], Field(discriminator="name")]
    )    

    # add the model instances as class variables
    for m in all_models:        
        setattr(cls, m.__name__, m())

    return cls