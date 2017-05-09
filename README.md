# Who Wants Lunch?

## Setup
The application is based on the following framework:
1. Python 3.6.1+
2. Pip 9.0.1+ (included with Python)

When following the installation steps below:
- Ensure you are running a command shell that recognises the `python` and `pip` commands.
- Ensure that you are in the correct directory in order to access [manage.py](WhoWantsLunch/manage.py).

### Packages
```sh
pip install -r requirements.txt
```
### Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

## Run
The following lists each of the commands that can be used to run parts of the application:

### Django
*The web application*
```sh
python manage.py runserver
```