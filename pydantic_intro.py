"""
This is very first introduction to pydantic
"""

from pydantic import BaseModel

class Foo(BaseModel):
    """
        BaseModel is a class in pydantic used for writing
        data models
        """
    count:int
    size:float

external_data ={"count":100,"size":30.5}

foo = Foo(**external_data)

print(foo)

breakpoint()