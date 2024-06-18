from flask import Flask, render_template, request, flash

import os
import db_interface
import db_interface as db


UPLOAD_FOLDER = '/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recipes", defaults={'sort_by': None})
@app.route("/recipes/<sort_by>")
def all_recipes(sort_by):
    recipes = []
    # print(sort_by)
    if sort_by:
        print(sort_by)
        recipe_list = db.meal_lookup(sort_by)
    else:
        # print("all")
        recipe_list = db.get_recipes()
    for r in recipe_list:
        recipe = {
            'recipe_id': r.recipe_id,
            'name': r.name,
            'cook_time': r.cook_time,
            'servings': r.servings,
            'calories': r.calories,
            'meal_type': r.meal_type,
            'user_id': r.user_id,
            'photo_url': r.photo_url
        }
        recipes.append(recipe)
        print(recipe)
    return render_template("all-recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
def selected_recipe(recipe_id):
    if request.method == "GET":

        recipe = db.get_recipe(recipe_id)
        print(recipe.__dict__)

        return render_template("recipe.html", recipe=recipe)

    elif request.method == "POST":
        ...


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        form = request.get_json()
        recipe_params = form["recipe_params"]
        ingredient_list = form['ingredients']
        print(recipe_params)
        print(ingredient_list)
        db_interface.submit_new_recipe(form)
    unit_list = db_interface.get_units()
    # print(unit_list)
    return render_template('upload-recipe.html', units=unit_list)


if __name__ == '__main__':
    app.run(debug=True)





#
# routes:
# home(/)
# all recipes(/recipes) GET
# single recipe(/recipe/<id>) GET, POST
# add recipe(/create_recipe) POST
# random recipe
# delete route

# connect front to back -> login stuff -> edit/delete stuff -> random recipe generation



