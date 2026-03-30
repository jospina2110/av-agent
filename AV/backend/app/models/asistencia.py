from datetime import date
from sqlalchemy import Date, ForeignKey, String, Text, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin


class EstadoAsistencia(str):
    PRESENTE = "presente"
    AUSENTE = "ausente"
    INCAPACIDAD = "incapacidad"
    PERMISO = "permiso"
    DIA_FESTIVO = "dia_festivo"

    TODOS = ["presente", "ausente", "incapacidad", "permiso", "dia_festivo"]


class Asistencia(Base, TimestampMixin):
    __tablename__ = "asistencias"
    __table_args__ = (
        # Un trabajador solo puede tener un registro por día
        UniqueConstraint("trabajador_id", "fecha", name="uq_asistencia_trabajador_fecha"),
        CheckConstraint(
            "estado IN ('presente', 'ausente', 'incapacidad', 'permiso', 'dia_festivo')",
            name="ck_asistencia_estado_valido",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    trabajador_id: Mapped[int] = mapped_column(
        ForeignKey("trabajadores.id", ondelete="CASCADE"), nullable=False, index=True
    )
    registrado_por: Mapped[int | None] = mapped_column(
        ForeignKey("trabajadores.id", ondelete="SET NULL"), nullable=True
    )

    fecha: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    estado: Mapped[str] = mapped_column(
        String(20), nullable=False, default=EstadoAsistencia.PRESENTE
    )
    observacion: Mapped[str | None] = mapped_column(Text)

    # Relaciones
    trabajador: Mapped["Trabajador"] = relationship(
        back_populates="asistencias", foreign_keys=[trabajador_id]
    )

    def es_dia_laborable(self) -> bool:
        return self.estado == EstadoAsistencia.PRESENTE

    def __repr__(self) -> str:
        return f"<Asistencia trabajador_id={self.trabajador_id} fecha={self.fecha} estado={self.estado!r}>"