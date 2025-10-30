SISTEMA DE GESTION DE TIENDA ONLINE

Proyecto parcial desarrollado con FastAPI, SQLAlchemy y SQLite.

# Ejecución

1. Clonar repositorio:
    en el bash -> git clone <URL> -> cd <nombredelarchivo>
2. Entorno virtual (opcional):
    crear el venv -> python -m venv venv
    activar el venv -> venv\Scripts\activate
3. Instalar dependencias:
    en el bash -> pip install -r requirements.txt
4. Ejecutar servidor:
    uvicorn main:app --reload
5. Abrir la documentacion:
    http://127.0.0.1:8000/docs

# Que hace el proyecto?

Este proyecto le permite al usuario gestionar diferentes aspectos de una tienda online, los cuales son son: categorias y productos.

# Una que otra cosita sobre proyecto

1. El proyecto incluye validaciones las cuales son utilizadas en los modelos Pydantic (o sea schemas.py) para asegurar que los datos que ingrese el usuario sean correctos (basicamente, busca posibles errores y los devuelve)
2. En el endpoint GET productos se aplican filtros, para asi poder listar productos que cumplan con diferentes condiciones que se ingresem (estos filtros son stock, precio y categoria)

# Me salio un error, que podra ser?

hay diferentes codigos de error en el proyecto, aca esta lo que significa cada uno:

1. 400 (Bad Request) -> Se envio un dato incorrecto o incompleto. Esto puede pasar si no se llena un campo obligatorio o si se envia un numero negativo donde no deberia. El servidor no puede procesar la petición, y devuelve este error para avisar que hay que corregir la información.

2. 404 (Not Found) -> El recurso solicitado no existe. Por ejemplo, si se intenta obtener un producto con un ID que no está en la base de datos

3. 409 (Conflict) -> Hay un conflicto en los datos existentes. Por ejemplo, si se intenta crear una categoría con un nombre que ya existe, el sistema no lo permite y devuelve este codigo para indicar que los datos entran en conflicto con algo que ya está registrado.

# Otros codigos que podrian aparecer (pero no son de error, todo bien)

1. 200 (Ok) -> Esto aparece cuando una operacion se ejecuta correctamente.

2. 201 (Created) -> Aparece cuando se crea un registro nuevo exitosamente.

# Funcionalidad del proyecto

En el orden: Metodo -> Endpoint -> Descripcion

    Para categorias:

    POST -> /categorias/ -> Crear una nueva categoria
    GET -> /categorias/ -> Listar todas las categorias activas
    GET -> /categorias/{id} -> Obtener una categoria junto a sus productos
    PUT -> /categorias/{id} -> Actualizar una categoria existente
    DELETE -> /categorias/{id} -> Desactivar una categoria y sus productos asociados

    Para productos:

    POST -> /productos/ -> Crear un nuevo producto
    GET -> /productos/ -> Listar productos (Con filtros)
    GET -> /productos/{id} -> Obtener un producto junto con su categoria
    PUT -> /productos/{id} -> Actualizar un producto
    DELETE -> /productos/{id} -> Desactivar un producto
    PATCH -> /productos/{id}/restar_stock -> Restar stock

# Tecnologias usadas

- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn