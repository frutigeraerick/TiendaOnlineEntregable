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

def obtener_categoria_con_productos(db: Session, categoria_id: int):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="No se encontro la categoria.")
    return categoria

def actualizar_categoria(db: Session, categoria_id: int, datos: schemas.CategoriaUpdate):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="No se encontro la categoria.")
    for campo, valor in datos.dict(exclude_unset=True).items():
        setattr(categoria, campo, valor)
    db.commit()
    db.refresh(categoria)
    return categoria

def desactivar_categoria(db: Session, categoria_id: int):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="No se encontro la categoria.")
    categoria.activa = False
    for producto in categoria.productos:
        producto.activa = False
    db.commit()
    return {"mensaje": "La categoria y sus productos han sido desactivados correctamente."}

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == producto.categoria_id).first()
    if not categoria or not categoria.activa:
        raise HTTPException(status_code=400, detail="La categoria no existe o esta inactiva.")
    nuevo_producto = models.Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        stock=producto.stock,
        descripcion=producto.descripcion,
        activa=True,
        categoria_id=producto.categoria_id
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto