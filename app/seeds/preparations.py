from app.models import db, Preparation, environment, SCHEMA

preparation1 = Preparation(description="Cook the pasta according to package instructions until al dente. Reserve 1/2 cup of the pasta water.",
    recipe_id=1
)

preparation2 = Preparation(description="While the pasta is cooking, make the pesto sauce. In a food processor, combine the basil leaves, garlic, Parmesan cheese, and olive oil. Pulse until smooth.",
    recipe_id=1
)

preparation3 = Preparation(description="If the pesto sauce is too thick, add some of the reserved pasta water, a tablespoon at a time, until the desired consistency is reached.",
    recipe_id=1
)

preparation4 = Preparation(description="Drain the pasta and return it to the pot. Add the pesto sauce and toss to coat the pasta evenly.",
    recipe_id=1
)

preparation5 = Preparation(description="Season with salt and pepper to taste.",
    recipe_id=1
)

preparation6 = Preparation(description="Serve hot, garnished with additional Parmesan cheese and fresh basil leaves, if desired.",
    recipe_id=1
)

preparation7 = Preparation(description="Stir in the chocolate chips by hand, making sure they are evenly distributed throughout the dough.",
    recipe_id=7
)

preparation8 = Preparation(description="Drop the dough by rounded spoonfuls onto the prepared baking sheet, spacing them about 2 inches apart.",
    recipe_id=6
)

preparation9 = Preparation(description="Bake for 10-12 minutes, until the edges are lightly browned and the centers are set.",
    recipe_id=5
)

preparation10 = Preparation(description="In a large skillet, heat the oil over medium-high heat.",
    recipe_id=2
)

preparation11 = Preparation(description="Add the chopped onion and cook for 2-3 minutes until it softens and becomes translucent.",
    recipe_id=1
)

preparation12 = Preparation(description="Add the minced garlic and cook for an additional 30 seconds until fragrant.",
    recipe_id=11
)

preparation13 = Preparation(description="Add the ground beef or turkey and cook for 5-7 minutes, breaking it up with a wooden spoon, until it is browned and cooked through.",
    recipe_id=6
)

preparation14 = Preparation(description="Add the chili powder, ground cumin, paprika, salt, and pepper to the skillet, and stir well to combine. Cook for another 2-3 minutes to allow the spices to meld with the meat.",
    recipe_id=5
)

preparation15 = Preparation(description="Warm the tortillas in a microwave or in a dry skillet over medium heat for a few seconds on each side.",
    recipe_id=8
)

preparation16 = Preparation(description="In a large pot, add the chicken and cover with water. Bring to a boil, then reduce the heat to low and let the chicken simmer for 1-2 hours until cooked through.",
    recipe_id=6
)

preparation17 = Preparation(description="Add the chopped onion, celery, carrots, garlic, bay leaf, thyme, salt, and pepper to the pot with the chicken broth. Simmer for 20-30 minutes until the vegetables are tender.",
    recipe_id=8
)

preparation18 = Preparation(description="If desired, add the egg noodles or other pasta to the pot and cook for 6-8 minutes until tender.",
    recipe_id=9
)


def seed_preparations():
    db.session.add(preparation1)
    db.session.add(preparation2)
    db.session.add(preparation3)
    db.session.add(preparation4)
    db.session.add(preparation5)
    db.session.add(preparation6)
    db.session.add(preparation7)
    db.session.add(preparation8)
    db.session.add(preparation9)
    db.session.add(preparation10)
    db.session.add(preparation11)
    db.session.add(preparation12)
    db.session.add(preparation13)
    db.session.add(preparation14)
    db.session.add(preparation15)
    db.session.add(preparation16)
    db.session.add(preparation17)
    db.session.add(preparation18)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_preparations():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.preparations RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM preparations")

    db.session.commit()
