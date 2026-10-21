from pydantic import BaseModel, Field
from typing import List, Optional

class Address(BaseModel):

    street : str
    city : str
    postal_code : str

class User(BaseModel):
    id : int
    name : str
    address : Address

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None # Self referencing (Forward referencing)

Comment.model_rebuild() # Needed for forward referenced fields


address = Address(
    city='Pune',
    postal_code='411040',
    street='Wanowrie'
)

user = User(
    address=address,
    id=1,
    name='Yashraj Admane'
)

comment = Comment(
    id=123,
    content="That's spectacular !",
    replies=[
        Comment(
            id=124,
            content="That's spectacular ! + 2",
        ),
        Comment(
            id=125,
            content="That's spectacular ! + 3",
        )
    ]
)