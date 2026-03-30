from datetime import date
from decimal import Decimal
from sqlalchemy import Date, ForeignKey, Numeric, Integer, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin


class Nomina(Base, TimestampMixin):
    __tablename__ = "nominas"
    __table_args__ = (
        CheckConstraint("dias_trabajados >= 0", name="ck_nomina_dias_positivos"),
        CheckConstraint("total_pagar >= 0", name="ck_nomina_total_positivo"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    trabajador_id: Mapped[int] = mapped_column(
        ForeignKey("trabajadores.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Período
    fecha_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_fin: Mapped[date] = mapped_column(Date, nullable=False)

    # Cálculo
    dias_trabajados: Mapped[int] = mapped_column(Integer, nullable=False)
    valor_dia_snapshot: Mapped[Decimal] = mapped_column(
        Numeric(12, 2), nullable=False
        # snapshot: guardamos el valor del día en el momento del cálculo
        # porque el trabajador puede cambiar de tarifa después
    )
    total_pagar: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)

    # Relaciones
    trabajador: Mapped["Trabajador"] = relationship(back_populates="nominas")

    def __repr__(self) -> str:
        return (
            f"<Nomina trabajador_id={self.trabajador_id} "
            f"periodo={self.fecha_inicio}→{self.fecha_fin} "
            f"total={self.total_pagar}>"
        )