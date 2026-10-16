from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data1 = {'id' : 101, 'name' : 'Josh Supreme', 'is_active' : True}
input_data2 = {'id' : '101', 'name' : 'Josh Supreme', 'is_active' : 'True'}
input_data3 = {'id' : '101A', 'name' : 'Josh Supreme', 'is_active' : 'Its True'}

user1 = User(**input_data1)
user2 = User(**input_data2)
user3 = User(**input_data3)

print(user1)
print(user2)
print(user3)

""" 
Prints user1 and user2 without any issues
as Pydantic auto-converts them

but 

user3 fails because it cannot auto convert it
"""