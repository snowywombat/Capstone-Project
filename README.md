# Shana's Kitchen 🍋

Shana's Kitchen is inspired by the website, Bon Appetit. It is a platform to post and view recipes for your own culinary exploration!

Live site: https://shanaskitchen.onrender.com

## Wiki Links:
* [API Documentation](https://github.com/snowywombat/Capstone-Project/wiki/API-Routes)
* [Database Schema](https://github.com/snowywombat/Capstone-Project/wiki/Database-Schema)
* [Feature List](https://github.com/snowywombat/Capstone-Project/wiki/Feature-List)
* [User Stories](https://github.com/snowywombat/Capstone-Project/wiki/User-Stories)

## Tech Stack

  ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
  ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
  ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
  ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
  ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
  ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
  * SQLAlchemy
  * Alembic
  
## Getting started
1. Clone this repository: `
   https://github.com/snowywombat/Capstone-Project.git
   `

2. Install dependencies

      ```bash
      pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
   - Example
   
   ```js
   SECRET_KEY=super-secret-key
   FLASK_ENV=development
   FLASK_DEBUG=True
   DATABASE_URL=sqlite:///dev.db
   SCHEMA=capstone_schema
   FLASK_RUN_PORT=5001
   ```

4. Make sure the SQLite3 database connection URL is in the **.env** file

5. This starter organizes all tables inside the `flask_schema` schema, defined
   by the `SCHEMA` environment variable.  Replace the value for
   `SCHEMA` with a unique name, **making sure you use the snake_case
   convention**.

6. Get into your pipenv, migrate your database, seed your database, and run your Flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

7. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

# Features 

## Recipes
* Users can view recipes
* Logged-in users can create a recipe
* Logged-in owners can update their recipe
* Logged-in owners can delete their recipe

## Reviews
* Users can view reviews for a recipe
* Logged-in users can create a review on a recipe
* Logged-in owners can update their review
* Logged-in owners can delete their review

## Tags
* Users can view tags for a recipe
* Logged-in owners can create tags
* Logged-in owners can delete their tags

## Food Culture Articles
* Users can view articles about food culture
* Logged-in users can create an article
* Logged-in owners can update their article
* Logged-in owners can delete their article


## Future Features
### Users Page
* Logged-in users can change their user settings
### AWS
* Logged-in owners can upload images of their spot to AWS S3

