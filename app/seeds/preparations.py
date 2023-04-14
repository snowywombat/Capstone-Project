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

preparation24 = Preparation(description="Preheat your oven to 375°F (190°C).",
    recipe_id=4
)

preparation25 = Preparation(description="Line a baking sheet with parchment paper.",
    recipe_id=4
)

preparation26 = Preparation(description="In a small mixing bowl, whisk together the olive oil, salt, and pepper.",
    recipe_id=4
)

preparation27 = Preparation(description="Place the salmon fillets on the prepared baking sheet, skin-side down (if using skin-on).",
    recipe_id=4
)

preparation28 = Preparation(description="Brush the salmon with the olive oil mixture, making sure to coat evenly.",
    recipe_id=4
)

preparation29 = Preparation(description="Top each salmon fillet with a few slices of lemon and a sprig of fresh dill.",
    recipe_id=4
)

preparation30 = Preparation(description="Bake the salmon in the preheated oven for 12-15 minutes, or until the internal temperature of the salmon reaches 145°F (63°C).",
    recipe_id=4
)

preparation31 = Preparation(description="Remove the salmon from the oven and let it rest for a few minutes.",
    recipe_id=4
)

preparation32 = Preparation(description="Using tongs, transfer the salmon to plates and serve immediately.",
    recipe_id=4
)

preparation33 = Preparation(description="In a small mixing bowl, whisk together the olive oil, lime juice, orange juice, chili powder, cumin, garlic powder, salt, and pepper.",
    recipe_id=5
)

preparation34 = Preparation(description="Place the flank steak in a shallow dish and pour the marinade over it, making sure to coat both sides.",
    recipe_id=5
)

preparation35 = Preparation(description="Cover the dish with plastic wrap and refrigerate for at least 30 minutes (or up to 4 hours).",
    recipe_id=5
)

preparation36 = Preparation(description="Preheat a grill or grill pan over high heat.",
    recipe_id=5
)

preparation37 = Preparation(description="Remove the steak from the marinade and discard any excess marinade.",
    recipe_id=5
)

preparation38 = Preparation(description="Grill the steak for 4-6 minutes per side, or until it reaches your desired level of doneness.",
    recipe_id=5
)

preparation39 = Preparation(description="Remove the steak from the grill and let it rest for a few minutes.",
    recipe_id=5
)

preparation40 = Preparation(description="While the steak is resting, warm the corn tortillas on the grill or in a skillet.",
    recipe_id=5
)

preparation41 = Preparation(description="Slice the steak against the grain into thin strips.",
    recipe_id=5
)

preparation42 = Preparation(description="Assemble the tacos by placing a few strips of steak on each tortilla, along with a sprinkle of cilantro, diced red onion, and a squeeze of lime juice.",
    recipe_id=5
)

preparation43 = Preparation(description="Serve immediately and enjoy!",
    recipe_id=5
)

preparation44 = Preparation(description="In a mixing bowl, stir together the Greek yogurt, honey, and vanilla extract until smooth.",
    recipe_id=6
)

preparation45 = Preparation(description="Rinse the berries and pat them dry with a paper towel. If using strawberries, remove the stems and slice them.",
    recipe_id=6
)

preparation46 = Preparation(description="Spoon a layer of the yogurt mixture into the bottom of each glass or jar.",
    recipe_id=6
)

preparation47 = Preparation(description="Add a layer of mixed berries on top of the yogurt.",
    recipe_id=6
)

preparation48 = Preparation(description="Sprinkle a layer of granola on top of the berries.",
    recipe_id=6
)

preparation49 = Preparation(description="Repeat these layers until the glasses or jars are full, ending with a layer of granola.",
    recipe_id=6
)

preparation50 = Preparation(description="Serve immediately, or cover and refrigerate until ready to serve.",
    recipe_id=6
)

preparation51 = Preparation(description="Rinse the mixed greens and pat them dry with a paper towel. Place them in a large mixing bowl.",
    recipe_id=7
)

preparation52 = Preparation(description="Add the diced avocado, cherry tomatoes, diced cucumber, chopped cilantro, and crumbled feta cheese to the mixing bowl.",
    recipe_id=7
)

preparation53 = Preparation(description="In a small mixing bowl, whisk together the olive oil, red wine vinegar, salt, and pepper.",
    recipe_id=7
)

preparation54 = Preparation(description="Pour the dressing over the salad and toss well to coat.",
    recipe_id=7
)

preparation55 = Preparation(description="Serve immediately, garnished with additional cilantro if desired.",
    recipe_id=7
)

preparation56 = Preparation(description="In a large mixing bowl, whisk together the flour, baking powder, salt, and sugar.",
    recipe_id=8
)

preparation57 = Preparation(description="In a separate mixing bowl, beat the egg and then whisk in the milk and melted butter.",
    recipe_id=8
)

preparation58 = Preparation(description="Pour the wet ingredients into the dry ingredients and whisk until smooth.",
    recipe_id=8
)

preparation59 = Preparation(description="Stir in the mixed berries.",
    recipe_id=8
)

preparation60 = Preparation(description="Heat a skillet or griddle over medium heat. Once hot, scoop about 1/4 cup of batter onto the skillet for each pancake.",
    recipe_id=8
)

preparation61 = Preparation(description="Cook until bubbles form on the surface of the pancake and the edges start to look set, then flip and cook for another minute or so on the other side until lightly golden brown.",
    recipe_id=8
)

preparation62 = Preparation(description="Repeat with the remaining batter, adding more butter or oil to the skillet if necessary.",
    recipe_id=8
)

preparation63 = Preparation(description="Serve the pancakes hot, topped with additional berries and your favorite syrup if desired.",
    recipe_id=8
)

preparation64 = Preparation(description="Heat a large pot over medium-high heat. Add the popcorn kernels and cover the pot with a lid.",
    recipe_id=9
)

preparation65 = Preparation(description="Shake the pot occasionally to prevent the kernels from burning. Once the popping slows down, remove the pot from the heat.",
    recipe_id=9
)

preparation66 = Preparation(description="Melt the butter in a small microwave-safe bowl.",
    recipe_id=9
)

preparation67 = Preparation(description="Pour the popcorn into a large mixing bowl and drizzle the melted butter over the popcorn. Toss well to coat.",
    recipe_id=9
)

preparation68 = Preparation(description="Season with salt to taste.",
    recipe_id=9
)

preparation69 = Preparation(description="Serve immediately and enjoy your low calorie buttery popcorn!",
    recipe_id=9
)

preparation70 = Preparation(description="Toast the slices of bread to your desired level of crispness.",
    recipe_id=10
)

preparation71 = Preparation(description="While the bread is toasting, slice the avocado in half and remove the pit.",
    recipe_id=10
)

preparation72 = Preparation(description="Scoop the avocado flesh into a bowl and mash it with a fork until it's smooth but still slightly chunky.",
    recipe_id=10
)

preparation73 = Preparation(description="Squeeze the lemon juice over the mashed avocado and stir to combine. Add salt and pepper to taste.",
    recipe_id=10
)

preparation74 = Preparation(description="Top the toasted bread slices with the mashed avocado mixture, spreading it evenly.",
    recipe_id=10
)

preparation75 = Preparation(description="Top the avocado with fresh spinach leaves.",
    recipe_id=10
)

preparation76 = Preparation(description="Serve immediately and enjoy your delicious avocado toast with spinach!",
    recipe_id=10
)

preparation77 = Preparation(description="In a large pot, bring the chicken broth to a simmer over medium heat.",
    recipe_id=11
)

preparation78 = Preparation(description="Add the chicken breasts, carrots, celery, onion, garlic, bay leaf, and thyme.",
    recipe_id=11
)

preparation79 = Preparation(description="Cover the pot and simmer for 20-25 minutes, or until the chicken is cooked through.",
    recipe_id=11
)

preparation80 = Preparation(description="Remove the chicken from the pot with tongs and shred it with two forks.",
    recipe_id=11
)

preparation81 = Preparation(description="Return the shredded chicken to the pot and add the egg noodles.",
    recipe_id=11
)

preparation82 = Preparation(description="Simmer for 8-10 minutes, or until the noodles are tender.",
    recipe_id=11
)

preparation83 = Preparation(description="Season the soup with salt and pepper to taste.",
    recipe_id=11
)

preparation84 = Preparation(description="Serve the soup hot, garnished with chopped fresh parsley if desired.",
    recipe_id=11
)

preparation85 = Preparation(description="In a large mixing bowl, whisk together the flour, salt, and yeast.",
    recipe_id=12
)

preparation86 = Preparation(description="Add the warm water and stir until a shaggy dough forms. The dough will be sticky and wet.",
    recipe_id=12
)

preparation87 = Preparation(description="Cover the bowl with a kitchen towel and let the dough rise in a warm place for 12-18 hours. The dough should double in size and have bubbles on the surface.",
    recipe_id=12
)

preparation88 = Preparation(description="Preheat your oven to 450°F (230°C) and place a Dutch oven with the lid on in the oven to heat up for 30 minutes.",
    recipe_id=12
)

preparation89 = Preparation(description="While the Dutch oven is heating up, turn the dough out onto a lightly floured surface and shape it into a round ball.",
    recipe_id=12
)

preparation90 = Preparation(description="Place a sheet of parchment paper on top of the dough ball and flip it over so the parchment paper is on the bottom.",
    recipe_id=12
)

preparation91 = Preparation(description="Cover the dough ball with a kitchen towel and let it rest for 30 minutes.",
    recipe_id=12
)

preparation92 = Preparation(description="Remove the Dutch oven from the oven and carefully lift the parchment paper with the dough ball and place it inside the Dutch oven. Cover with the lid.",
    recipe_id=12
)

preparation93 = Preparation(description="Bake the bread for 30 minutes with the lid on, then remove the lid and bake for an additional 15-20 minutes, or until the bread is golden brown and crusty.",
    recipe_id=12
)

preparation94 = Preparation(description="Remove the bread from the Dutch oven and let it cool on a wire rack for at least 30 minutes before slicing and serving.",
    recipe_id=12
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
    db.session.add(preparation24)
    db.session.add(preparation25)
    db.session.add(preparation26)
    db.session.add(preparation27)
    db.session.add(preparation28)
    db.session.add(preparation29)
    db.session.add(preparation30)
    db.session.add(preparation31)
    db.session.add(preparation32)
    db.session.add(preparation33)
    db.session.add(preparation34)
    db.session.add(preparation35)
    db.session.add(preparation36)
    db.session.add(preparation37)
    db.session.add(preparation38)
    db.session.add(preparation39)
    db.session.add(preparation40)
    db.session.add(preparation41)
    db.session.add(preparation42)
    db.session.add(preparation43)
    db.session.add(preparation44)
    db.session.add(preparation45)
    db.session.add(preparation46)
    db.session.add(preparation47)
    db.session.add(preparation48)
    db.session.add(preparation49)
    db.session.add(preparation50)
    db.session.add(preparation51)
    db.session.add(preparation52)
    db.session.add(preparation53)
    db.session.add(preparation54)
    db.session.add(preparation55)
    db.session.add(preparation56)
    db.session.add(preparation57)
    db.session.add(preparation58)
    db.session.add(preparation59)
    db.session.add(preparation60)
    db.session.add(preparation61)
    db.session.add(preparation62)
    db.session.add(preparation63)
    db.session.add(preparation64)
    db.session.add(preparation65)
    db.session.add(preparation66)
    db.session.add(preparation67)
    db.session.add(preparation68)
    db.session.add(preparation69)
    db.session.add(preparation70)
    db.session.add(preparation71)
    db.session.add(preparation72)
    db.session.add(preparation73)
    db.session.add(preparation74)
    db.session.add(preparation75)
    db.session.add(preparation76)
    db.session.add(preparation77)
    db.session.add(preparation78)
    db.session.add(preparation79)
    db.session.add(preparation80)
    db.session.add(preparation81)
    db.session.add(preparation82)
    db.session.add(preparation83)
    db.session.add(preparation84)
    db.session.add(preparation85)
    db.session.add(preparation86)
    db.session.add(preparation87)
    db.session.add(preparation88)
    db.session.add(preparation89)
    db.session.add(preparation90)
    db.session.add(preparation91)
    db.session.add(preparation92)
    db.session.add(preparation93)
    db.session.add(preparation94)

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
