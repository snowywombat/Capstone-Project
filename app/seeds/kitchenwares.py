from app.models import db, Kitchenware, environment, SCHEMA

kitchenware1 = Kitchenware(name="Large pot for boiling pasta",
    recipe_id=1
)

kitchenware2 = Kitchenware(name="Colander for draining pasta",
    recipe_id=1
)

kitchenware3 = Kitchenware(name="Food processor or blender",
    recipe_id=1
)

kitchenware4 = Kitchenware(name="Measuring cups and spoons",
    recipe_id=1
)

kitchenware5 = Kitchenware(name="Wooden spoon or tongs",
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

kitchenware18 = Kitchenware(name="Baking sheet",
    recipe_id=4
)

kitchenware19 = Kitchenware(name="Parchement paper",
    recipe_id=4
)

kitchenware20 = Kitchenware(name="Mixing bowl",
    recipe_id=4
)

kitchenware21 = Kitchenware(name="Whisk",
    recipe_id=4
)

kitchenware22 = Kitchenware(name="Tongs",
    recipe_id=4
)

kitchenware23 = Kitchenware(name="Grill or grill pan",
    recipe_id=5
)

kitchenware24 = Kitchenware(name="Mixing bowl",
    recipe_id=5
)

kitchenware25 = Kitchenware(name="Tongs",
    recipe_id=5
)

kitchenware26 = Kitchenware(name="Cutting board",
    recipe_id=5
)

kitchenware27 = Kitchenware(name="Knife",
    recipe_id=5
)

kitchenware28 = Kitchenware(name="4 glasses or jars",
    recipe_id=6
)

kitchenware29 = Kitchenware(name="Mixing bowl",
    recipe_id=6
)

kitchenware30 = Kitchenware(name="Spoon",
    recipe_id=6
)

kitchenware31 = Kitchenware(name="Large mxing bowl",
    recipe_id=7
)

kitchenware32 = Kitchenware(name="Cutting board",
    recipe_id=7
)

kitchenware33 = Kitchenware(name="Knife",
    recipe_id=7
)

kitchenware34 = Kitchenware(name="Salad tongs or serving spoons",
    recipe_id=7
)

kitchenware35 = Kitchenware(name="Large mixing bowl",
    recipe_id=8
)

kitchenware36 = Kitchenware(name="Whisk",
    recipe_id=8
)

kitchenware37 = Kitchenware(name="Measuring cups and spoons",
    recipe_id=8
)

kitchenware38 = Kitchenware(name="Skillet or griddle",
    recipe_id=8
)

kitchenware39 = Kitchenware(name="Spatula",
    recipe_id=8
)

kitchenware40 = Kitchenware(name="Large pot with lid",
    recipe_id=9
)

kitchenware41 = Kitchenware(name="Measuring cups and spoons",
    recipe_id=9
)

kitchenware42 = Kitchenware(name="Mixing bowl",
    recipe_id=9
)

kitchenware43 = Kitchenware(name="Toaster or toaster oven",
    recipe_id=10
)

kitchenware44 = Kitchenware(name="Cutting board",
    recipe_id=10
)

kitchenware45 = Kitchenware(name="Knife",
    recipe_id=10
)

kitchenware46 = Kitchenware(name="Bowl",
    recipe_id=10
)

kitchenware47 = Kitchenware(name="Fork",
    recipe_id=10
)

kitchenware48 = Kitchenware(name="Large pot with lid",
    recipe_id=11
)

kitchenware49 = Kitchenware(name="Cutting board",
    recipe_id=11
)

kitchenware50 = Kitchenware(name="Knife",
    recipe_id=11
)

kitchenware51 = Kitchenware(name="Wooden spoon",
    recipe_id=11
)

kitchenware52 = Kitchenware(name="Tongs",
    recipe_id=11
)

kitchenware53 = Kitchenware(name="Measuring cups and spoons",
    recipe_id=11
)

kitchenware54 = Kitchenware(name="Large mixing bowl",
    recipe_id=12
)

kitchenware55 = Kitchenware(name="Wooden spoon",
    recipe_id=12
)

kitchenware56 = Kitchenware(name="Dutch oven with lid",
    recipe_id=12
)

kitchenware57 = Kitchenware(name="Parchement paper",
    recipe_id=12
)

kitchenware58 = Kitchenware(name="Kitchen towel",
    recipe_id=12
)

kitchenware59 = Kitchenware(name="Oven",
    recipe_id=12
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
    db.session.add(kitchenware21)
    db.session.add(kitchenware22)
    db.session.add(kitchenware23)
    db.session.add(kitchenware24)
    db.session.add(kitchenware25)
    db.session.add(kitchenware26)
    db.session.add(kitchenware27)
    db.session.add(kitchenware28)
    db.session.add(kitchenware29)
    db.session.add(kitchenware30)
    db.session.add(kitchenware31)
    db.session.add(kitchenware32)
    db.session.add(kitchenware33)
    db.session.add(kitchenware34)
    db.session.add(kitchenware35)
    db.session.add(kitchenware36)
    db.session.add(kitchenware37)
    db.session.add(kitchenware38)
    db.session.add(kitchenware39)
    db.session.add(kitchenware40)
    db.session.add(kitchenware41)
    db.session.add(kitchenware42)
    db.session.add(kitchenware43)
    db.session.add(kitchenware44)
    db.session.add(kitchenware45)
    db.session.add(kitchenware46)
    db.session.add(kitchenware47)
    db.session.add(kitchenware48)
    db.session.add(kitchenware49)
    db.session.add(kitchenware50)
    db.session.add(kitchenware51)
    db.session.add(kitchenware52)
    db.session.add(kitchenware53)
    db.session.add(kitchenware54)
    db.session.add(kitchenware55)
    db.session.add(kitchenware56)
    db.session.add(kitchenware57)
    db.session.add(kitchenware58)
    db.session.add(kitchenware59)
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
