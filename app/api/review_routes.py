from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import db, Review
from ..forms.review_form import CreateReviewForm, EditReviewForm
from .auth_routes import validation_errors_to_error_messages

review_routes = Blueprint('review', __name__)

@review_routes.route('/<int:reviewId>', methods=["PUT"])
@login_required
def update_review(reviewId):
    edit_review = db.session.query(Review).get(int(reviewId))

    if not edit_review:
        return {"message": "Review couldn't be found"}, 404


    if edit_review.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401


    form = EditReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data

        edit_review.review = data["review"]
        edit_review.stars = data["stars"]
        edit_review.location = data["location"]

        db.session.commit()

        return {
            "id": edit_review.id,
            "user_id": edit_review.user_id,
            "recipe_id": edit_review.recipe_id,
            "review": data["review"],
            "stars": data["stars"],
            "location": data["location"],
            "user": {
                "id": edit_review.user.id,
                "firstName": edit_review.user.first_name,
                "lastName": edit_review.user.last_name
            },
            "created_at": edit_review.created_at
        }

    #Error handling
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@review_routes.route('/<int:reviewId>', methods=["DELETE"])
@login_required
def delete_review(reviewId):
    #find recipe
    delete_review = db.session.query(Review).get(int(reviewId))

    if not delete_review:
      return {"message": "Review couldn't be found"}, 404

    if delete_review.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    db.session.delete(delete_review)
    db.session.commit()

    return {"message": "Successfully deleted"}
