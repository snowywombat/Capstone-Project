from flask.cli import AppGroup
from .users import seed_users, undo_users
from .recipes import seed_recipes, undo_recipes
from .reviews import seed_reviews, undo_reviews
from .tags import seed_tags, undo_tags
from .cultures import seed_cultures, undo_cultures
from .kitchenwares import seed_kitchenwares, undo_kitchenwares
from .ingredients import seed_ingredients, undo_ingredients
from .preparations import seed_preparations, undo_preparations

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_preparations()
        undo_ingredients()
        undo_kitchenwares()
        undo_cultures()
        undo_tags()
        undo_reviews()
        undo_recipes
        undo_users()
    seed_users()
    seed_recipes()
    seed_reviews()
    seed_tags()
    seed_cultures()
    seed_kitchenwares()
    seed_ingredients()
    seed_preparations()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
    undo_preparations()
    undo_ingredients()
    undo_kitchenwares()
    undo_cultures()
    undo_tags()
    undo_reviews()
    undo_recipes()
    undo_users()
