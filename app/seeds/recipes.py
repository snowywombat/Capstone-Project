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



def seed_recipes():
    db.session.add(recipe1)
    db.session.add(recipe2)
    db.session.add(recipe3)


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
