from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    descripcion = Column(String, nullable=True)
    activa = Column(Boolean, default=True)

    productos = relationship("Producto", back_populates="categoria", cascade="all, delete")

    def __repr__(self):
        return f"<Categoria(nombre={self.nombre}, activa={self.activa})>"


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    descripcion = Column(String, nullable=True)
    activa = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    categoria = relationship("Categoria", back_populates="productos")

    def __repr__(self):
        return f"<Producto(nombre={self.nombre}, stock={self.stock}, activa={self.activa})>"