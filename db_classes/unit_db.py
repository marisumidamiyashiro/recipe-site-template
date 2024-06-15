from db_classes.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Unit(Base):
    __tablename__ = "units"

    unit_id: Mapped[int] = mapped_column('unit_id', primary_key=True)
    label: Mapped[str] = mapped_column('label', unique=True)

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return self.label


def get_unit(unit_id, session):
    unit = session.query(Unit).filter(Unit.unit_id == unit_id)
    return unit[0]


def create_unit(unit_label, session):
    new_unit = Unit(unit_label)
    session.add(new_unit)
    session.commit()
    session.refresh(new_unit)
    return new_unit.unit_id
