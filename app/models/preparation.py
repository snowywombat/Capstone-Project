from .db import db, environment, SCHEMA, add_prefix_for_prod

class Preparation(db.Model):
    __tablename__ = 'preparations'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)

    # Many-To-One between Preparations and Recipes
    recipe = db.relationship("Recipe", back_populates='preparations')

    def to_dict(self):
        return {
            'id': self.id,
            "description": self.description,
            "recipe_id": self.recipe_id,
            "recipe": self.recipe,
        }
