from pydantic import BaseModel, Field
from typing import List, Optional


class Lesson(BaseModel):
    id : int
    topic : str

class Module(BaseModel):
    id : int
    name : str
    lessons : List[Lesson]

class Course(BaseModel):
    id : int
    title : str
    modules : List[Module]

