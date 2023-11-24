# User Coding assignment App

This Django application provides a simple user management system with Parent and Child user types.

## Prerequisites

- Python 3.x
- Django (install using `pip install Django`)

## Installation and run

1. Clone the repository:

   ```bash
   git clone https://github.com/mahidulmoon/user_management_django.git

2. Change into project directory
   `cd user_management_django`
3. Install the required dependencies:
   `pip install -r requirements.txt`
4. Run migrations to create the database:
   `python manage.py migrate`
5. Run the development server
   `python manage.py runserver`


## API Endpoints

1. Create user: POST `/users/create/`
2. Update user: POST `/users/update/<int:user_id>/`
3. Delete user: POST `/users/delete/<int:user_id>/`

##Running Tests

Run the tests using the following command:
1. `python manage.py test`