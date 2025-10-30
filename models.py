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