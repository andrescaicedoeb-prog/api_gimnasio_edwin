from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import Membresia, MembresiaCreate, MembresiaUpdate
from database import membresias_db, cargar_datos_iniciales

app = FastAPI(title="API Gimnasio - Membresías")

cargar_datos_iniciales()

@app.get("/membresias", response_model=List[Membresia])
def listar_membresias():
    return membresias_db

@app.get("/membresias/{id}", response_model=Membresia)
def ver_membresia(id: UUID):
    for membresia in membresias_db:
        if membresia.id == id:
            return membresia
    raise HTTPException(status_code=404, detail="Membresía no encontrada")


@app.post("/membresias", response_model=Membresia, status_code=201)
def crear_membresia(datos: MembresiaCreate):

    for membresia in membresias_db:
        if membresia.nombre_usuario.lower() == datos.nombre_usuario.lower():
            raise HTTPException(status_code=400, detail="Ya existe una membresía para ese usuario")

    nueva = Membresia(**datos.model_dump()) 
    membresias_db.append(nueva)
    return nueva

@app.put("/membresias/{id}", response_model=Membresia)
def editar_membresia(id: UUID, datos: MembresiaUpdate):
    for i, membresia in enumerate(membresias_db):
        if membresia.id == id:
            cambios = datos.model_dump(exclude_unset=True)

            nuevo_nombre = cambios.get("nombre_usuario")
            if nuevo_nombre:
                for otra in membresias_db:
                    if otra.id != id and otra.nombre_usuario.lower() == nuevo_nombre.lower():
                        raise HTTPException(status_code=400, detail="Ya existe una membresía para ese usuario")

            membresias_db[i] = membresia.model_copy(update=cambios)
            return membresias_db[i]
    raise HTTPException(status_code=404, detail="Membresía no encontrada")

@app.delete("/membresias/{id}")
def borrar_membresia(id: UUID):
    for membresia in membresias_db:
        if membresia.id == id:
            membresias_db.remove(membresia)
            return {"mensaje": "Membresía eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Membresía no encontrada")