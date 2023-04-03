from app.models import db, Kitchenware, environment, SCHEMA

kitchenware1 = Kitchenware(name="Large pot for boiling pasta",
    recipe_id=1
)

kitchenware2 = Kitchenware(name="Colander for draining pasta",
    recipe_id=1
)

kitchenware3 = Kitchenware(name="Food processor or blender for making the pesto sauce",
    recipe_id=1
)

kitchenware4 = Kitchenware(name="Measuring cups and spoons",
    recipe_id=1
)

kitchenware5 = Kitchenware(name="Wooden spoon or tongs for stirring pasta",
    recipe_id=1
)

kitchenware6 = Kitchenware(name="Serving bowl",
    recipe_id=1
)

kitchenware7 = Kitchenware(name="Large pot",
    recipe_id=2
)

kitchenware8 = Kitchenware(name="Cutting board",
    recipe_id=2
)

kitchenware9 = Kitchenware(name="Sharp knife",
    recipe_id=2
)

kitchenware10 = Kitchenware(name="Wooden spoon or spatula",
    recipe_id=2
)

kitchenware11 = Kitchenware(name="Measuring cups and spoons",
    recipe_id=2
)

kitchenware12 = Kitchenware(name="Can opener",
    recipe_id=2
)

kitchenware13 = Kitchenware(name="Small bowl",
    recipe_id=2
)

kitchenware14 = Kitchenware(name="Rolling pin",
    recipe_id=3
)

kitchenware15 = Kitchenware(name="Pizza pan or baking sheet",
    recipe_id=3
)

kitchenware16 = Kitchenware(name="Parchment paper",
    recipe_id=3
)

kitchenware17 = Kitchenware(name="Measuring cups and spoons",
    recipe_id=3
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
