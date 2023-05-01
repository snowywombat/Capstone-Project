from app.models import db, Tag, environment, SCHEMA

tag1 = Tag(
    tag_name = "healthy",
    user_id=1,
    recipe_id=1
)

tag2 = Tag(
    tag_name = "fresh",
    user_id=2,
    recipe_id=2
)

tag3 = Tag(
    tag_name = "yummy",
    user_id=3,
    recipe_id=3
)

tag4 = Tag(
    tag_name = "lo-carbs",
    user_id=4,
    recipe_id=4
)

tag5 = Tag(
    tag_name = "kosher",
    user_id=5,
    recipe_id=5
)

tag6 = Tag(
    tag_name = "greens",
    user_id=5,
    recipe_id=6
)

tag7 = Tag(
    tag_name = "simple",
    user_id=10,
    recipe_id=7
)

tag8 = Tag(
    tag_name = "gluten-free",
    user_id=7,
    recipe_id=8
)

tag9 = Tag(
    tag_name = "cheesy",
    user_id=8,
    recipe_id=9
)

tag10 = Tag(
    tag_name = "nut-free",
    user_id=9,
    recipe_id=10
)

tag11 = Tag(
    tag_name = "italian",
    user_id=6,
    recipe_id=11
)

tag12 = Tag(
    tag_name = "vegan",
    user_id=3,
    recipe_id=12
)

tag13 = Tag(
    tag_name = "vegetarian",
    user_id=1,
    recipe_id=1
)

tag14 = Tag(
    tag_name = "breakfast",
    user_id=2,
    recipe_id=2
)

tag15 = Tag(
    tag_name = "sweet",
    user_id=3,
    recipe_id=3
)

tag16 = Tag(
    tag_name = "quick",
    user_id=4,
    recipe_id=4
)

tag17 = Tag(
    tag_name = "spring",
    user_id=5,
    recipe_id=5
)

tag18 = Tag(
    tag_name = "snack",
    user_id=5,
    recipe_id=6
)

tag19 = Tag(
    tag_name = "dairy-free",
    user_id=10,
    recipe_id=7
)

tag20 = Tag(
    tag_name = "mexican",
    user_id=7,
    recipe_id=8
)



def seed_tags():
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)
    db.session.add(tag4)
    db.session.add(tag5)
    db.session.add(tag6)
    db.session.add(tag7)
    db.session.add(tag8)
    db.session.add(tag9)
    db.session.add(tag10)
    db.session.add(tag11)
    db.session.add(tag12)
    db.session.add(tag13)
    db.session.add(tag14)
    db.session.add(tag15)
    db.session.add(tag16)
    db.session.add(tag17)
    db.session.add(tag18)
    db.session.add(tag19)
    db.session.add(tag20)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tags():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tags RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM tags")

    db.session.commit()
