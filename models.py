from typing import List
from pydantic import BaseModel, Field


class OrderRequest(BaseModel):
    id: str = Field(..., min_length=2, max_length=15, regex="^[a-zA-Z0-9]*$", description="ID for the request.")
    orders_nos: List[int]
    arrival_rate: float = Field(..., gt=0, le=1, description="Arrival Rate. It should be between 0 and 1")
    service_rate: int = Field(..., gt=0, description="Number of servers at the stall")

    class Config:
        schema_extra = {
            "example": {
                "id": "456cdfazs23",
                "orders_nos": [
                    1,
                    2,
                    3
                ],
                "arrival_rate": 0.5,
                "service_rate": 2
            }
        }


class OrderResponse(BaseModel):
    id: str
    order_nos: List[int]

    class Config:
        schema_extra = {
            "example": {
                "id": "456cdfazs23",
                "order_nos": [1, 2, 3]
            }
        }
