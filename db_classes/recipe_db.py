from sqlalchemy import ForeignKey
from sqlalchemy import update, delete, func
from sqlalchemy.orm import Mapped, mapped_column
from db_classes.db import Base, find_changes
from db_classes.collection_db import Collection
from db_classes.user_db import User



class Recipe(Base):
    __tablename__ = "recipes"

    recipe_id: Mapped[int] = mapped_column('recipe_id', primary_key=True)
    name: Mapped[str] = mapped_column('name')
    cook_time: Mapped[str] = mapped_column('cook_time')
    servings: Mapped[int] = mapped_column('servings')
    calories: Mapped[int] = mapped_column('calories')
    instructions: Mapped[str] = mapped_column('instructions')
    collection_id: Mapped[Collection] = mapped_column('collection_id', ForeignKey('collections.collection_id')
                                                      , default=-1)
    user_id: Mapped[User] = mapped_column('user_id', ForeignKey('users.user_id'))
    meal_type: Mapped[str] = mapped_column('meal_type', default='misc')
    photo_url: Mapped[str] = mapped_column('photo_url', default='https://placehold.co/600x400')

    def __init__(self, name, cook_time, servings, calories, instructions, meal_type="misc",
                 photo_url='https://placehold.co/600x400', collection=-1, user_id=-1):
        self.name = name
        self.cook_time = cook_time
        self.servings = servings
        self.calories = calories
        self.instructions = instructions
        self.meal_type = meal_type
        self.photo_url = photo_url
        self.collection_id = collection
        self.user_id = user_id

    def __repr__(self):
        return f"Recipe: {self.name}\nCook Time: {self.cook_time}\tCalories: {self.calories}\n{self.instructions}"


def get_all_recipes(session):
    recipes = session.query(Recipe).all()
    return recipes


def recipe_lookup(recipe_id, session):
    from db_classes.recipe_ingredient_db import get_recipe_ingredients
    recipe = session.query(Recipe).filter(Recipe.recipe_id == recipe_id).first()
    recipe.__dict__['ingredients'] = get_recipe_ingredients(recipe.recipe_id, session=session)
    # recipe_obj = {
    #     'name': recipe.name,
    #     'ingredients': get_recipe_ingredients(recipe.recipe_id, session=session),
    #     'servings': recipe.servings,
    #     'cook time': recipe.cook_time,
    #     'calories': recipe.calories,
    #     'instructions': recipe.instructions,
    #     'photo_url': recipe.photo_url
    # }

    return recipe


def meal_type_lookup(sort_by, session):
    recipes = session.query(Recipe).filter(func.lower(Recipe.meal_type) == sort_by.lower())
    return recipes


def create_recipe(name, cook_time, servings, calories, instructions,session, meal_type="misc",
                  photo_url='https://placehold.co/250x250', collection=-1, user_id=-1):

    recipe = Recipe(name, cook_time, servings, calories, instructions, meal_type, photo_url,
                    collection, user_id)
    session.add(recipe)
    session.commit()
    session.refresh(recipe)
    return recipe.recipe_id


def edit_recipe(recipe, session, engine):
    recipe_params = {param: value for param, value in recipe.items() if value is not None}
    selected_recipe = session.query(Recipe).filter(Recipe.recipe_id == recipe['recipe_id']).first()
    # new_set = set(recipe_params.items())

    old_recipe = selected_recipe.__dict__
    del old_recipe['_sa_instance_state']
    # old_set = set(old_recipe.items())

    changes = find_changes(old_recipe.items(), recipe_params.items())

    stmt = update(Recipe).where(Recipe.recipe_id == selected_recipe.recipe_id).values(changes)

    if changes:
        with engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()
            print(res)


def delete_recipe(recipe_id, session, engine):
    stmt = delete(Recipe).where(Recipe.recipe_id == recipe_id)

    with engine.connect() as conn:
        res = conn.execute(stmt)
        conn.commit()
        print(res)
