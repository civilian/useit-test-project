# Oscar Chamat | useit test project

This repository contains my Test Project for the Software Development role at
[useitweb](https://www.useitweb.com), thank you for taking the time to read this documentation.
If you want me to implement some new feature, fix something or give any further detail don't hesitate on reaching me at chamatoscar@gmail.com.

## Installation
Assuming you are using Ubuntu and you have the repository cloned already

### Testing installation
1) Make sure you have **Python 3.6+** installed on your machine
2) `cd useit-test-project`
3) Create pipenv to manage the virtualenv -> `python3 -m pip install pipenv`
4) Install dependencies -> `pipenv install`
5) Activate the virtual env -> `pipenv shell`
5) If you want you can either
    * Use the database with preprepopulated -> `mv test.db.sqlite3 db.sqlite3`
    * Or migrate the database -> `python manage.py migrate`
6) Run the testing server -> `python manage.py runserver`

## Executing 
Go to the url indicated by the test server -> [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

The users that you can log in with are:

| User  | Password |
|-------|----------|
| pablo | pablo    |
| oscar | oscar    |
| anita | anita    |

The url to login is [http://localhost:8000/accounts/login](http://localhost:8000/accounts/login) you can go there from the Account navigation link.

The index of the applications shows all the public boards while the Boards navigation link shows the user own boards and the public boards of other users.

## Testing
The functional test implementation has been started so to run them after installation you have to run:
`python manage.py test functional_tests`

## Implementation
I implemented the test project as a Django application and using Django Rest Framework for the API Rest.

### Implemented Features
* Ideas API Rest (Create, Update, Get and Delete)
* Boards API Rest (Create, Update, Get and Delete)
* Used ViewSets (Equivalent to Class Based Views) for all API Views
* Used Django Class bassed views for all the implementation (User signup and login, Board creation and Ideas crud)
* The ideas creation was implemented using javascript and the API Rest.
* Functional tests started for accounts.

### Dependencies
* Python [3.6] (Python Version)
* Django [2.1.7] (Backend Language)
* Django Rest Framework [3.9.2] (API Rest)
* Pipenv [0.3.0] (Virtual enviroment and enviromental variables)
* Selenium [3.141.0], factory_boy[2.11.1] (Functional tests)

## Closing
Thanks for reading this far, I wish you a good day and I'm very looking forward to an interview with you.