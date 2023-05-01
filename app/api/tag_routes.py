from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import db, Tag
from ..forms.tag_form import CreateTagForm, EditTagForm
from .auth_routes import validation_errors_to_error_messages

tag_routes = Blueprint('tag', __name__)

@tag_routes.route('/<int:tagId>', methods=["PUT"])
@login_required
def update_tag(tagId):
    edit_tag = db.session.query(Tag).get(int(tagId))

    if not edit_tag:
        return {"message": "Tag couldn't be found"}, 404


    if edit_tag.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401


    form = EditTagForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data

        edit_tag.tag_name = data["tag_name"]

        db.session.commit()

        return {
            "id": edit_tag.id,
            "user_id": edit_tag.user_id,
            "recipe_id": edit_tag.recipe_id,
            "tag_name": data["tag_name"],
            "user": {
                "id": edit_tag.user.id,
                "firstName": edit_tag.user.first_name,
                "lastName": edit_tag.user.last_name
            },
            "created_at": edit_tag.created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@tag_routes.route('/<int:tagId>', methods=["DELETE"])
@login_required
def delete_tag(tagId):

    delete_tag = db.session.query(Tag).get(int(tagId))

    if not delete_tag:
      return {"message": "Tag couldn't be found"}, 404

    if delete_tag.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    db.session.delete(delete_tag)
    db.session.commit()

    return {"message": "Successfully deleted"}
