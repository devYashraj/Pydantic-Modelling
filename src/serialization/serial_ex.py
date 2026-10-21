from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class Address(BaseModel):

    street : str
    city : str
    zip_code : str

class User(BaseModel):
    id : int
    name : str
    email : str
    address : Address
    is_active : bool = True
    createdAt : datetime
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v : v.strftime('%d-%m-%Y')}
    )

# create user instance
user = User(
    id=1,
    name="Yashraj Admane",
    email='example@gmail.com',
    createdAt=datetime(2026, 3, 15, 14, 30),
    address=Address(
        street='Wanworie',
        city='Pune',
        zip_code='411040'
    ),
    tags=["techenthusiast", "self-learner"]
)

#using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)

print("++++++++++++++++++++")
#using model_dump_json
json_str = user.model_dump_json()
print(json_str)

