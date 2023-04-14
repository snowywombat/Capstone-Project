from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        first_name='Demo', last_name='User', username='demo123', email='demo@aa.io', password='password')
    shana = User(
        first_name='Shana', last_name='Edouard', username='shanaedouard', email='shana@aa.io', password='password')
    meryl = User(
        first_name='Meryl', last_name='Streep', username='merylstreep',email='meryl@aa.io', password='password')
    sandra = User(
        first_name='Sandra', last_name="Bullock", username='sandrabullock', email='sandra@aa.io', password='password')
    aubrey = User(
        first_name='Aubrey', last_name='Plaza', username='aubreyplaza', email='aubrey@aa.io', password='password')
    boglarka = User(
        first_name='Boglarka', last_name='Edouard', username='boglarkaedouard', email='boglarka@aa.io', password='password')
    coreen = User(
        first_name='Coreen', last_name='Viczian', username='coreenviczian', email='coreen@aa.io', password='password')
    steve = User(
        first_name='Steve', last_name='Carell', username='stevecarell', email='steve@aa.io', password='password')
    gordon = User(
        first_name='Gordon', last_name='Ramsay', username='gordonramsay', email='gordon@aa.io', password='password')
    bill = User(
        first_name='Bill', last_name='Hader', username='billhader', email='bill@aa.io', password='password')


    db.session.add(demo)
    db.session.add(shana)
    db.session.add(meryl)
    db.session.add(sandra)
    db.session.add(aubrey)
    db.session.add(boglarka)
    db.session.add(coreen)
    db.session.add(steve)
    db.session.add(gordon)
    db.session.add(bill)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
