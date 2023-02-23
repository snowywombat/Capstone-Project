from .db import db, environment, SCHEMA, add_prefix_for_prod

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    measurement_num = db.Column(db.Float, nullable=False)
    measurement_type = db.Column(db.String(20), nullable=False)
    ingredient = db.Column(db.String(100), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)

    # Many-To-One between Ingredients and Recipes
    recipe = db.relationship("Recipe", back_populates='ingredients')

    def to_dict(self):
        return {
            'id': self.id,
            'measurement_num': self.measurement_num,
            "measurement_type": self.measurement_type,
            "ingredient": self.ingredient,
            "recipe_id": self.recipe_id,
            "recipe": self.recipe
        }
