from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items : List[str]
    quantities :  Dict[str, int]

class BlogPost(BaseModel):
    user_id : int
    content : str
    image_url : Optional[str] = None

