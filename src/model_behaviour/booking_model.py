from pydantic import BaseModel, field_validator, computed_field, Field

class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(..., ge=1)
    rate_per_night : float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.nights * self.rate_per_night