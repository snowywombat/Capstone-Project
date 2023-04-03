from app.models import db, Recipe, environment, SCHEMA

recipe1 = Recipe(name='Pesto Pasta',
    description='A simple yet delicious recipe for pesto pasta.',
    servings_num = 6,
    img_url='https://images.pexels.com/photos/1435896/pexels-photo-1435896.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=3
)

recipe2 = Recipe(name='Chicken Curry',
    description='A spicy chicken curry recipe that is perfect for cold nights.',
    servings_num = 2,
    img_url='https://images.pexels.com/photos/7438982/pexels-photo-7438982.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=6
)

recipe3 = Recipe(name='Cheese Pizza',
    description='A classic cheese pizza recipe that is sure to please.',
    servings_num = 4,
    img_url='https://images.pexels.com/photos/2471171/pexels-photo-2471171.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=7
)

recipe4 = Recipe(name='Beef Stir Fry',
    description='A quick and easy beef stir fry recipe that is perfect for busy weeknights.',
    servings_num = 4,
    img_url='https://images.pexels.com/photos/2181151/pexels-photo-2181151.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=3
)

recipe5 = Recipe(name='Chocolate Cake',
    description='A decadent chocolate cake recipe that is perfect for special occasions.',
    servings_num = 12,
    img_url='https://images.pexels.com/photos/4109998/pexels-photo-4109998.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=6
)

recipe6 = Recipe(name='Tacos',
    description='A simple recipe for tacos that is perfect for a weeknight dinner.',
    servings_num = 8,
    img_url='https://images.pexels.com/photos/7613568/pexels-photo-7613568.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=7
)

recipe7 = Recipe(name='Chicken Salad',
    description='A healthy and delicious chicken salad recipe that is perfect for lunch.',
    servings_num = 4,
    img_url='https://images.pexels.com/photos/3763426/pexels-photo-3763426.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=3
)

recipe8 = Recipe(name='Spaghetti and Meatballs',
    description='A classic spaghetti and meatballs recipe that is perfect for family dinners.',
    servings_num = 8,
    img_url='https://images.pexels.com/photos/9617397/pexels-photo-9617397.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=6
)

recipe9 = Recipe(name='Roast Chicken',
    description='A delicious roast chicken recipe that is perfect for Sunday dinner.',
    servings_num = 6,
    img_url='https://images.pexels.com/photos/2673353/pexels-photo-2673353.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=7
)

recipe10 = Recipe(name='Pumpkin Soup',
    description='A comforting pumpkin soup recipe that is perfect for chilly evenings.',
    img_url='https://images.pexels.com/photos/6072108/pexels-photo-6072108.jpeg?auto=compress&cs=tinysrgb&w=1600',
    servings_num = 2,
    user_id=3
)

recipe11 = Recipe(name='Fish and Chips',
    description='A classic fish and chips recipe that is perfect for a Friday night dinner.',
    servings_num = 4,
    img_url='https://images.pexels.com/photos/1123249/pexels-photo-1123249.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=6
)

recipe12 = Recipe(name='Blueberry Pancakes',
    description='Fluffy pancakes loaded with sweet blueberries. This easy recipe is perfect for a delicious breakfast or brunch treat.',
    servings_num = 8,
    img_url='https://images.pexels.com/photos/3780469/pexels-photo-3780469.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=7
)

recipe13 = Recipe(name='Tomato Soup',
    description='Classic comfort food at its finest! This recipe features velvety tomato soup.',
    servings_num = 4,
    img_url='https://images.pexels.com/photos/539451/pexels-photo-539451.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=3
)

recipe14 = Recipe(name='Classic French Toast',
    description='Golden brown bread soaked in a sweet egg mixture, Classic French Toast is the ultimate breakfast comfort food!',
    servings_num = 6,
    img_url='https://images.pexels.com/photos/10232459/pexels-photo-10232459.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=6
)

recipe15 = Recipe(name='Vegetable Lasagna',
    description='Hearty and comforting, Vegetable Lasagna features layers of noodles, veggies, and creamy cheese sauce.',
    servings_num = 8,
    img_url='https://images.pexels.com/photos/4079522/pexels-photo-4079522.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=7
)

def seed_recipes():
    db.session.add(recipe1)
    db.session.add(recipe2)
    db.session.add(recipe3)
    db.session.add(recipe4)
    db.session.add(recipe5)
    db.session.add(recipe6)
    db.session.add(recipe7)
    db.session.add(recipe8)
    db.session.add(recipe9)
    db.session.add(recipe10)
    db.session.add(recipe11)
    db.session.add(recipe12)
    db.session.add(recipe13)
    db.session.add(recipe14)
    db.session.add(recipe15)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_recipes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.recipes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM recipes")

    db.session.commit()
