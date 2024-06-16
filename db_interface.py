from sqlalchemy import create_engine

from db_classes.db import bind_engine
from db_classes.recipe_db import (create_recipe, delete_recipe, recipe_lookup, edit_recipe, get_all_recipes,
                                  meal_type_lookup)
from db_classes.ingredient_db import create_ingredient
from db_classes.recipe_ingredient_db import (create_recipe_ingredient, delete_recipe_ingredients)
from db_classes.unit_db import create_unit, get_unit, get_all_units

engine = create_engine("sqlite:///recipesite.db")
session = bind_engine(engine)
SQLALCH_INSTANCE = '_sa_instance_state'

# recipe.get_all_recipes2(session)


def create_dummy_recipe():

    units = ["teaspoons", "tablespoons", "cups", "ounces", "pints", "gallons", 'lbs', "none"]
    for unit in units:
        create_unit(unit, session=session)

    sample_recipe_params = {
        'name': 'Chicken n Cheese',
        'cook_time': '20 minutes',
        'servings': 1,
        'calories': 300,
        'instructions': "cook it\neat it",
        'meal_type': 'Breakfast'
    }
    sample_ingredient_list = [
        {
            'label': 'chicken',
            'unit_id': '8',
            'amount': 1
        },
        {
            'label': 'Cheddar Cheese',
            'unit_id': '4',
            'amount': 10
        }
    ]
    sample_recipe = {
        'recipe_params': sample_recipe_params,
        'ingredients': sample_ingredient_list
    }

    submit_new_recipe(sample_recipe)


def submit_new_recipe(recipe):
    recipe_params = {k: v for k, v in recipe["recipe_params"].items() if v is not None}
    recipe_id = create_recipe(**recipe_params, session=session)
    i = 1
    for ingredient in recipe["ingredients"]:
        ingredient_id = create_ingredient(ingredient["label"], session=session)

        create_recipe_ingredient(recipe_id, ingredient_id, ingredient["unit_id"], ingredient["amount"], i,
                                 session=session)
        i += 1


def remove_recipe(recipe_id):
    delete_recipe(recipe_id, session=session, engine=engine)
    delete_recipe_ingredients(recipe_id, session=session, engine=engine)


def get_recipes():
    return get_all_recipes(session=session)


def get_recipe(recipe_id):
    return recipe_lookup(recipe_id, session=session)


def change_recipe(recipe):
    edit_recipe(recipe, session=session, engine=engine)


def meal_lookup(sort_by):
    return meal_type_lookup(sort_by, session=session)


def get_units():
    units = get_all_units(session=session)
    unit_list = []
    for unit in units:
        unit_list.append(unit.label)
    return unit_list

def main() -> None:
    ...
    # recipe = recipe_lookup(1, session=session)
    # print(recipe.__dict__)
    # sample_recipe_ingredient = {
    #     "recipe_ingredient_id": 1,
    #     "recipe_id": 1,
    #     "ingredient_id": 1,
    #     "unit_id": 1,
    #     "amount": 2.0,
    #     "sort": 1
    # }
    # update_recipe_ingredient(sample_recipe_ingredient, session=session, engine=engine)
    # sample_recipe_params = {
    #     'name': 'Chicken n Cheese',
    #     'cook_time': '20 minutes',
    #     'servings': 1,
    #     'calories': 300,
    #     'instructions': "cook it\neat it",
    #     'meal_type': 'Breakfast'
    # }
    # edit_sample_recipe_params = {
    #     'recipe_id': 2,
    #     'name': 'Chicken n Cheese',
    #     'cook_time': '20 minutes',
    #     'servings': 4,
    #     'calories': 8000,
    #     'instructions': "cook it\neat it",
    #     'meal_type': 'Breakfast'
    # }
    # sample_ingredient_list = [
    #     {
    #         'label': 'chicken',
    #         'unit_id': '1',
    #         'amount': 1
    #     },
    #     {
    #         'label': 'Cheddar Cheese',
    #         'unit_id': '2',
    #         'amount': 10
    #     }
    # ]
    # edit_recipe(edit_sample_recipe_params, session=session, engine=engine)
    # sample_recipe = {
    #     'recipe_params': sample_recipe_params,
    #     'ingredients': sample_ingredient_list
    # }
    #
    # submit_new_recipe(sample_recipe)
    # recipe_list = get_all_recipes(session=session)
    # for r in recipe_list:
    #     print(r)

    # recipe = create_recipe("Chicken Parmesean", "1 hour", 1, 500, "Cook\nstuff",
    #                         session=session,
    #                         photo_url="https://assets.bonappetit.com/photos/5ea8f0df16738800085ad5d2/1:1/w_2560%2Cc_limit/Chicken-Parmesean-Recipe-Lede.jpg")
    # whole_unit = create_unit("whole", session=session)
    # oz_unit = create_unit("oz", session=session)
    # chicken_id = create_ingredient("Chicken", session=session)
    # parmesan_id = create_ingredient("Parmesean", session=session)
    # recipe_ingredient1 = create_recipe_ingredient(recipe, chicken_id, whole_unit, 1, 1, session=session)
    # recipe_ingredient2 = create_recipe_ingredient(recipe, parmesan_id, oz_unit, 5, 2, session=session)



if __name__ == '__main__':
    main()
