from app.models import db, Ingredient, environment, SCHEMA

ingredient1 = Ingredient(measurement_num=1,
    measurement_type="cup",
    ingredient="flour",
    recipe_id=6
)

ingredient2 = Ingredient(measurement_num=3,
    measurement_type="cups",
    ingredient="water",
    recipe_id=1
)

ingredient3 = Ingredient(measurement_num=0.5,
    measurement_type="teaspoon",
    ingredient="salt",
    recipe_id=7
)

ingredient4 = Ingredient(measurement_num=2,
    measurement_type="1/4 cup",
    ingredient="yeast",
    recipe_id=5
)

ingredient5 = Ingredient(measurement_num=1,
    measurement_type="teaspoon",
    ingredient="baking soda",
    recipe_id=11
)

ingredient6 = Ingredient(measurement_num=0.75,
    measurement_type="cup",
    ingredient="granulated sugar",
    recipe_id=10
)

ingredient7 = Ingredient(measurement_num=2,
    measurement_type="large",
    ingredient="eggs",
    recipe_id=6
)

ingredient8 = Ingredient(measurement_num=2,
    measurement_type="tablespoons",
    ingredient="olive oil",
    recipe_id=8
)

ingredient9 = Ingredient(measurement_num=1,
    measurement_type="medium",
    ingredient="onion, chopped",
    recipe_id=2
)

ingredient10 = Ingredient(measurement_num=1,
    measurement_type="cup",
    ingredient="flour",
    recipe_id=4
)

ingredient11 = Ingredient(measurement_num=2,
    measurement_type="cloves",
    ingredient="garlic, minced",
    recipe_id=9
)

ingredient12 = Ingredient(measurement_num=2,
    measurement_type="cans (28 oz each)",
    ingredient="whole peeled tomatoes",
    recipe_id=3
)

ingredient13 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="chicken or vegetable broth",
    recipe_id=5
)

ingredient14 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="heavy cream",
    recipe_id=7
)

ingredient15 = Ingredient(measurement_num=2,
    measurement_type="tablespoons",
    ingredient="chopped fresh basil leaves",
    recipe_id=2
)

ingredient16 = Ingredient(measurement_num=1,
    measurement_type="pound",
    ingredient="boneless, skinless chicken breast, sliced into thin strips",
    recipe_id=1
)

ingredient17 = Ingredient(measurement_num=1,
    measurement_type="tablespoon",
    ingredient="grated fresh ginger",
    recipe_id=9
)

ingredient18 = Ingredient(measurement_num=0.25,
    measurement_type="cup",
    ingredient="soy sauce",
    recipe_id=11
)

ingredient19 = Ingredient(measurement_num=1,
    measurement_type="ablespoon",
    ingredient="honey",
    recipe_id=6
)

ingredient20 = Ingredient(measurement_num=2,
    measurement_type="cup",
    ingredient="mixed vegetables",
    recipe_id=8
)


def seed_ingredients():
    db.session.add(ingredient1)
    db.session.add(ingredient2)
    db.session.add(ingredient3)
    db.session.add(ingredient4)
    db.session.add(ingredient5)
    db.session.add(ingredient6)
    db.session.add(ingredient7)
    db.session.add(ingredient8)
    db.session.add(ingredient9)
    db.session.add(ingredient10)
    db.session.add(ingredient11)
    db.session.add(ingredient12)
    db.session.add(ingredient13)
    db.session.add(ingredient14)
    db.session.add(ingredient15)
    db.session.add(ingredient16)
    db.session.add(ingredient17)
    db.session.add(ingredient18)
    db.session.add(ingredient19)
    db.session.add(ingredient20)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_ingredients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ingredients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM ingredients")

    db.session.commit()
