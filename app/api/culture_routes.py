from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import db, Culture
from ..forms.culture_form import CreateCultureForm, EditCultureForm
from .auth_routes import validation_errors_to_error_messages

culture_routes = Blueprint('culture', __name__)

@culture_routes.route('/')
def get_all_articles(cultureId):
    all_articles = Culture.query.all()

    res = {
    "Articles":[]
    }

    for article in all_articles:
        data = article.to_dict()
        data.pop("user")
        res["Articles"].append(data)


    return res


@culture_routes.route('/<int:cultureId>')
def get_single_article(cultureId):
    single_article = db.session.query(Culture).get(int(cultureId))

    if not single_article:
        return {"message": "Article couldn't be found"}, 404

    data = single_article.to_dict()

    res = {
    "Article":[]
    }

    article = {
        "id": data["id"],
        "user_id": data["user_id"],
        "title": data["title"],
        "description": data["description"],
        "banner_img": data["banner_img"],
        "article": data["article"],
        "createdAt": data["created_at"],
        "user": {
            "id": data["user"].id,
            "firstName": data["user"].first_name,
            "lastName": data["user"].last_name,
            "email": data["user"].email,
            "username": data["user"].username
        },
    }


    res["Article"].append(article)
    return res


@culture_routes.route('/',  methods=["POST"])
@login_required
def create_article():
    user_id = current_user.id

    form = CreateCultureForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        newArticle = Culture (
            title = data["title"],
            description = data["description"],
            banner_img = data["banner_img"],
            article = data["article"],
            user_id = user_id,
        )

        db.session.add(newArticle)
        db.session.commit()

        allArticles = Culture.query.all()

        return {
            "id": allArticles[len(allArticles)-1].id,
            "user_id": user_id,
            "title": data["title"],
            "description": data["description"],
            "banner_img": data["banner_img"],
            "article": data["article"],
            "user": {
                "id": allArticles[len(allArticles)-1].user.id,
                "firstName": allArticles[len(allArticles)-1].user.first_name,
                "lastName": allArticles[len(allArticles)-1].user.last_name
            },
            "createdAt": allArticles[len(allArticles)-1].created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



@culture_routes.route('/<int:cultureId>', methods=["PUT"])
@login_required
def update_article(cultureId):
    edit_article = db.session.query(Culture).get(int(cultureId))

    if not edit_article:
        return {"message": "Article couldn't be found"}, 404


    if edit_article.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401


    form = EditCultureForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data

        edit_article.title = data["title"]
        edit_article.description = data["description"]
        edit_article.banner_img = data["banner_img"]
        edit_article.article = data["article"]

        db.session.commit()

        return {
            "id": edit_article.id,
            "user_id": edit_article.user_id,
            "title": data["title"],
            "description": data["description"],
            "banner_img": data["banner_img"],
            "article": data["article"],
            "user": {
                "id": edit_article.user.id,
                "firstName": edit_article.user.first_name,
                "lastName": edit_article.user.last_name
            },
            "created_at": edit_article.created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@culture_routes.route('/<int:cultureId>', methods=["DELETE"])
@login_required
def delete_article(cultureId):

    #find article
    remove_article = db.session.query(Culture).get(int(cultureId))

    if not remove_article:
      return {"message": "Article couldn't be found"}, 404

    if remove_article.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    db.session.delete(remove_article)
    db.session.commit()

    return {"message": "Successfully deleted"}
