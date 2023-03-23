from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from flask_wtf.csrf import generate_csrf, validate_csrf
from wtforms import ValidationError
from app.models import Recipe, db, Review, Kitchenware, Ingredient, Preparation
from ..forms.recipe_form import CreateRecipeForm, EditRecipeForm
from ..forms.review_form import CreateReviewForm, EditReviewForm
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
        "preparation": preparationData
    }

    res["Recipes"].append(recipe)
    return res


@recipe_routes.route('/', methods=["POST"])
@login_required
def create_recipe():
    user_id = current_user.id
    data = request.get_json()
    print(data, 'pink unicorns')

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

        amount = item["measurement_num"]

        if not item["ingredient"]:
            errors["item['ingredient']"] = "Ingredient is required"
        elif len(item["ingredient"]) < 2 or len(item["ingredient"]) > 100:
            errors["item['ingredient']"] = "Ingredient must be more than 1 and less than 100 characters"

        if not item["measurement_type"]:
            errors["item['measurment_type]"] = "Measurement type is required"
        elif len(item["measurement_type"]) < 2 or len(item["measurement_type"]) > 20:
            errors["item['measurement_type]"] = "Measurement type must be more than 1 and less than 20 characters"

        if amount is None:
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

    allRecipes = Recipe.query.all()
    print(allRecipes, 'allRecipes boom')
    allIngredients = Ingredient.query.all()
    allKitchenwares = Kitchenware.query.all()
    allPreparations = Preparation.query.all()
    print(allIngredients[len(allIngredients) - 1].id)
    print(allKitchenwares[len(allKitchenwares) - 1].id + 1)

    print(data["ingredients"], 'coconut')

    if current_user.is_authenticated:
        newRecipe = Recipe(
            name = data["name"],
            description = data["description"],
            servings_num = data["servings_num"],
            img_url = data["img_url"],
            user_id = user_id
        )

        print(newRecipe, 'spotify')
        print(newRecipe.to_dict(), 'julep')

        db.session.add(newRecipe)
        db.session.commit()

        print(newRecipe.to_dict(), 'mint')

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

        recipe_dict["created_at"] = str(time)

        recipe_dict["user"] = {
            "id": newRecipe.user.id,
            "firstName": newRecipe.user.first_name,
            "lastName": newRecipe.user.last_name
        }

        print(recipe_dict["kitchenwares"], 'blank')

        newKitchenArray = []

        for item in newRecipe.kitchenwares:
            print(item.to_dict(), 'slack')
            item = {
                "id": item.id,
                "name": item.name,
                "recipe_id": item.recipe_id
            }
            print(item, "cookie")
            newKitchenArray.append(item)


        print(newKitchenArray, "tortilla")
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

        amount = decimal.Decimal(item["measurement_num"])

        if not item["ingredient"]:
            errors["item['ingredient']"] = "Ingredient is required"
        elif len(item["ingredient"]) < 2 or len(item["ingredient"]) > 100:
            errors["item['ingredient']"] = "Ingredient must be more than 1 and less than 100 characters"

        if not item["measurement_type"]:
            errors["item['measurment_type]"] = "Measurement type is required"
        elif len(item["measurement_type"]) < 2 or len(item["measurement_type"]) > 20:
            errors["item['measurement_type]"] = "Measurement type must be more than 1 and less than 20 characters"

        if amount is None:
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

    # allIngredients = Ingredient.query.all()
    # allKitchenwares = Kitchenware.query.all()
    # allPreparations = Preparation.query.all()


    if current_user.is_authenticated:

        edit_recipe.name = data["name"]
        edit_recipe.description = data["description"]
        edit_recipe.servings_num = data["servings_num"]
        edit_recipe.img_url = data["img_url"]

        # ingredients = []
        # for item in edit_recipe.ingredients:
        #     for ele in data["ingredients"]:
        #         item.ingredient = ele["ingredient"]
        #         item.measurement_num = ele["measurement_num"]
        #         item.measurement_type = ele["measurement_type"]
        #     db.session.add(item)
        #     ingredients.append(item)


        # kitchenwares = []
        # print(edit_recipe.kitchenwares, 'stars')
        # for item in edit_recipe.kitchenwares:
        #     for ele in data["kitchenwares"]:
        #         item.name = ele["name"]
        #     db.session.add(item)
        #     kitchenwares.append(item)


        ingredients = []
        for item, ele in zip(edit_recipe.ingredients, data["ingredients"]):
            item.ingredient = ele["ingredient"]
            item.measurement_num = ele["measurement_num"]
            item.measurement_type = ele["measurement_type"]
            item.recipe_id = edit_recipe.id
            db.session.add(item)
            ingredients.append(item)
        edit_recipe.ingredients = ingredients

        # kitchenwaresLst = []
        # for item in edit_recipe.kitchenwares:
        #     for ele in data["kitchenwares"]:
        #         editKitchenwares = Kitchenware(
        #             name = ele["name"],
        #             recipe_id = edit_recipe.id,
        #         )

        #         db.session.add(editKitchenwares)
        #         kitchenwaresLst.append(editKitchenwares)


        # edit_recipe.kitchenwares = kitchenwaresLst
        # db.session.commit()


        kitchenwares = []
        for ele in data["kitchenwares"]:
            print(ele, 'ele in kitchenwares')
            # Check if a kitchenware with same name already exists
            existing_item = Kitchenware.query.filter_by(recipe_id=edit_recipe.id).first()
            print(existing_item, 'existing item')
            if existing_item:
                print('it is hitting the if statement **************')

                # If exists, update its info
                existing_item.name = ele["name"]

            else:
                # If it doesn't exist, add new kitchenware
                print('it is hitting the else statement')
                new_item = Kitchenware(
                    name=ele["name"],
                    recipe_id=edit_recipe.id,
                )

                db.session.add(new_item)
                kitchenwares.append(new_item)

        # Update kitchenwares and commit
        print(kitchenwares, 'the kitchenwares list')
        # edit_recipe.kitchenwares = kitchenwares
        for item in kitchenwares:
            print(item, 'this is the item')
            print(item.to_dict(), 'view item')

        print(edit_recipe.kitchenwares, 'edit recipe kitchenwares')
        db.session.commit()


        preparations = []
        for item, ele in zip(edit_recipe.preparations, data["preparations"]):
            item.description = ele["description"]
            item.recipe_id = edit_recipe.id
            db.session.add(item)
            preparations.append(item)

        edit_recipe.preparations = preparations
        db.session.commit()


        time = Recipe.query.order_by(Recipe.created_at.asc()).first().created_at
        edit_recipe.created_at = time

        print(edit_recipe.to_dict(), 'bread')

        recipe_dict = edit_recipe.to_dict()
        del recipe_dict['reviews']
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


        db.session.add(edit_recipe)
        db.session.commit()

        print(edit_recipe.kitchenwares, 'pineapple pudding')


        return json.dumps(recipe_dict)


        # return {
        #     "id": edit_recipe.id,
        #     "user_id": edit_recipe.user_id,
        #     "name": data["name"],
        #     "description": data["description"],
        #     "servings_num": data["servings_num"],
        #     "img_url": data["img_url"],
        #     "ingredients": data["ingredients"],
        #     "kitchenwares": data["kitchenwares"],
        #     "preparations": data["preparations"],
        #     "created_at": edit_recipe.created_at
        # }, 201

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

        print(newReview, 'peony')
        print(newReview.to_dict, 'daisy')
        print(newReview.created_at, 'lilly')

        allReviews = Review.query.all()
        print(allReviews, 'fern')

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
