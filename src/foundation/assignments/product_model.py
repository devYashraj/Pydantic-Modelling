from pydantic import BaseModel

class ProductItem(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True
    