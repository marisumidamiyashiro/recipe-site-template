from flask import (Flask, render_template, request, flash, redirect,
                   url_for, Response, session)
from flask_login import LoginManager
import os
import db_interface as db

SECRET_KEY = '6cc3494a062a8393a19a7c060ba7a743335ceb7fc44ae87f76358c5846bbe637'

UPLOAD_FOLDER = '/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_user(user_id)

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
        # print(recipe_params)
        # print(ingredient_list)
        recipe_id = db.submit_new_recipe(form)
        print(recipe_id)
        response = Response("{'a':'b'}", status=201, mimetype='application/json')

        response.data = f"{recipe_id}"
        return response
    else:
        unit_list = db.get_units()
        # print(unit_list)
        return render_template('upload-recipe.html', units=unit_list)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        print(request.form)
        return redirect(url_for('home'))


@app.route('/signup', methods=["POST"])
def signup():
    form = request.form
    print(f"{form['new_username']}\n{form['email']}\n{form['new_password']}")
    result = db.create_new_user(form['new_username'],form['email'],form['new_password'])
    if result == -1:
        print(db.user_login("dawgnukem", "12345"))
    return redirect(url_for('home'))


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



