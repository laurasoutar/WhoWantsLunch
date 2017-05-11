# Who Wants Lunch?

## Setup
The application is based on the following framework:
1. Python 3.6.1+
2. Pip 9.0.1+ (included with Python)

When following the installation steps below:
- Ensure you are running a command shell that recognises the `python` and `pip` commands.
- Ensure that you are in the correct directory in order to access [*manage.py*](WhoWantsLunch/manage.py).

### Packages
```sh
pip install -r requirements.txt
```

### Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Settings
Before running the application, please complete the following configuration:
- [*WhoWantsLunch\settings.py*](WhoWantsLunch\WhoWantsLunch\settings.py)
    - `HOST` - the URL where the application is hosted (e.g. *google.com*).
    - `SCHEME` - the protocol used to access the application (e.g. *http*).
    - `SLACK_CLIENT_ID` - the Slack app client ID (found at: *https://api.slack.com/apps/MY-APP-ID/general*)
    - `SLACK_CLIENT_SECRET` - the Slack app client secret (found at: *https://api.slack.com/apps/MY-APP-ID/general*)
- [*SlackBot\apps.py*](WhoWantsLunch\SlackBot\apps.py)
    - `team_key` - the Slack bot user token (found at: *https://api.slack.com/apps/MY-APP-ID/oauth*)

## Run
The following lists each of the commands that can be used to run parts of the application:

### Django
*The web application*
```sh
python manage.py runserver
```