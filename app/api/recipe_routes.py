from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
import pandas as pd
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


    return {
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
            "lastName": data["user"].last_name
        },
        "kitchenware": kitchenwareData,
        "ingredients": ingredientData,
        "preparation": preparationData
    }

@recipe_routes.route('/', methods=["POST"])
@login_required
def create_recipe():
    user_id = current_user.id
    print('this is the curent user', current_user)
    data = request.get_json()
    print('data', data)

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

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@recipe_routes.route('/<int:recipeId>', methods=["PUT"])
@login_required
def update_recipe(recipeId):
    #find recipe
    edit_recipe = db.session.query(Recipe).get(int(recipeId))

    if not edit_recipe:
        return {"message": "Recipe couldn't be found"}, 404

    if edit_recipe.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    form = EditRecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data

        edit_recipe.name = data["name"]
        edit_recipe.description = data["description"]
        edit_recipe.servings_num = data["servings_num"]
        edit_recipe.img_url = data["img_url"]

        db.session.commit()

        return {
            "id": edit_recipe.id,
            "user_id": edit_recipe.user_id,
            "name": data["name"],
            "description": data["description"],
            "servings_num": data["servings_num"],
            "img_url": data["img_url"],
            "created_at": edit_recipe.created_at
        }
    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

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
        data.pop("recipe")
        data.pop("user")
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
        newReview = Review (
            review = data["review"],
            stars = data["stars"],
            location = data["location"],
            user_id = user_id,
            recipe_id = int(recipeId)
        )

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
            "createdAt": allReviews[len(allReviews)-1].created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400
