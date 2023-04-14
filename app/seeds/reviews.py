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

review3 = Review(review="It's a really great recipe!",
    stars=5,
    location="Seattle, WA",
    user_id=2,
    recipe_id=4
)

review4 = Review(review="Lacked a little bit of flavor, but overall, great!",
    stars=4,
    location="Seattle, WA",
    user_id=2,
    recipe_id=7
)

review5 = Review(review="I've made this recipe multiple times and it never disappoints. Highly recommend!",
    stars=5,
    location="Summit, NJ",
    user_id=3,
    recipe_id=1
)

review6 = Review(review="The dish turned out okay, but it wasn't as flavorful as I was hoping for.",
    stars=3,
    location="Summit, NJ",
    user_id=3,
    recipe_id=7
)

review7 = Review(review="I loved this recipe! It was so easy and tasted great.",
    stars=4,
    location="Arlington County, VA",
    user_id=4,
    recipe_id=1
)

review8 = Review(review="The dish was okay, but I've had better. It lacked a little something.",
    stars=3,
    location="Arlington County, VA",
    user_id=4,
    recipe_id=2
)

review9 = Review(review="This recipe was a disappointment, I wouldn't make it again.",
    stars=1,
    location="Wilmington, DE",
    user_id=5,
    recipe_id=4
)

review10 = Review(review="The flavors in this dish are incredible, I'm impressed.",
    stars=5,
    location="Wilmington, DE",
    user_id=5,
    recipe_id=10
)

review11 = Review(review="This dish is absolutely delicious, full of flavor and satisfying.",
    stars=5,
    location="Williamsburg, VA",
    user_id=6,
    recipe_id=1
)

review12 = Review(review="I didn't love it, but it wasn't terrible either.",
    stars=4,
    location="Williamsburg, VA",
    user_id=6,
    recipe_id=9
)

review13 = Review(review="A great recipe that's easy to follow and turned out fantastic.",
    stars=5,
    location="Long Beach, CA",
    user_id=7,
    recipe_id=2
)

review14 = Review(review="Unfortunately, this dish just didn't turn out well for me.",
    stars=2,
    location="Long Beach, CA",
    user_id=7,
    recipe_id=11
)

review15 = Review(review="Not the best, but not the worst either. Just an average dish.",
    stars=3,
    location="Concord, MA",
    user_id=8,
    recipe_id=12
)

review16 = Review(review="Absolutely loved this recipe - can't wait to make it again!",
    stars=5,
    location="Concord, MA",
    user_id=8,
    recipe_id=6
)

review17 = Review(review="A new favorite in my recipe collection - definitely worth trying!",
    stars=5,
    location="Johnstone, UK",
    user_id=9,
    recipe_id=5
)

review18 = Review(review="Wow, this recipe exceeded my expectations! So tasty and satisfying.",
    stars=5,
    location="Johnstone, UK",
    user_id=9,
    recipe_id=4
)

review19 = Review(review="This recipe is a keeper! The flavors and textures were perfect.",
    stars=5,
    location="Tulsa, OK",
    user_id=10,
    recipe_id=9
)

review20 = Review(review="It was alright, but I think I'll try a different recipe next time.",
    stars=3,
    location="Tulsa, OK",
    user_id=10,
    recipe_id=2
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
    db.session.add(review16)
    db.session.add(review17)
    db.session.add(review18)
    db.session.add(review19)
    db.session.add(review20)
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
