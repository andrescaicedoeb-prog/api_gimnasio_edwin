from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class MembresiaBase(BaseModel):
    nombre_usuario: str = Field(min_length=3, max_length=50, description="Nombre del afiliado")
    plan_suscripcion: str = Field(min_length=3, max_length=30, description="Plan de la membresía (Basico, Premium, VIP)")
    meses_duracion: int = Field(gt=0, le=36, description="Duración en meses (debe ser mayor a 0)")
    activo: bool = Field(default=False, description="Indica si la membresía está activa")


class MembresiaCreate(MembresiaBase):
    pass


class MembresiaUpdate(BaseModel):
    nombre_usuario: Optional[str] = Field(default=None, min_length=3, max_length=50)
    plan_suscripcion: Optional[str] = Field(default=None, min_length=3, max_length=30)
    meses_duracion: Optional[int] = Field(default=None, gt=0, le=36)
    activo: Optional[bool] = None


class Membresia(MembresiaBase):
    id: UUID = Field(default_factory=uuid4)