from app.models import db, Review, environment, SCHEMA

review1 = Review(review="This was an amazing dish! I added a little extra spice and it was perfect.",
    stars=5,
    location="Seattle, WA",
    user_id=1,
    recipe_id=2
)

review2 = Review(review="The recipe was easy to follow and the results were delicious.",
    stars=4,
    location="Seattle, WA",
    user_id=1,
    recipe_id=3
)

review3 = Review(review="I've made this recipe multiple times and it never disappoints. Highly recommend!",
    stars=5,
    location="Summit, NJ",
    user_id=2,
    recipe_id=1
)

review4 = Review(review="The dish turned out okay, but it wasn't as flavorful as I was hoping for.",
    stars=3,
    location="Summit, NJ",
    user_id=2,
    recipe_id=3
)

review5 = Review(review="I loved this recipe! It was so easy and tasted great.",
    stars=4,
    location="Arlington County, VA",
    user_id=3,
    recipe_id=1
)

review6 = Review(review="The dish was okay, but I've had better. It lacked a little something.",
    stars=3,
    location="Arlington County, VA",
    user_id=3,
    recipe_id=2
)



def seed_reviews():
    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM reviews")

    db.session.commit()
