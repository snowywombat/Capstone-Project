from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from flask_wtf.csrf import generate_csrf, validate_csrf
from wtforms import ValidationError
from app.models import Recipe, db, Review, Kitchenware, Ingredient, Preparation
from ..forms.recipe_form import CreateRecipeForm, EditRecipeForm
from ..forms.review_form import CreateReviewForm, EditReviewForm
from .auth_routes import validation_errors_to_error_messages

recipe_routes = Blueprint('recipe', __name__)

@recipe_routes.route('/')
def get_all_recipes():
    allRecipes = Recipe.query.all()

    res = {
    "Recipes":[]
    }

    for recipe in allRecipes:
        data = recipe.to_dict()
        data.pop("user")
        data.pop("reviews")
        data.pop("kitchenwares")
        data.pop("preparations")
        data.pop("ingredients")
        res["Recipes"].append(data)

    return res

@recipe_routes.route('/<int:recipeId>')
def get_recipe_detail(recipeId):
    single_recipe = db.session.query(Recipe).get(int(recipeId))

    if not single_recipe:
        return {"message": "Recipe couldn't be found"}, 404

    data = single_recipe.to_dict()

    res = {
    "Recipes":[]
    }

    #get kitchenware out of recipe
    kitchenwareData = []
    for kitchenware in data["kitchenwares"]:
        kitchenwareDict = kitchenware.to_dict()
        kitchenwareDict.pop("recipe")
        kitchenwareData.append(kitchenwareDict)

    #get ingredients out of recipe
    ingredientData = []
    for ingredient in data["ingredients"]:
        ingredientDict = ingredient.to_dict()
        ingredientDict.pop("recipe")
        ingredientData.append(ingredientDict)

    #get preparation out of recipe
    preparationData = []
    for preparation in data["preparations"]:
        preparationDict = preparation.to_dict()
        preparationDict.pop("recipe")
        preparationData.append(preparationDict)

    recipe = {
        "id": data["id"],
        "userId": data["user_id"],
        "name": data["name"],
        "description": data["description"],
        "servingSize": data["servings_num"],
        "imgUrl": data["img_url"],
        "createdAt": data["created_at"],
        "user": {
            "id": data["user"].id,
            "firstName": data["user"].first_name,
            "lastName": data["user"].last_name,
            "email": data["user"].email,
            "username": data["user"].username
        },
        "kitchenware": kitchenwareData,
        "ingredients": ingredientData,
        "preparation": preparationData
    }

    res["Recipes"].append(recipe)
    return res


@recipe_routes.route('/', methods=["POST"])
@login_required
def create_recipe():
    user_id = current_user.id
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    servings_num = int(data.get('servings_num'))
    ingredients = data.get('ingredients')
    kitchenwares = data.get('kitchenwares')
    preparations = data.get('preparations')
    img_url = data.get('img_url')

    errors = {}

    if not name:
        errors["name"] = "Name is required"
    elif len(name) < 2 or len(name) > 50:
        errors["name"] = "Name must be more than 1 and less than 50 characters"

    if not description:
        errors["description"] = "Description is required"
    elif len(description) < 2 or len(description) > 200:
        errors["description"] = "Description must be more than 1 and less than 200 characters"

    if not servings_num:
        errors["servings_num"] = "Serving size is required"
    elif servings_num < 1 or servings_num > 100:
        errors["servings_num"] = "Serving size must be between 1 and 100."

    if not img_url:
        errors["img_url"] = "Image is required"
    elif len(img_url) < 2 or len(img_url) > 1000:
        errors["img_url"] = "Image url must be more than 1 and less than 1, 000 characters"

    if not ingredients:
        errors["ingredients"] = "Ingredients are required"

    if not kitchenwares:
        errors["kitchenwares"] = "Things you'll need are required"

    if not preparations:
        errors["preparations"] = "Instructions are required"

    for item in ingredients:

        amount = float(item["measurement_num"])

        if not item["ingredient"]:
            errors["item['ingredient']"] = "Ingredient is required"
        elif len(item["ingredient"]) < 2 or len(item["ingredient"]) > 100:
            errors["item['ingredient']"] = "Ingredient must be more than 1 and less than 100 characters"

        if not item["measurement_type"]:
            errors["item['measurment_type]"] = "Measurement type is required"
        elif len(item["measurement_type"]) < 2 or len(item["measurement_type"]) > 20:
            errors["item['measurement_type]"] = "Measurement type must be more than 1 and less than 20 characters"

        if not (amount):
            errors["amount"] = "Measurement amount is required"
        elif amount < 1.0 or amount > 10000.0:
            errors["amount"] = "Measurement number must be less than 10, 000"

    for item in kitchenwares:

        if not item["name"]:
            errors["item['name']"] = "Name of cookware is required"
        elif len(item["name"]) < 2 or len(item["name"]) > 50:
            errors["item['name']"] = "Name of things you'll need must be more than 1 and less than 20 characters"

    for item in preparations:

        if not item["description"]:
            errors["item['description']"] = "Preparation step is required"
        elif len(item["description"]) < 2 or len(item["description"]) > 200:
            errors["item['description]"] = "Preparation step must be more than 1 and less than 200 characters long"


    formatted_errors = [f"{key}: {value}" for key, value in errors.items()]

    if errors:
        return {"errors": formatted_errors}, 400


    csrf_token = request.cookies['csrf_token']

    if current_user.is_authenticated:
        newRecipe = Recipe(
            name= data["name"],
            description = data["description"],
            servings_num = data["servings_num"],
            img_url = data['img_url'],
            user_id = user_id
        )

        db.session.add(newRecipe)
        db.session.commit()

        ingredients = []
        for item in data["ingredients"]:
            newIngredient = Ingredient(
                measurement_num=item["measurement_num"],
                measurement_type=item["measurement_type"],
                ingredient=item["ingredient"],
                recipe_id = newRecipe.id,
            )
            db.session.add(newIngredient)
            ingredients.append(newIngredient)
            db.session.commit()


        kitchenwares = []
        for item in data["kitchenwares"]:
            newKitchenware = Kitchenware(
                name=item["name"],
                recipe_id = newRecipe.id
            )
            db.session.add(newKitchenware)
            kitchenwares.append(newKitchenware)
            db.session.commit()


        preparations = []
        for item in data["preparations"]:
            newPreparation = Preparation(
                description=item["description"],
                recipe_id = newRecipe.id
            )
            db.session.add(newPreparation)
            preparations.append(newPreparation)
            db.session.commit()

        allRecipes = Recipe.query.all()


        return {
            "id": allRecipes[len(allRecipes)-1].id,
            "user_id": user_id,
            "name": data["name"],
            "description": data["description"],
            "servings_num": data["servings_num"],
            "img_url": data["img_url"],
            "created_at": allRecipes[len(allRecipes)-1].created_at,
            "ingredient": data["ingredients"],
            "kitchenwares": data["kitchenwares"],
            "preparation": data["preparations"],

        }, 201


    else:
        return jsonify(message='You are not authorized to access this resource'), 401



@recipe_routes.route('/<int:recipeId>', methods=["PUT"])
@login_required
def update_recipe(recipeId):
    #find recipe
    edit_recipe = db.session.query(Recipe).get(int(recipeId))
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    servings_num = int(data.get('servings_num'))
    ingredients = data.get('ingredients')
    kitchenwares = data.get('kitchenwares')
    preparations = data.get('preparations')
    img_url = data.get('img_url')

    errors = {}

    if not name:
        errors["name"] = "Name is required"
    elif len(name) < 2 or len(name) > 50:
        errors["name"] = "Name must be more than 1 and less than 50 characters"

    if not description:
        errors["description"] = "Description is required"
    elif len(description) < 2 or len(description) > 200:
        errors["description"] = "Description must be more than 1 and less than 200 characters"

    if not servings_num:
        errors["servings_num"] = "Serving size is required"
    elif servings_num < 1 or servings_num > 100:
        errors["servings_num"] = "Serving size must be between 1 and 100."

    if not img_url:
        errors["img_url"] = "Image is required"
    elif len(img_url) < 2 or len(img_url) > 1000:
        errors["img_url"] = "Image url must be more than 1 and less than 1, 000 characters"

    if not ingredients:
        errors["ingredients"] = "Ingredients are required"

    if not kitchenwares:
        errors["kitchenwares"] = "Things you'll need are required"

    if not preparations:
        errors["preparations"] = "Instructions are required"

    for item in ingredients:

        amount = float(item["measurement_num"])

        if not item["ingredient"]:
            errors["item['ingredient']"] = "Ingredient is required"
        elif len(item["ingredient"]) < 2 or len(item["ingredient"]) > 100:
            errors["item['ingredient']"] = "Ingredient must be more than 1 and less than 100 characters"

        if not item["measurement_type"]:
            errors["item['measurment_type]"] = "Measurement type is required"
        elif len(item["measurement_type"]) < 2 or len(item["measurement_type"]) > 20:
            errors["item['measurement_type]"] = "Measurement type must be more than 1 and less than 20 characters"

        if not (amount):
            errors["amount"] = "Measurement amount is required"
        elif amount < 1.0 or amount > 10000.0:
            errors["amount"] = "Measurement number must be less than 10, 000"

    for item in kitchenwares:

        if not item["name"]:
            errors["item['name']"] = "Name of cookware is required"
        elif len(item["name"]) < 2 or len(item["name"]) > 50:
            errors["item['name']"] = "Name of things you'll need must be more than 1 and less than 20 characters"

    for item in preparations:

        if not item["description"]:
            errors["item['description']"] = "Preparation step is required"
        elif len(item["description"]) < 2 or len(item["description"]) > 200:
            errors["item['description]"] = "Preparation step must be more than 1 and less than 200 characters long"


    formatted_errors = [f"{key}: {value}" for key, value in errors.items()]

    if errors:
        return {"errors": formatted_errors}, 400


    csrf_token = request.cookies['csrf_token']

    if not edit_recipe:
        return {"message": "Recipe couldn't be found"}, 404

    if edit_recipe.user_id != current_user.id:
        return {
            'errors': ['Unauthorized']
        }, 401


    if current_user.is_authenticated:
        edit_recipe.name = data["name"]
        edit_recipe.description = data["description"]
        edit_recipe.servings_num = data["servings_num"]
        edit_recipe.img_url = data["img_url"]
        for item in edit_recipe.ingredients:
            for ele in data["ingredients"]:
                item.ingredient = ele["ingredient"]
                item.measurement_num = ele["measurement_num"]
                item.measurement_type = ele["measurement_type"]
        for item in edit_recipe.kitchenwares:
            for ele in data["kitchenwares"]:
                item.name = ele["name"]
        for item in edit_recipe.preparations:
            for ele in data["preparations"]:
                item.description = ele["description"]

        db.session.commit()

        return {
            "id": edit_recipe.id,
            "user_id": edit_recipe.user_id,
            "name": data["name"],
            "description": data["description"],
            "servings_num": data["servings_num"],
            "img_url": data["img_url"],
            "ingredients": data["ingredients"],
            "kitchenwares": data["kitchenwares"],
            "preparations": data["preparations"],
            "created_at": edit_recipe.created_at
        }, 201

    else:
        return jsonify(message='You are not authorized to access this resource'), 401


@recipe_routes.route('/<int:recipeId>', methods=["DELETE"])
@login_required
def delete_recipe(recipeId):
    #find recipe
    delete_recipe = db.session.query(Recipe).get(int(recipeId))

    if not delete_recipe:
      return {"message": "Recipe couldn't be found"}, 404

    if delete_recipe.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    db.session.delete(delete_recipe)
    db.session.commit()

    return {"message": "Successfully deleted"}



@recipe_routes.route('/<int:recipeId>/reviews')
def get_all_reviews(recipeId):
    single_recipe = db.session.query(Recipe).get(int(recipeId))
    all_reviews = Review.query.filter_by(recipe_id=single_recipe.id).all()

    if not single_recipe:
        return {"message": "Recipe couldn't be found"}, 404

    res = {
    "Reviews":[]
    }

    for review in all_reviews:
        data = review.to_dict()
        data["user"] = review.user.to_dict()
        data.pop("recipe")
        res["Reviews"].append(data)

    return res


@recipe_routes.route('/<int:recipeId>/reviews',  methods=["POST"])
@login_required
def create_review(recipeId):
    user_id = current_user.id

    recipe = Recipe.query.get(recipeId)

    if recipe is None:
        return {
        "message": "Recipe couldn't be found",
        "statusCode": 404
      }, 404

    form = CreateReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        print(data, 'this is data')
        print(Review, 'this is the review')
        newReview = Review (
            review = data["review"],
            stars = data["stars"],
            location = data["location"],
            user_id = user_id,
            recipe_id = int(recipeId)
        )

        print(newReview, 'this is newReview')

        db.session.add(newReview)
        db.session.commit()

        allReviews = Review.query.all()

        return {
            "id": allReviews[len(allReviews)-1].id,
            "user_id": user_id,
            "recipe_id": recipeId,
            "review": data["review"],
            "stars": data["stars"],
            "location": data["location"],
            "user": {
                "id": allReviews[len(allReviews)-1].user.id,
                "firstName": allReviews[len(allReviews)-1].user.first_name,
                "lastName": allReviews[len(allReviews)-1].user.last_name
            },
            "createdAt": allReviews[len(allReviews)-1].created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400
