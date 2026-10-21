from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username : str

    # These run before the model instance is fully built
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must at least have 4 characters")
        return v


class SignupData(BaseModel):

    pwd : str
    confirm_pwd : str

    @model_validator(mode='after')
    def check_pwd_match(self):
        if self.pwd != self.confirm_pwd:
            raise ValueError("Passwords do not match")
        return self

class Product(BaseModel):
    price : float
    qty : int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.qty

