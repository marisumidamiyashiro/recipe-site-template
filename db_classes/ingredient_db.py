from db_classes.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Ingredient(Base):
    __tablename__ = "ingredients"

    ingredient_id: Mapped[int] = mapped_column('ingredient_id', primary_key=True)
    label: Mapped[str] = mapped_column('label', unique=True)

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return f"{self.label}"


def create_ingredient(ingredient_name, session):
    ingredient_name = str.lower(ingredient_name)
    exists = session.query(Ingredient).filter_by(label=ingredient_name).first()

    if exists:
        return exists.ingredient_id
    else:
        new_ingredient = Ingredient(ingredient_name)
        session.add(new_ingredient)
        session.commit()
        session.refresh(new_ingredient)
        return new_ingredient.ingredient_id


def get_ingredient(ingredient_id, session):
    ingredient = session.query(Ingredient).filter(Ingredient.ingredient_id == ingredient_id)

    return ingredient[0]


# def create(ingredient_labels, session):
#     i = 1
#     ingredient_ids = []
#     for ingredient in ingredient_labels:
#         exists = session.query(Ingredient).filter_by(label=ingredient["label"]).first()
#         if exists:
#             ingredient_id = exists.ingredient_id
#         else:
#             ingredient_id = create_ingredient(ingredient["label"], session=session)
#         ingredient_ids.append(ingredient_id)
#         i += 1
#
#     return ingredient_ids

