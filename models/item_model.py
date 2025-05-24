from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class ItemModel(BaseModel):
    _id: ObjectId 
    name: str
    description: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            str: lambda x: str(x),
        }