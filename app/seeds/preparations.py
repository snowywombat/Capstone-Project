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

preparation7 = Preparation(description="Heat the vegetable oil in a large skillet or pot over medium heat.",
    recipe_id=2
)

preparation8 = Preparation(description="Add the chopped onion and cook until softened, about 5 minutes.",
    recipe_id=2
)

preparation9 = Preparation(description="Add the minced garlic and ginger, and cook for another 1-2 minutes until fragrant.",
    recipe_id=2
)

preparation10 = Preparation(description="Add the chicken pieces to the skillet or pot, and cook until lightly browned on all sides, about 5 minutes.",
    recipe_id=2
)

preparation11 = Preparation(description="Add the curry powder, ground cumin, ground coriander, turmeric, cayenne pepper, and salt to the skillet or pot, and stir well to coat the chicken and vegetables with the spices",
    recipe_id=2
)

preparation12 = Preparation(description="Add the diced tomatoes and coconut milk to the skillet or pot, and stir well to combine.",
    recipe_id=2
)

preparation13 = Preparation(description="Bring the mixture to a simmer, then reduce the heat to low and let it cook for 20-25 minutes, or until the chicken is cooked through and the sauce has thickened.",
    recipe_id=2
)

preparation14 = Preparation(description="Stir in the chopped cilantro, if using.",
    recipe_id=2
)

preparation15 = Preparation(description="Serve the chicken curry over rice or with naan bread, and enjoy!",
    recipe_id=2
)

preparation16 = Preparation(description="Preheat your oven to 450°F",
    recipe_id=3
)

preparation17 = Preparation(description="Roll out the pizza dough on a floured surface into a circle, about 12 inches in diameter.",
    recipe_id=3
)

preparation18 = Preparation(description="Place the rolled-out pizza dough onto a pizza pan or baking sheet lined with parchment paper.",
    recipe_id=3
)

preparation19 = Preparation(description="In a small bowl, mix together the tomato sauce, garlic powder, onion powder, oregano, salt, and pepper.",
    recipe_id=3
)

preparation20 = Preparation(description="Spread the tomato sauce mixture evenly over the pizza dough, leaving a small border around the edges.",
    recipe_id=3
)

preparation21 = Preparation(description="Sprinkle the shredded mozzarella cheese on top of the sauce.",
    recipe_id=3
)

preparation22 = Preparation(description="Bake the pizza in the preheated oven for 10-12 minutes or until the cheese is melted and the crust is golden brown.",
    recipe_id=3
)

preparation23 = Preparation(description="Remove the pizza from the oven and let it cool for a few minutes before slicing and serving.",
    recipe_id=3
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
    db.session.add(preparation19)
    db.session.add(preparation20)
    db.session.add(preparation21)
    db.session.add(preparation22)
    db.session.add(preparation23)
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
