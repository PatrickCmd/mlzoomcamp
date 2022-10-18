import numpy as np

import bentoml
from bentoml.io import JSON
from pydantic import BaseModel


class CreditApplication(BaseModel):
    """Pydantic schema for the data being sent

    {
        "name": "Tim",
        "age": 37,
        "country": "US",
        "rating": 3.14
    }
    """
    name: str
    age: int
    country: str
    rating: float
