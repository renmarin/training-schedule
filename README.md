# training-schedule
Django training schedule app with GraphQL interface

# Links
**Heroku:** https://training-schedule-7128.herokuapp.com/

**Postman collection link:** https://www.getpostman.com/collections/d0d110fcfaab2bdc8f1e

# How to run
1. Install everything from the requirements.txt file: `pip install -r requirements.txt`
2. Populate the database if using a local database `python populate_db.py` (optional)
3. Start server `python manage.py runserver` or `gunicorn sport.wsgi`
