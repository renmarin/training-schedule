# training-schedule
Django training schedule app with GraphQL interface

# Links
**Heroku:** https://training-schedule-7128.herokuapp.com/

**Postman collection link:** https://www.getpostman.com/collections/d0d110fcfaab2bdc8f1e

# How to run
1. Install everything from the requirements.txt file: `pip install -r requirements.txt`
2. Populate the database if using a local database `python populate_db.py` (optional)
3. Start server `python manage.py runserver` or `gunicorn sport.wsgi`

# Sample Custom Queries

1. All schedules (sorted by date, time):
```
query{
  schedules{
    id
    name
    date
    time
    user{
      id
      username
    }
  }
}
```
2. Schedules between 2022-01-08 - 2022-01-09 inclusive (sorted by date, time):
```
query {
  schedules(startDate: "2022-01-08" endDate: "2022-01-09") {
    id
    name
    date
    time
    user{
      id
      username
    }
  }
}
```
3. Schedules between 2022-01-08 - 2022-01-09 and 14:00 - 16:00 inclusive (sorted by date, time):
```
query {
  schedules(startDate: "2022-01-08" endDate: "2022-01-09" startTime: "14:00" endTime: "16:00") {
    id
    name
    date
    time
    user{
      id
      username
    }
  }
}
```
4. Detail of training with ID = 24:
```
query {
  detailById(id: 24) {
    id
    name
    date
    time
    user{
      id
      username
    }
  }
}
```
5. Schedule of a user with ID = 9:
```
query {
  userById(id: 9) {
    id
    username
    schedules{
      id
      name
      date
      time
    }
  }
}
```
