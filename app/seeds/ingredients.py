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

ingredient25 = Ingredient(measurement_num=4,
    measurement_type="fillets",
    ingredient="salmon",
    recipe_id=4
)

ingredient26 = Ingredient(measurement_num=2,
    measurement_type="tablespoons",
    ingredient="olive oil",
    recipe_id=4
)

ingredient27 = Ingredient(measurement_num=1,
    measurement_type="teaspoon",
    ingredient="salt",
    recipe_id=4
)

ingredient28 = Ingredient(measurement_num=0.5,
    measurement_type="teaspoon",
    ingredient="black pepper",
    recipe_id=4
)

ingredient28 = Ingredient(measurement_num=2,
    measurement_type="medium",
    ingredient="lemons, sliced",
    recipe_id=4
)

ingredient29 = Ingredient(measurement_num=4,
    measurement_type="sprigs",
    ingredient="fresh dill",
    recipe_id=4
)

ingredient30 = Ingredient(measurement_num=1,
    measurement_type="pound",
    ingredient="flank steak",
    recipe_id=5
)

ingredient31 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="olive oil",
    recipe_id=5
)

ingredient32 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="lime juice",
    recipe_id=5
)

ingredient33 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="orange juice",
    recipe_id=5
)

ingredient34 = Ingredient(measurement_num=1,
    measurement_type="tsp",
    ingredient="chili powder",
    recipe_id=5
)

ingredient35 = Ingredient(measurement_num=1,
    measurement_type="tsp",
    ingredient="cumin",
    recipe_id=5
)

ingredient36 = Ingredient(measurement_num=0.5,
    measurement_type="tsp",
    ingredient="garlic powder",
    recipe_id=5
)

ingredient37 = Ingredient(measurement_num=10,
    measurement_type="small",
    ingredient="corn torillas",
    recipe_id=5
)

ingredient38 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="chopped fresh cilantro",
    recipe_id=5
)

ingredient39 = Ingredient(measurement_num=0.5,
    measurement_type="medium",
    ingredient="red onion, diced",
    recipe_id=5
)

ingredient40 = Ingredient(measurement_num=2,
    measurement_type="cups",
    ingredient="plain Greek yogurt",
    recipe_id=6
)

ingredient41 = Ingredient(measurement_num=2,
    measurement_type="cups",
    ingredient="mixed berries",
    recipe_id=6
)

ingredient42 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="granola",
    recipe_id=6
)

ingredient43 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="honey",
    recipe_id=6
)

ingredient43 = Ingredient(measurement_num=1,
    measurement_type="tsp",
    ingredient="vanilla extract",
    recipe_id=6
)

ingredient44 = Ingredient(measurement_num=6,
    measurement_type="cups",
    ingredient="mixed greens",
    recipe_id=7
)

ingredient45 = Ingredient(measurement_num=1,
    measurement_type="large",
    ingredient="ripe avocado, peeled and diced",
    recipe_id=7
)

ingredient46 = Ingredient(measurement_num=1,
    measurement_type="cup",
    ingredient="cherry tomatoes, halved",
    recipe_id=7
)

ingredient47 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="diced cucumber",
    recipe_id=7
)

ingredient48 = Ingredient(measurement_num=0.25,
    measurement_type="cup",
    ingredient="chopped fresh cilantro",
    recipe_id=7
)

ingredient50 = Ingredient(measurement_num=0.25,
    measurement_type="cup",
    ingredient="crumbled feta cheese",
    recipe_id=7
)

ingredient51 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="extra-virgin olive oil",
    recipe_id=7
)

ingredient52 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="red wine vinegar",
    recipe_id=7
)

ingredient53 = Ingredient(measurement_num=1,
    measurement_type="cup",
    ingredient="all-purpose flour",
    recipe_id=8
)

ingredient54 = Ingredient(measurement_num=1,
    measurement_type="tablespoon",
    ingredient="baking powder",
    recipe_id=8
)

ingredient55 = Ingredient(measurement_num=0.25,
    measurement_type="teaspoon",
    ingredient="salt",
    recipe_id=8
)

ingredient56 = Ingredient(measurement_num=1,
    measurement_type="tablespoon",
    ingredient="granulated sugar",
    recipe_id=8
)

ingredient57 = Ingredient(measurement_num=1,
    measurement_type="large",
    ingredient="egg",
    recipe_id=8
)

ingredient58 = Ingredient(measurement_num=1,
    measurement_type="cup",
    ingredient="milk",
    recipe_id=8
)

ingredient59 = Ingredient(measurement_num=2,
    measurement_type="tablespoons",
    ingredient="unsalted butter, melted",
    recipe_id=8
)

ingredient60 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="mixed berries",
    recipe_id=8
)

ingredient61 = Ingredient(measurement_num=0.25,
    measurement_type="cup",
    ingredient="popcorn kernels",
    recipe_id=9
)

ingredient62 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="unsalted butter",
    recipe_id=9
)

ingredient63 = Ingredient(measurement_num=3,
    measurement_type="tsp",
    ingredient="salt",
    recipe_id=9
)

ingredient64 = Ingredient(measurement_num=2,
    measurement_type="slices",
    ingredient="whole grain bread",
    recipe_id=10
)

ingredient65 = Ingredient(measurement_num=1,
    measurement_type="large",
    ingredient="ripe avocado",
    recipe_id=10
)

ingredient66 = Ingredient(measurement_num=0.5,
    measurement_type="cup",
    ingredient="fresh spinach leaves",
    recipe_id=10
)

ingredient67 = Ingredient(measurement_num=0.5,
    measurement_type="small",
    ingredient="lemon",
    recipe_id=10
)

ingredient68 = Ingredient(measurement_num=1,
    measurement_type="pound",
    ingredient="boneless, skinless chicken breasts",
    recipe_id=11
)

ingredient69 = Ingredient(measurement_num=8,
    measurement_type="cups",
    ingredient="low-sodium chicken broth",
    recipe_id=11
)

ingredient70 = Ingredient(measurement_num=2,
    measurement_type="cups",
    ingredient="chopped carrots",
    recipe_id=11
)

ingredient71 = Ingredient(measurement_num=2,
    measurement_type="cups",
    ingredient="chopped celery",
    recipe_id=11
)

ingredient72 = Ingredient(measurement_num=1,
    measurement_type="medium",
    ingredient="onion, chopped",
    recipe_id=11
)

ingredient73 = Ingredient(measurement_num=3,
    measurement_type="cloves",
    ingredient="garlic, minced",
    recipe_id=11
)

ingredient74 = Ingredient(measurement_num=1,
    measurement_type="large",
    ingredient="bay leaf",
    recipe_id=11
)

ingredient75 = Ingredient(measurement_num=1,
    measurement_type="tsp",
    ingredient="dried thyme",
    recipe_id=11
)

ingredient76 = Ingredient(measurement_num=8,
    measurement_type="ounces",
    ingredient="egg noodles",
    recipe_id=11
)

ingredient77 = Ingredient(measurement_num=2,
    measurement_type="tbsp",
    ingredient="fresh parsley, chopped",
    recipe_id=11
)

ingredient78 = Ingredient(measurement_num=3,
    measurement_type="cups",
    ingredient="all-purpose flour",
    recipe_id=12
)

ingredient79 = Ingredient(measurement_num=1.5,
    measurement_type="teaspoons",
    ingredient="salt",
    recipe_id=12
)

ingredient79 = Ingredient(measurement_num=0.5,
    measurement_type="teaspoon",
    ingredient="active dry yeast",
    recipe_id=12
)

ingredient80 = Ingredient(measurement_num=1.5,
    measurement_type="cups",
    ingredient="warm water",
    recipe_id=12
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
    db.session.add(ingredient25)
    db.session.add(ingredient26)
    db.session.add(ingredient27)
    db.session.add(ingredient28)
    db.session.add(ingredient29)
    db.session.add(ingredient30)
    db.session.add(ingredient31)
    db.session.add(ingredient32)
    db.session.add(ingredient33)
    db.session.add(ingredient34)
    db.session.add(ingredient35)
    db.session.add(ingredient36)
    db.session.add(ingredient37)
    db.session.add(ingredient38)
    db.session.add(ingredient39)
    db.session.add(ingredient40)
    db.session.add(ingredient41)
    db.session.add(ingredient42)
    db.session.add(ingredient43)
    db.session.add(ingredient44)
    db.session.add(ingredient45)
    db.session.add(ingredient46)
    db.session.add(ingredient47)
    db.session.add(ingredient48)
    db.session.add(ingredient50)
    db.session.add(ingredient51)
    db.session.add(ingredient52)
    db.session.add(ingredient53)
    db.session.add(ingredient54)
    db.session.add(ingredient55)
    db.session.add(ingredient56)
    db.session.add(ingredient57)
    db.session.add(ingredient58)
    db.session.add(ingredient59)
    db.session.add(ingredient60)
    db.session.add(ingredient61)
    db.session.add(ingredient62)
    db.session.add(ingredient63)
    db.session.add(ingredient64)
    db.session.add(ingredient65)
    db.session.add(ingredient66)
    db.session.add(ingredient67)
    db.session.add(ingredient68)
    db.session.add(ingredient69)
    db.session.add(ingredient70)
    db.session.add(ingredient71)
    db.session.add(ingredient72)
    db.session.add(ingredient73)
    db.session.add(ingredient74)
    db.session.add(ingredient75)
    db.session.add(ingredient76)
    db.session.add(ingredient77)
    db.session.add(ingredient78)
    db.session.add(ingredient79)
    db.session.add(ingredient80)
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
