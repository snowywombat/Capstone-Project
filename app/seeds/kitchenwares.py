from app.models import db, Kitchenware, environment, SCHEMA

kitchenware1 = Kitchenware(name="spoon",
    recipe_id=1
)

kitchenware2 = Kitchenware(name="bowl",
    recipe_id=2
)

kitchenware3 = Kitchenware(name="pan",
    recipe_id=3
)

kitchenware4 = Kitchenware(name="wisk",
    recipe_id=4
)

kitchenware5 = Kitchenware(name="baking sheet",
    recipe_id=5
)

kitchenware6 = Kitchenware(name="large bowl",
    recipe_id=6
)

kitchenware7 = Kitchenware(name="spatula",
    recipe_id=7
)

kitchenware8 = Kitchenware(name="cutting knife",
    recipe_id=8
)

kitchenware9 = Kitchenware(name="cutting board",
    recipe_id=9
)

kitchenware10 = Kitchenware(name="pot",
    recipe_id=10
)

kitchenware11 = Kitchenware(name="oven proof pan",
    recipe_id=11
)

kitchenware12 = Kitchenware(name="blender",
    recipe_id=1
)

kitchenware13 = Kitchenware(name="rolling pin",
    recipe_id=2
)

kitchenware14 = Kitchenware(name="10' deep pan",
    recipe_id=3
)

kitchenware15 = Kitchenware(name="grater",
    recipe_id=4
)

kitchenware16 = Kitchenware(name="slicer",
    recipe_id=5
)

kitchenware17 = Kitchenware(name="wooden spoon",
    recipe_id=6
)

kitchenware18 = Kitchenware(name="beater",
    recipe_id=7
)

kitchenware19 = Kitchenware(name="salad fork",
    recipe_id=8
)

kitchenware20 = Kitchenware(name="pitcher",
    recipe_id=9
)


def seed_kitchenwares():
    db.session.add(kitchenware1)
    db.session.add(kitchenware2)
    db.session.add(kitchenware3)
    db.session.add(kitchenware4)
    db.session.add(kitchenware5)
    db.session.add(kitchenware6)
    db.session.add(kitchenware7)
    db.session.add(kitchenware8)
    db.session.add(kitchenware9)
    db.session.add(kitchenware10)
    db.session.add(kitchenware11)
    db.session.add(kitchenware12)
    db.session.add(kitchenware13)
    db.session.add(kitchenware14)
    db.session.add(kitchenware15)
    db.session.add(kitchenware16)
    db.session.add(kitchenware17)
    db.session.add(kitchenware18)
    db.session.add(kitchenware19)
    db.session.add(kitchenware20)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_kitchenwares():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.kitchenwares RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM kitchenwares")

    db.session.commit()
