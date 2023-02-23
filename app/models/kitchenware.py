from .db import db, environment, SCHEMA, add_prefix_for_prod

class Kitchenware(db.Model):
    __tablename__ = 'kitchenwares'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)

    # Many-To-One between Kichenwares and Recipes
    recipe = db.relationship("Recipe", back_populates='kitchenwares')

    def to_dict(self):
        return {
            'id': self.id,
            "name": self.name,
            "recipe_id": self.recipe_id,
            "recipe": self.recipe
        }
