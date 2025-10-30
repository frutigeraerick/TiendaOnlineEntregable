from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from sqlmodel import SQLModel
import models, schemas, crud
from database import engine, SessionLocal

SQLModel.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Categorías y Productos",
    description="Proyecto Parcial",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/categorias/", response_model=schemas.CategoriaRead, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@app.get("/categorias/", response_model=list[schemas.CategoriaRead])
def obtener_categorias_activas(db: Session = Depends(get_db)):
    return crud.obtener_categorias_activas(db)

@app.get("/categorias/{categoria_id}", response_model=schemas.CategoriaReadConProductos)
def obtener_categoria_con_productos(categoria_id: int, db: Session = Depends(get_db)):
    return crud.obtener_categoria_con_productos(db, categoria_id)

@app.put("/categorias/{categoria_id}", response_model=schemas.CategoriaRead)
def actualizar_categoria(categoria_id: int, datos: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    return crud.actualizar_categoria(db, categoria_id, datos)

@app.delete("/categorias/{categoria_id}")
def desactivar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return crud.desactivar_categoria(db, categoria_id)

@app.post("/productos/", response_model=schemas.ProductoRead, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/", response_model=list[schemas.ProductoRead])
def listar_productos(categoria_id: int = None, stock_min: int = None, precio_max: float = None, db: Session = Depends(get_db)):
    return crud.listar_productos(db, categoria_id, stock_min, precio_max)

@app.get("/productos/{producto_id}", response_model=schemas.ProductoReadConCategoria)
def obtener_producto_con_categoria(producto_id: int, db: Session = Depends(get_db)):
    return crud.obtener_producto_con_categoria(db, producto_id)

@app.put("/productos/{producto_id}/restar_stock", response_model=schemas.ProductoRead)
def restar_stock(producto_id: int, cantidad: int, db: Session = Depends(get_db)):
    return crud.restar_stock(db, producto_id, cantidad)