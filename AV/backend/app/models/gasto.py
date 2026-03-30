from datetime import date
from decimal import Decimal
from sqlalchemy import Date, ForeignKey, Numeric, String, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin


class CategoriaGasto(str):
    MATERIALES = "materiales"
    HERRAMIENTAS = "herramientas"
    TRANSPORTE = "transporte"
    ALIMENTACION = "alimentacion"
    SERVICIOS = "servicios"
    OTRO = "otro"


class EstadoGasto(str):
    PENDIENTE = "pendiente"       # recién subido, sin validar
    PROCESADO = "procesado"       # OCR corrió, datos extraídos
    VALIDADO = "validado"         # aprobado por encargado
    RECHAZADO = "rechazado"


class Gasto(Base, TimestampMixin):
    __tablename__ = "gastos"
    __table_args__ = (
        CheckConstraint("total >= 0", name="ck_gasto_total_positivo"),
        CheckConstraint(
            "estado IN ('pendiente', 'procesado', 'validado', 'rechazado')",
            name="ck_gasto_estado_valido",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    obra_id: Mapped[int] = mapped_column(
        ForeignKey("obras.id", ondelete="CASCADE"), nullable=False, index=True
    )
    registrado_por_id: Mapped[int | None] = mapped_column(
        ForeignKey("trabajadores.id", ondelete="SET NULL"), nullable=True
    )

    # Datos extraídos por OCR + parser
    proveedor: Mapped[str | None] = mapped_column(String(200))
    nit: Mapped[str | None] = mapped_column(String(20))          # NIT colombiano: 123.456.789-0
    numero_factura: Mapped[str | None] = mapped_column(String(50))
    fecha_factura: Mapped[date | None] = mapped_column(Date)
    total: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))

    # Clasificación
    categoria: Mapped[str] = mapped_column(
        String(50), default=CategoriaGasto.OTRO, nullable=False
    )
    descripcion: Mapped[str | None] = mapped_column(Text)

    # Estado del pipeline OCR
    estado: Mapped[str] = mapped_column(
        String(20), default=EstadoGasto.PENDIENTE, nullable=False, index=True
    )

    # Archivos
    imagen_path: Mapped[str | None] = mapped_column(String(500))  # ruta en storage
    texto_ocr_raw: Mapped[str | None] = mapped_column(Text)       # output crudo del OCR

    # Confianza del parser (0.0 a 1.0)
    confianza_ocr: Mapped[Decimal | None] = mapped_column(Numeric(3, 2))

    # Relaciones
    obra: Mapped["Obra"] = relationship(back_populates="gastos")
    registrado_por: Mapped["Trabajador | None"] = relationship(
        foreign_keys=[registrado_por_id]
    )

    def __repr__(self) -> str:
        return f"<Gasto id={self.id} proveedor={self.proveedor!r} total={self.total} estado={self.estado!r}>"