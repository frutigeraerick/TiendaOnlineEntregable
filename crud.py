from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schemas

def crear_categoria(db: Session, categoria: schemas.CategoriaCreate):
    existente = db.query(models.Categoria).filter(models.Categoria.nombre == categoria.nombre).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe una categoria con ese nombre.")
    nueva_categoria = models.Categoria(nombre=categoria.nombre, descripcion=categoria.descripcion, activa=True)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

def obtener_categorias_activas(db: Session):
    return db.query(models.Categoria).filter(models.Categoria.activa == True).all()