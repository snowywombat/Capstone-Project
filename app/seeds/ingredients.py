from app.models import db, Ingredient, environment, SCHEMA

ingredient1 = Ingredient(measurement_num=1,
    measurement_type="pound",
    ingredient="pasta",
    recipe_id=1
)

ingredient2 = Ingredient(measurement_num=2,
    measurement_type="cups",
    ingredient="fresh basil leaves, packed",
    recipe_id=1
)

ingredient3 = Ingredient(measurement_num=3,
    measurement_type="cloves",
    ingredient="garlic, minced",
    recipe_id=1
)

ingredient4 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="grated Parmesan cheese",
    recipe_id=1
)

ingredient5 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="olive oil",
    recipe_id=1
)

ingredient6 = Ingredient(measurement_num=1,
    measurement_type="lb",
    ingredient="boneless, skinless chicken breasts, cut into bite-sized pieces",
    recipe_id=2
)

ingredient7 = Ingredient(measurement_num=1,
    measurement_type="medium",
    ingredient="onion, chopped",
    recipe_id=2
)

ingredient8 = Ingredient(measurement_num=1,
    measurement_type="tbsp",
    ingredient="ginger, minced",
    recipe_id=2
)

ingredient9 = Ingredient(measurement_num=1,
    measurement_type="tbsp",
    ingredient="vegetable oil",
    recipe_id=2
)

ingredient10 = Ingredient(measurement_num=1,
    measurement_type="tbsp",
    ingredient="curry powder",
    recipe_id=2
)

ingredient11 = Ingredient(measurement_num=1,
    measurement_type="tsp",
    ingredient="ground cumin",
    recipe_id=2
)

ingredient12 = Ingredient(measurement_num=1,
    measurement_type="tsp",
    ingredient="ground coriander",
    recipe_id=2
)

ingredient13 = Ingredient(measurement_num=0.5,
    measurement_type="tsp",
    ingredient="turmeric",
    recipe_id=2
)

ingredient14 = Ingredient(measurement_num=0.5,
    measurement_type="tsp",
    ingredient="cayenne pepper (adjust to taste)",
    recipe_id=2
)

ingredient15 = Ingredient(measurement_num=0.5,
    measurement_type="tsp",
    ingredient="salt (adjust to taste)",
    recipe_id=2
)

ingredient16 = Ingredient(measurement_num=1,
    measurement_type="can (14 oz)",
    ingredient="diced tomatoes",
    recipe_id=2
)

ingredient17 = Ingredient(measurement_num=1,
    measurement_type="can (13.5 oz)",
    ingredient="coconut milk",
    recipe_id=2
)

ingredient18 = Ingredient(measurement_num=0.25,
    measurement_type="cup",
    ingredient="fresh cilantro leaves, chopped (optional)",
    recipe_id=2
)

ingredient19 = Ingredient(measurement_num=1,
    measurement_type="pound",
    ingredient="pizza dough",
    recipe_id=3
)

ingredient20 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="tomato sauce",
    recipe_id=3
)

ingredient21 = Ingredient(measurement_num=0.25,
    measurement_type="tsp",
    ingredient="garlic powder",
    recipe_id=3
)

ingredient22 = Ingredient(measurement_num=0.25,
    measurement_type="tsp",
    ingredient="onion powder",
    recipe_id=3
)

ingredient23 = Ingredient(measurement_num=0.25,
    measurement_type="tsp",
    ingredient="dried oregano",
    recipe_id=3
)

ingredient24 = Ingredient(measurement_num=2,
    measurement_type="cups",
    ingredient="shredded mozzarella cheese",
    recipe_id=3
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
    db.session.add(ingredient21)
    db.session.add(ingredient22)
    db.session.add(ingredient23)
    db.session.add(ingredient24)
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
