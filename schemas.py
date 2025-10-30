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

class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre del producto")
    precio: float = Field(..., gt=0, description="Precio del producto (mayor que 0)")
    stock: int = Field(..., ge=0, description="Cantidad en stock (no puede ser negativa)")
    descripcion: Optional[str] = Field(None, max_length=300, description="Descripcion del producto")
    activa: Optional[bool] = True