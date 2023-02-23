from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

today = datetime.now()

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(100), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=today)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)

    # Many-To-One between Reviews and Users
    user = db.relationship("User", back_populates="reviews")
    # Many-To-One between Reviews and Recipes
    recipe = db.relationship("Recipe", back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'review': self.review,
            'stars': self.stars,
            'location': self.location,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id,
            'user': self.user,
            'recipe': self.recipe
        }
