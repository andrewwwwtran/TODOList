# TODOList
To Do list web application

- Has user authentication
- To-do list is connected to each user (no other user has access to another's to-do list)
- User is able to add/delete tasks.
- Used simple CSS Bootstrap

What I've learned:
- User authentication
  - How to hash passwords using werkzeug's packages
  - How to retrieve login/sign up information using Flask request package
  - Checking if user is already logged in with Flask.current_user
  - Checking if user's email was already used
- Database
  - How to store users and their to-do lists using Flask SQLAlchemy
  - How to retrieve/delete tasks in user's to-do list from the database
  - Making a database schema for user and tasks
- Jinja
  - Using blocks to change content between each html page
  - How to write if-else statements/for-loops
  - How to display data using {{ data }}
- Flask
  - Flashing messages using Flask.flash
  - Redirect users upon button click with Flask.redirect and url_for
