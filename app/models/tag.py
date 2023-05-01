from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

today = datetime.now()

class Tag(db.Model):
    __tablename__ = 'tags'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=today)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)

    # Many-To-One between Tags and Users
    user = db.relationship("User", back_populates="tags")
    # Many-To-One between Tags and Recipes
    recipe = db.relationship("Recipe", back_populates='tags')

    def to_dict(self):
        return {
            'id': self.id,
            'tag_name': self.tag_name,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id,
            'user': self.user,
            'recipe': self.recipe
        }
