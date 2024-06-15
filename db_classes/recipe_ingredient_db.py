from sqlalchemy import ForeignKey, update, delete
from sqlalchemy.orm import Mapped, mapped_column
from db_classes.db import Base, find_changes
from db_classes.ingredient_db import Ingredient, get_ingredient
from db_classes.unit_db import Unit, get_unit



class RecipeIngredient(Base):
    __tablename__ = "recipe ingredients"
    from db_classes.recipe_db import Recipe
    recipe_ingredient_id: Mapped[int] = mapped_column('recipe_ingredient_id', primary_key=True)
    recipe_id: Mapped[Recipe] = mapped_column('recipe_id', ForeignKey('recipes.recipe_id'))
    ingredient_id: Mapped[Ingredient] = mapped_column('ingredient_id', ForeignKey('ingredients.ingredient_id'))
    unit_id: Mapped[Unit] = mapped_column('unit_id', ForeignKey('units.unit_id'))
    amount: Mapped[float] = mapped_column('amount')
    sort: Mapped[int] = mapped_column('sort')

    def __init__(self, recipe_id, ingredient_id, unit_id, amount, sort):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.unit_id = unit_id
        self.amount = amount
        self.sort = sort

    def __repr__(self):
        return f"recipe: {self.recipe_id}\ningredient: {self.ingredient_id}"


def create_recipe_ingredient(recipe_id, ingredient_id, unit_id, amount, sort_order, session):
    new_ingredient = RecipeIngredient(recipe_id, ingredient_id, unit_id, amount, sort_order)
    session.add(new_ingredient)
    session.commit()
    session.refresh(new_ingredient)
    return new_ingredient.recipe_ingredient_id


def get_recipe_ingredients(recipe_id, session):
    ingredients = session.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe_id)
    ingredient_list = []
    for ingredient in ingredients:
        ingredient_name = get_ingredient(ingredient.ingredient_id, session=session)
        ingredient_unit = get_unit(ingredient.unit_id, session=session)
        ingredient_tuple = (ingredient_name, ingredient.amount, ingredient_unit)

        ingredient_list.append(ingredient_tuple)

    return ingredient_list


def delete_recipe_ingredients(recipe_id, session, engine):
    # ingredients = session.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe_id)

    stmt = delete(RecipeIngredient).where(RecipeIngredient.recipe_id == recipe_id)

    with engine.connect() as conn:
        res = conn.execute(stmt)
        conn.commit()
        print(res)


def update_recipe_ingredient(recipe_ingredient, session, engine):
    ingredient_params = {param: value for param, value in recipe_ingredient.items() if value is not None}
    selected_ingredient = ((session.query(RecipeIngredient)
                           .filter(RecipeIngredient.recipe_ingredient_id == ingredient_params['recipe_ingredient_id']))
                           .first())

    old_ingredient = selected_ingredient.__dict__
    del old_ingredient['_sa_instance_state']
    changes = find_changes(old_ingredient.items(), ingredient_params.items())
    stmt = (update(RecipeIngredient)
            .where(RecipeIngredient.recipe_ingredient_id == ingredient_params['recipe_ingredient_id'])).values(changes)

    if changes:
        with engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()
            print(res)

