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

class ProductoCreate(ProductoBase):
    categoria_id: int = Field(..., description="ID de la categoria en la que esta el producto")

    @validator("nombre")
    def validar_nombre(cls, v):
        if not v.strip():
            raise ValueError("El nombre del producto no puede estar vacio")
        return v

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    descripcion: Optional[str] = Field(None, max_length=300)
    activa: Optional[bool] = None
    categoria_id: Optional[int] = None

class ProductoOut(ProductoBase):
    id: int
    categoria_id: int
    class Config:
        orm_mode = True

class CategoriaConProductos(CategoriaOut):
    productos: List[ProductoOut] = []

CategoriaRead = CategoriaOut
ProductoRead = ProductoOut
CategoriaReadConProductos = CategoriaConProductos
ProductoReadConCategoria = ProductoOut