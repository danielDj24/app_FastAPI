from pydantic import BaseModel, Field
from typing import Optional
class Movies(BaseModel):
    """Model for create a published movie"""
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(ge=1900, le= 2023)
    rating: float = Field(ge = 1,le= 10)
    category: str = Field(min_length=5, max_length=20 )
    
    class Config:
        """model defined structure of the database"""
        schema_extra = {
            'example':{
                "title": "pelicula",
                "overview": "descripcion de la pelicula",
                "year":2022,
                "rating":9.8,
                "category":"comedia"
            }
        }