from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin


class Obra(Base, TimestampMixin):
    __tablename__ = "obras"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    direccion: Mapped[str | None] = mapped_column(String(300))
    descripcion: Mapped[str | None] = mapped_column(Text)
    activa: Mapped[bool] = mapped_column(default=True, nullable=False)

    # Relaciones
    trabajadores: Mapped[list["Trabajador"]] = relationship(
        back_populates="obra", cascade="all, delete-orphan"
    )
    gastos: Mapped[list["Gasto"]] = relationship(
        back_populates="obra", cascade="all, delete-orphan"
    )