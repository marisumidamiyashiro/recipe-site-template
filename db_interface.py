from sqlalchemy import create_engine
import random
from db_classes.db import bind_engine
from db_classes.recipe_db import (create_recipe, delete_recipe, recipe_lookup, edit_recipe, get_all_recipes,
                                  meal_type_lookup)
from db_classes.ingredient_db import create_ingredient
from db_classes.recipe_ingredient_db import (create_recipe_ingredient, delete_recipe_ingredients)
from db_classes.unit_db import create_unit, get_unit, get_all_units
from db_classes.user_db import get_user_by_id, create_user, login
engine = create_engine("sqlite:///recipesite.db")
session = bind_engine(engine)
SQLALCH_INSTANCE = '_sa_instance_state'

# recipe.get_all_recipes2(session)


def get_user(user_id):
    return get_user_by_id(user_id, session=session)


def user_login(username, password):
    return login(username, password, session=session)


def create_new_user(username, email, password):
    return create_user(username, email, password, session=session)


def create_dummy_recipe():

    units = ["teaspoons", "tablespoons", "cups", "ounces", "pints", "gallons", 'lbs', "cloves", "cans", "none"]
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
    # print(f"recipe params: {recipe_params}")
    recipe_id = create_recipe(**recipe_params, session=session)
    # print(f"recipe_id: {recipe_id}")
    i = 1
    for ingredient in recipe["ingredients"]:
        ingredient_id = create_ingredient(ingredient["label"], session=session)
        # print(f"ingredient id: {ingredient_id}")
        # print(f"unit id: {ingredient["unit"]}")
        # print(f"amount: {ingredient["amount"]}")
        # print(f"sort: {i}")
        create_recipe_ingredient(recipe_id, ingredient_id, ingredient["unit"], ingredient["amount"], i,
                                 session=session)
        i += 1
    return recipe_id


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
    return units


def compare_ingredient_lists(ingredient_list, ingredient_tuples):

    for ingredient in ingredient_tuples:
        ingredient_list = compare_ingredients(ingredient_list, ingredient)

    return ingredient_list


def compare_ingredients(ingredient_list, ingredient_tuple):
    found = False
    for index, ingredient in enumerate(ingredient_list):
        if ingredient[0] == ingredient_tuple[0]:
            if ingredient[2] == ingredient_tuple[2]:
                new_touple = (ingredient[0], ingredient[1]+ingredient_tuple[1], ingredient[2])
                ingredient_list[index] = new_touple
            else:
                ingredient_list.insert(index,ingredient_tuple)
            found = True
    if not found:
        ingredient_list.append(ingredient_tuple)
    return ingredient_list


def create_random_list(meal_type, amount, userid=-1):
    if userid != -1:
        pass
    else:
        recipes = [r for r in meal_lookup(meal_type)]

        if len(recipes) < amount:
            amount = len(recipes)
        random_recipes = random.sample(recipes, amount)
        print("Recipes to combine:")
        for r in random_recipes:
            print(f"{r.recipe_id}. {r.name}:")
        print("\n")
        finalized_list = []
        combined_ingredients = []
        for r in random_recipes:
            recipe = get_recipe(r.recipe_id)
            del recipe.__dict__['_sa_instance_state']
            # print(recipe.__dict__)
            converted_recipe = recipe.__dict__
            finalized_list.append(converted_recipe)

            if len(combined_ingredients) == 0:
                combined_ingredients = converted_recipe["ingredients"]

            else:
                combined_ingredients = compare_ingredient_lists(combined_ingredients, converted_recipe["ingredients"])
        print(f"final_list: {combined_ingredients}")
        recipe_final = [finalized_list, combined_ingredients]
        return recipe_final


def main() -> None:
    # recipes = create_random_list("Dinner", 5)
    # for r in recipes[0]:
    #     print(r)
    # print(recipes[1])
    create_dummy_recipe()
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
    ...


if __name__ == '__main__':
    main()
