from decimal import Decimal
from sqlalchemy import String, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin


class EspecialidadEnum(str):
    ALBANILERIA = "albanileria"
    ELECTRICIDAD = "electricidad"
    PLOMERIA = "plomeria"
    CARPINTERIA = "carpinteria"
    PINTURA = "pintura"
    GENERAL = "general"
    OTRO = "otro"


class Trabajador(Base, TimestampMixin):
    __tablename__ = "trabajadores"
    __table_args__ = (
        UniqueConstraint("cedula", name="uq_trabajador_cedula"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    obra_id: Mapped[int] = mapped_column(
        ForeignKey("obras.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Datos personales
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    cedula: Mapped[str] = mapped_column(String(20), nullable=False)
    telefono: Mapped[str | None] = mapped_column(String(20))

    # Datos laborales
    cargo: Mapped[str] = mapped_column(String(100), nullable=False)
    especialidad: Mapped[str] = mapped_column(
        String(50), default=EspecialidadEnum.GENERAL, nullable=False
    )
    valor_dia: Mapped[Decimal] = mapped_column(
        Numeric(12, 2), nullable=False
    )
    activo: Mapped[bool] = mapped_column(default=True, nullable=False)

    # Relaciones
    obra: Mapped["Obra"] = relationship(back_populates="trabajadores")
    asistencias: Mapped[list["Asistencia"]] = relationship(
        back_populates="trabajador", cascade="all, delete-orphan"
    )
    nominas: Mapped[list["Nomina"]] = relationship(
        back_populates="trabajador", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Trabajador id={self.id} nombre={self.nombre!r} cedula={self.cedula!r}>"