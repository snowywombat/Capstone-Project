from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from flask_wtf.csrf import generate_csrf, validate_csrf
from wtforms import ValidationError
from app.models import Recipe, db, Review, Tag, Kitchenware, Ingredient, Preparation
from ..forms.recipe_form import CreateRecipeForm, EditRecipeForm
from ..forms.review_form import CreateReviewForm
from ..forms.tag_form import CreateTagForm
from .auth_routes import validation_errors_to_error_messages
import uuid
import json
import decimal

recipe_routes = Blueprint('recipe', __name__)

@recipe_routes.route('/')
def get_all_recipes():
    allRecipes = Recipe.query.all()

    res = {
    "Recipes":[]
    }

    for recipe in allRecipes:
        data = recipe.to_dict()

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

        data.pop("user")
        data.pop("reviews")
        data.pop("tags")
        data.pop("kitchenwares")
        data.pop("preparations")
        data.pop("ingredients")
        res["Recipes"].append(data)

    return res

@recipe_routes.route('/<int:recipeId>')
def get_recipe_detail(recipeId):
    single_recipe = db.session.query(Recipe).get(int(recipeId))
    all_reviews = Review.query.filter_by(recipe_id=single_recipe.id).all()
    all_tags = Tag.query.filter_by(recipe_id=single_recipe.id).all()

    if not single_recipe:
        return {"message": "Recipe couldn't be found"}, 404

    data = single_recipe.to_dict()

    res = {
    "Recipes":[]
    }

    #get reviews out of recipe
    reviewsData = []
    for review in all_reviews:
        reviewDict = review.to_dict()
        reviewDict.pop("recipe")
        reviewDict.pop("user")
        reviewsData.append(reviewDict)


    #get tags out of recipe
    tagsData = []
    for tag in all_tags:
        tagDict = tag.to_dict()
        tagDict.pop("recipe")
        tagDict.pop("user")
        tagsData.append(tagDict)

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
        "user_id": data["user_id"],
        "name": data["name"],
        "description": data["description"],
        "servingSize": data["servings_num"],
        "img_url": data["img_url"],
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
        "preparation": preparationData,
        "reviews": reviewsData,
        "tags": tagsData

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
    elif len(name) < 2 or len(name) > 100:
        errors["name"] = "Name must be between 2 and 100 characters"

    if not description:
        errors["description"] = "Description is required"
    elif len(description) < 2 or len(description) > 500:
        errors["description"] = "Description must between 2 and 500 characters"

    if not servings_num:
        errors["servings_num"] = "Serving size is required"
    elif servings_num < 1 or servings_num > 100:
        errors["servings_num"] = "Serving size must be between 1 and 100."

    if not img_url:
        errors["img_url"] = "Image is required"
    elif len(img_url) < 13 or len(img_url) > 1000:
        errors["img_url"] = "Image url must be between 13 and 1, 000 characters"
    elif "http://" not in img_url and "https://" not in img_url:
        errors["img_url"] = "Image url must include http:// or https://"
    elif ".jpeg" not in img_url and ".jpg" not in img_url and ".png" not in img_url and ".gif" not in img_url and ".JPEG" not in img_url and ".JPG" not in img_url and ".PNG" not in img_url and ".GIF" not in img_url:
        errors["img_url"] = "Image url must end in .jpg, .jpeg, .png, or .gif"

    if not ingredients:
        errors["ingredients"] = "Ingredients are required"

    if not kitchenwares:
        errors["kitchenwares"] = "Things you'll need are required"

    if not preparations:
        errors["preparations"] = "Instructions are required"

    for item in ingredients:

        amount = decimal.Decimal(item["measurement_num"])

        if not item["ingredient"]:
            errors["item['ingredient']"] = "Ingredient is required"
        elif len(item["ingredient"]) < 2 or len(item["ingredient"]) > 100:
            errors["item['ingredient']"] = "Ingredient item must be between 2 and 100 characters"

        if not item["measurement_type"]:
            errors["item['measurment_type]"] = "Measurement type is required"
        elif len(item["measurement_type"]) < 2 or len(item["measurement_type"]) > 20:
            errors["item['measurement_type]"] = "Ingredient measurement type must be between 2 and 20 characters"

        if amount is None:
            errors["amount"] = "Measurement amount is required"
        elif amount < 0.001 or amount > 10000.0:
            errors["amount"] = "Ingredient measurement number must be less than 10, 000"

    for item in kitchenwares:

        if not item["name"]:
            errors["item['name']"] = "Name of cookware is required"
        elif len(item["name"]) < 2 or len(item["name"]) > 50:
            errors["item['name']"] = "Things you'll need item must be between 2 and 50 characters"

    for item in preparations:

        if not item["description"]:
            errors["item['description']"] = "Preparation step is required"
        elif len(item["description"]) < 2 or len(item["description"]) > 150:
            errors["item['description]"] = "Instruction step must be between 2 and 150 characters"


    formatted_errors = [f"{key}: {value}" for key, value in errors.items()]

    if errors:
        return {"errors": formatted_errors}, 400


    csrf_token = request.cookies['csrf_token']

    allRecipes = Recipe.query.all()
    allIngredients = Ingredient.query.all()
    allKitchenwares = Kitchenware.query.all()
    allPreparations = Preparation.query.all()

    if current_user.is_authenticated:
        newRecipe = Recipe(
            name = data["name"],
            description = data["description"],
            servings_num = data["servings_num"],
            img_url = data["img_url"],
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



        kitchenwares = []
        for item in data["kitchenwares"]:
            newKitchenware = Kitchenware(
                name=item["name"],
                recipe_id = newRecipe.id,
            )
            db.session.add(newKitchenware)
            kitchenwares.append(newKitchenware)



        preparations = []
        for item in data["preparations"]:
            newPreparation = Preparation(
                description=item["description"],
                recipe_id = newRecipe.id,
            )
            db.session.add(newPreparation)
            preparations.append(newPreparation)

        db.session.commit()

        time = Recipe.query.order_by(Recipe.created_at.asc()).first().created_at
        newRecipe.created_at = time

        list(newRecipe.ingredients)
        list(newRecipe.preparations)
        list(newRecipe.kitchenwares)

        recipe_dict = newRecipe.to_dict()
        del recipe_dict['reviews']
        del recipe_dict['tags']

        recipe_dict["created_at"] = str(time)

        recipe_dict["user"] = {
            "id": newRecipe.user.id,
            "firstName": newRecipe.user.first_name,
            "lastName": newRecipe.user.last_name
        }

        newKitchenArray = []

        for item in newRecipe.kitchenwares:
            item = {
                "id": item.id,
                "name": item.name,
                "recipe_id": item.recipe_id
            }
            newKitchenArray.append(item)

        recipe_dict["kitchenwares"] = newKitchenArray


        newPrepArray = []

        for item in newRecipe.preparations:
            item = {
                "id": item.id,
                "description": item.description,
                "recipe_id": item.recipe_id
            }
            newPrepArray.append(item)

        recipe_dict["preparations"] = newPrepArray


        newIngredientArray = []

        for item in newRecipe.ingredients:
            item = {
                "id": item.id,
                "measurement_num": float(item.measurement_num),
                "measurement_type": item.measurement_type,
                "ingredient": item.ingredient,
                "recipe_id": item.recipe_id
            }
            newIngredientArray.append(item)


        recipe_dict["ingredients"] = newIngredientArray


        return json.dumps(recipe_dict)

    else:
        return jsonify(message='You are not authorized to access this resource'), 401



@recipe_routes.route('/<int:recipeId>', methods=["PUT"])
@login_required
def update_recipe(recipeId):
    edit_recipe = db.session.query(Recipe).get(int(recipeId))
    edit_ingredient = db.session.query(Ingredient).filter_by(recipe_id=recipeId).all()
    edit_kitchenware = db.session.query(Kitchenware).filter_by(recipe_id=recipeId).all()
    edit_preparation = db.session.query(Preparation).filter_by(recipe_id=recipeId).all()

    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    servings_num = int(data.get('servings_num'))
    ingredients = data.get('ingredients')
    kitchenwares = data.get('kitchenwares')
    preparations = data.get('preparations')
    img_url = data.get('img_url')
    newKitchenwares = data.get('newKitchenware')
    newIngredients = data.get('newIngredient')
    newPreparations = data.get('newPreparation')

    errors = {}

    if not name:
        errors["name"] = "Name is required"
    elif len(name) < 2 or len(name) > 100:
        errors["name"] = "Name must be between 2 and 100 characters"

    if not description:
        errors["description"] = "Description is required"
    elif len(description) < 2 or len(description) > 500:
        errors["description"] = "Description must between 2 and 500 characters"

    if not servings_num:
        errors["servings_num"] = "Serving size is required"
    elif servings_num < 1 or servings_num > 100:
        errors["servings_num"] = "Serving size must be between 1 and 100."

    if not img_url:
        errors["img_url"] = "Image is required"
    elif len(img_url) < 13 or len(img_url) > 1000:
        errors["img_url"] = "Image url must be between 13 and 1, 000 characters"
    elif "http://" not in img_url and "https://" not in img_url:
        errors["img_url"] = "Image url must include http:// or https://"
    elif ".jpeg" not in img_url and ".jpg" not in img_url and ".png" not in img_url and ".gif" not in img_url and ".JPEG" not in img_url and ".JPG" not in img_url and ".PNG" not in img_url and ".GIF" not in img_url:
        errors["img_url"] = "Image url must end in .jpg, .jpeg, .png, or .gif"

    if not ingredients:
        errors["ingredients"] = "Ingredients are required"

    if not kitchenwares:
        errors["kitchenwares"] = "Things you'll need are required"

    if not preparations:
        errors["preparations"] = "Instructions are required"

    for item in ingredients:

        amount = decimal.Decimal(item["measurement_num"])

        if not item["ingredient"]:
            errors["item['ingredient']"] = "Ingredient is required"
        elif len(item["ingredient"]) < 2 or len(item["ingredient"]) > 100:
            errors["item['ingredient']"] = "Ingredient item must be between 2 and 100 characters"

        if not item["measurement_type"]:
            errors["item['measurment_type]"] = "Measurement type is required"
        elif len(item["measurement_type"]) < 2 or len(item["measurement_type"]) > 20:
            errors["item['measurement_type]"] = "Ingredient measurement type must be between 2 and 20 characters"

        if amount is None:
            errors["amount"] = "Measurement amount is required"
        elif amount < 0.001 or amount > 10000.0:
            errors["amount"] = "Ingredient measurement number must be less than 10, 000"

    for item in kitchenwares:

        if not item["name"]:
            errors["item['name']"] = "Name of cookware is required"
        elif len(item["name"]) < 2 or len(item["name"]) > 50:
            errors["item['name']"] = "Things you'll need item must be between 2 and 50 characters"

    for item in preparations:

        if not item["description"]:
            errors["item['description']"] = "Preparation step is required"
        elif len(item["description"]) < 2 or len(item["description"]) > 150:
            errors["item['description]"] = "Instruction step must be between 2 and 150 characters"


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

        #creates new kitchenwares
        for item in newKitchenwares:
            newKitchenware = Kitchenware(
                name = item["name"],
                recipe_id = edit_recipe.id,
            )
            db.session.add(newKitchenware)
        db.session.commit()

        #creates new ingredients
        for item in newIngredients:
            newIngredient = Ingredient(
                measurement_num = item["measurement_num"],
                measurement_type = item["measurement_type"],
                ingredient = item["ingredient"],
                recipe_id = edit_recipe.id,
            )
            db.session.add(newIngredient)
        db.session.commit()

        #creates new preparations
        for item in newPreparations:
            newPreparation = Preparation(
                description = item["description"],
                recipe_id = edit_recipe.id,
            )
            db.session.add(newPreparation)
        db.session.commit()


        ingredients = []
        for ele in data["ingredients"]:
            # Check if a ingredient with same name already exists
            for item in edit_ingredient:
                if item.id == ele["id"]:
                    # If exists, update its info
                    item.measurement_num = ele["measurement_num"]
                    item.measurement_type = ele["measurement_type"]
                    item.ingredient = ele["ingredient"]

        # Update ingredients and commit
        db.session.commit()


        kitchenwares = []
        for ele in data["kitchenwares"]:
            # Check if a kitchenware with same name already exists
            for item in edit_kitchenware:
                if item.id == ele["id"]:
                    # If exists, update its info
                    item.name = ele["name"]

        # Update kitchenwares and commit
        db.session.commit()


        preparations = []
        for ele in data["preparations"]:
            # Check if a preparation with same name already exists
            for item in edit_preparation:
                if item.id == ele["id"]:
                    # If exists, update its info
                    item.description = ele["description"]

        # Update preparations and commit
        db.session.commit()


        time = Recipe.query.order_by(Recipe.created_at.asc()).first().created_at
        edit_recipe.created_at = time


        recipe_dict = edit_recipe.to_dict()
        del recipe_dict['reviews']
        del recipe_dict['tags']
        recipe_dict["created_at"] = str(time)

        recipe_dict["user"] = {
            "id": edit_recipe.user.id,
            "firstName": edit_recipe.user.first_name,
            "lastName": edit_recipe.user.last_name
        }

        newKitchenArray = []
        for item in edit_recipe.kitchenwares:
            item = {
                "id": item.id,
                "name": item.name,
                "recipe_id": item.recipe_id,

            }
            newKitchenArray.append(item)
        recipe_dict["kitchenwares"] = newKitchenArray


        newPrepArray = []
        for item in edit_recipe.preparations:
            item = {
                "id": item.id,
                "description": item.description,
                "recipe_id": item.recipe_id
            }
            newPrepArray.append(item)
        recipe_dict["preparations"] = newPrepArray


        newIngredientArray = []
        for item in edit_recipe.ingredients:
            item = {
                "id": item.id,
                "measurement_num": float(item.measurement_num),
                "measurement_type": item.measurement_type,
                "ingredient": item.ingredient,
                "recipe_id": item.recipe_id
            }
            newIngredientArray.append(item)
        recipe_dict["ingredients"] = newIngredientArray


        #creating new key called newKitchenwares
        recipe_dict["newKitchenwares"] = newKitchenwares

        #creating new key called newIngredients
        recipe_dict["newIngredients"] = newIngredients

        #creating new key called newPreparations
        recipe_dict["newPreparations"] = newPreparations

        db.session.add(edit_recipe)
        db.session.commit()


        return json.dumps(recipe_dict)


    else:
        return jsonify(message='You are not authorized to access this resource'), 401


@recipe_routes.route('/<int:recipeId>', methods=["DELETE"])
@login_required
def delete_recipe(recipeId):
    #find recipe
    delete_recipe = db.session.query(Recipe).get(int(recipeId))
    delete_ingredient = db.session.query(Ingredient).get(int(recipeId))
    delete_kitchenware = db.session.query(Kitchenware).get(int(recipeId))
    delete_preparation = db.session.query(Preparation).get(int(recipeId))

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
            "user": {
                "id": allReviews[len(allReviews)-1].user.id,
                "firstName": allReviews[len(allReviews)-1].user.first_name,
                "lastName": allReviews[len(allReviews)-1].user.last_name
            },
            "createdAt": allReviews[len(allReviews)-1].created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

@recipe_routes.route('/<int:recipeId>/tags')
def get_all_tags(recipeId):
    single_recipe = db.session.query(Recipe).get(int(recipeId))
    all_tags = Tag.query.filter_by(recipe_id=single_recipe.id).all()

    if not single_recipe:
        return {"message": "Recipe couldn't be found"}, 404

    res = {
    "Tags":[]
    }

    for tag in all_tags:
        data = tag.to_dict()
        data["user"] = tag.user.to_dict()
        data.pop("recipe")
        res["Tags"].append(data)

    return res


@recipe_routes.route('/<int:recipeId>/tags',  methods=["POST"])
@login_required
def create_tag(recipeId):
    user_id = current_user.id

    recipe = Recipe.query.get(recipeId)

    if recipe is None:
        return {
        "message": "Recipe couldn't be found",
        "statusCode": 404
      }, 404

    form = CreateTagForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        newTag = Tag (
            tag_name = data["tag_name"],
            user_id = user_id,
            recipe_id = int(recipeId)
        )

        db.session.add(newTag)
        db.session.commit()

        allTags = Tag.query.all()

        return {
            "id": allTags[len(allTags)-1].id,
            "user_id": user_id,
            "recipe_id": recipeId,
            "tag_name": data["tag_name"],
            "user": {
                "id": allTags[len(allTags)-1].user.id,
                "firstName": allTags[len(allTags)-1].user.first_name,
                "lastName": allTags[len(allTags)-1].user.last_name
            },
            "createdAt": allTags[len(allTags)-1].created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400
