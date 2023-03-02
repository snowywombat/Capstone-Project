from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

today = datetime.now()

class Recipe(db.Model):
    __tablename__ = 'recipes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(750), nullable=False)
    servings_num = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=today)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)

    # Many-To-One between Recipes and Users
    user = db.relationship("User", back_populates="recipes")

    reviews = db.relationship("Review", back_populates="recipe", cascade="all,delete")
    kitchenwares = db.relationship("Kitchenware", back_populates="recipe", cascade="all,delete")
    preparations = db.relationship("Preparation", back_populates="recipe", cascade="all,delete")
    ingredients = db.relationship("Ingredient", back_populates="recipe", cascade="all,delete")

    # print(reviews, 'reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'servings_num': self.servings_num,
            'img_url': self.img_url,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'user': self.user,
            'reviews': self.reviews,
            'kitchenwares': self.kitchenwares,
            'preparations': self.preparations,
            'ingredients':self.ingredients
        }
