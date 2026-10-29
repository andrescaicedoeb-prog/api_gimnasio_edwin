from models import Membresia

membresias_db = []

def cargar_datos_iniciales():
    membresias_db.clear() 

    membresias_db.append(Membresia(
        nombre_usuario="Carlos Perez",
        plan_suscripcion="Basico",
        meses_duracion=3,
        activo=True
    ))
    membresias_db.append(Membresia(
        nombre_usuario="Laura Gomez",
        plan_suscripcion="Premium",
        meses_duracion=6,
        activo=True
    ))
    membresias_db.append(Membresia(
        nombre_usuario="Andres Rojas",
        plan_suscripcion="VIP",
        meses_duracion=12,
        activo=False
    ))
    membresias_db.append(Membresia(
        nombre_usuario="Maria Torres",
        plan_suscripcion="Basico",
        meses_duracion=1,
        activo=False
    ))