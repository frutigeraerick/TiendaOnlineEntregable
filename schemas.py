from typing import List, Optional
from pydantic import BaseModel, Field, validator

class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50, description="Nombre de la categoria")
    descripcion: Optional[str] = Field(None, max_length=200, description="Descripcion de la categoria")
    activa: Optional[bool] = True

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=50)
    descripcion: Optional[str] = Field(None, max_length=200)
    activa: Optional[bool] = None

class CategoriaOut(CategoriaBase):
    id: int
    class Config:
        orm_mode = True