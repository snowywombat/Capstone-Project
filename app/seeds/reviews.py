from app.models import db, Review, environment, SCHEMA

review1 = Review(review="This was an amazing dish! I added a little extra spice and it was perfect.",
    stars=5,
    location="Los Angeles",
    user_id=3,
    recipe_id=6
)

review2 = Review(review="The recipe was easy to follow and the results were delicious.",
    stars=4,
    location="Sydney, Australia",
    user_id=2,
    recipe_id=2
)

review3 = Review(review="I've made this recipe multiple times and it never disappoints. Highly recommend!",
    stars=5,
    location="San Francisco, CA",
    user_id=2,
    recipe_id=10
)

review4 = Review(review="The dish turned out okay, but it wasn't as flavorful as I was hoping for.",
    stars=3,
    location="Chicago, Illinois",
    user_id=1,
    recipe_id=8
)

review5 = Review(review="I loved this recipe! It was so easy and tasted great.",
    stars=4,
    location="Houston, TX",
    user_id=1,
    recipe_id=5
)

review6 = Review(review="The dish was okay, but I've had better. It lacked a little something.",
    stars=3,
    location="Seattle",
    user_id=3,
    recipe_id=1
)

review7 = Review(review="The recipe was easy to follow and the results were delicious. I'll definitely be making this again!",
    stars=4,
    location="Miami, Florida",
    user_id=2,
    recipe_id=7
)

review8 = Review(review="I was disappointed in this dish. It didn't live up to my expectations.",
    stars=2,
    location="Edinburgh",
    user_id=1,
    recipe_id=4
)

review9 = Review(review="This recipe was amazing! The flavors were so complex and delicious.",
    stars=5,
    location="Kansas City",
    user_id=3,
    recipe_id=9
)

review10 = Review(review="The dish was decent, but nothing to write home about. I might try it again with some modifications.",
    stars=3,
    location="Washington D.C.",
    user_id=1,
    recipe_id=11
)

review11 = Review(review="This recipe was fantastic! I didn't think I'd like the combination of flavors, but it was delicious.",
    stars=4,
    location="Boston",
    user_id=2,
    recipe_id=3
)

review12 = Review(review="The dish was just okay. It needed a little something extra to make it really shine.",
    stars=3,
    location="Czech Republic",
    user_id=1,
    recipe_id=9
)

review13 = Review(review="The recipe was easy to follow and the dish turned out great! I'll definitely be making this again.",
    stars=4,
    location="San Diego, California",
    user_id=2,
    recipe_id=1
)

review14 = Review(review="I was disappointed in this recipe. It was bland and lacked flavor.",
    stars=1,
    location="Portland, OR",
    user_id=3,
    recipe_id=8
)

review15 = Review(review="I was disappointed in this recipe. It was bland and lacked flavor.",
    stars=4,
    location="Phoenix",
    user_id=2,
    recipe_id=4
)


def seed_reviews():
    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.add(review9)
    db.session.add(review10)
    db.session.add(review11)
    db.session.add(review12)
    db.session.add(review13)
    db.session.add(review14)
    db.session.add(review15)
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
