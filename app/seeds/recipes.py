from app.models import db, Recipe, environment, SCHEMA

recipe1 = Recipe(name='Pesto Pasta',
    description='A simple yet delicious recipe for pesto pasta.',
    servings_num = 6,
    img_url='https://images.pexels.com/photos/1435896/pexels-photo-1435896.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=1
)

recipe2 = Recipe(name='Chicken Curry',
    description='A spicy chicken curry recipe that is perfect for cold nights.',
    servings_num = 2,
    img_url='https://images.pexels.com/photos/7438982/pexels-photo-7438982.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=2
)

recipe3 = Recipe(name='Cheese Pizza',
    description='A classic cheese pizza recipe that is sure to please.',
    servings_num = 4,
    img_url='https://images.pexels.com/photos/2471171/pexels-photo-2471171.jpeg?auto=compress&cs=tinysrgb&w=1600',
    user_id=3
)

recipe4 = Recipe(name='Baked Salmon',
    description='Flaky baked salmon seasoned with lemon and herbs, tender and delicious.',
    servings_num = 6,
    img_url='https://images.pexels.com/photos/5741440/pexels-photo-5741440.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=4
)

recipe5 = Recipe(name='Carne Asada Tacos',
    description='Tender beef in warm corn tortillas, topped with onion and cilantro.',
    servings_num = 5,
    img_url='https://images.pexels.com/photos/7613568/pexels-photo-7613568.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=5
)

recipe6 = Recipe(name='Greek Yogurt Parfait',
    description='Thick Greek yogurt layered with fresh berries and crunchy granola.',
    servings_num = 4,
    img_url='https://images.pexels.com/photos/4696280/pexels-photo-4696280.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=5
)

recipe7 = Recipe(name='Mixed Salad w/ Avocado',
    description='Colorful mix of greens, veggies, and feta cheese, dressed with tangy vinaigrette.',
    servings_num = 6,
    img_url='https://images.pexels.com/photos/1213710/pexels-photo-1213710.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=10
)

recipe8 = Recipe(name='Very Berry Pancakes',
    description='Delicious pancakes loaded with fresh berries, a sweet breakfast treat.',
    servings_num = 8,
    img_url='https://images.pexels.com/photos/2280545/pexels-photo-2280545.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=7
)

recipe9 = Recipe(name='Low Calorie Buttery Popcorn',
    description='Light and airy popcorn seasoned with buttery flavor, guilt-free snacking.',
    servings_num = 2,
    img_url='https://images.pexels.com/photos/3537844/pexels-photo-3537844.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=8
)

recipe10 = Recipe(name='Avocado Toast with Spinach',
    description='Crusty bread topped with creamy avocado, fresh spinach, and zesty lemon.',
    servings_num = 2,
    img_url='https://images.pexels.com/photos/1351238/pexels-photo-1351238.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=9
)

recipe11 = Recipe(name='Chicken Noodle Soup',
    description='Hearty chicken soup with tender noodles and fresh herbs, comforting classic.',
    servings_num = 8,
    img_url='https://images.pexels.com/photos/4041711/pexels-photo-4041711.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=6
)

recipe12 = Recipe(name='Rustic Artesian Bread',
    description='Crusty, rustic bread made with simple ingredients, perfect for sandwiches.',
    servings_num = 12,
    img_url='https://images.pexels.com/photos/1387070/pexels-photo-1387070.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
    user_id=3
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
