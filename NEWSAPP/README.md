# Django Hacker New Api
This project is base on a hacker news api. <br>
Django is used to consume the hacker news api and stored into a local database (Sqlite for development), you can switch to any database of your choice.
It also send requests every 5 mins to the hacker news api to get updated news


## Requisites
- Django 3. and above
- Python 3.7
- Django rest framework
- Apscheduler
- SQLite

## Setup
This project requires Python 3.7. To setup the environment, please follow these steps:
```
```
- Create a folder in your desired location

```
```
- Create a virtual environment (optional , but very useful)
```

```
- Clone the github repository
```
git clone https://github.com/blackgeeknerd/Hacker-News.git
```
- Activate the virtual enviroment and Install the requirements
```
pip install -r requirements.txt
```

## Run Django Project Locally

- make migration
    - python manage.py makemigrations
- migrate
    - python manage.py migrate
- run server
    - python manage.py runserver [port number]


## Functionalities
### Regular User Pages
- Create stories
- Edit/Update Stories created by Users but not News/Stories gotten from the New Api
- Delete Stories created by Users but not News/Stories gotten from the New Api
- Search by Username, By(name), Title and Type 
### APi  http://127.0.0.1:8000/news-api/newsdb/
- Get least of Latest News
- Post News
 



