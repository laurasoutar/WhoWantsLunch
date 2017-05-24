# Who Wants Lunch?

## Application setup
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

## Slack setup
1. Create a new app at: *https://api.slack.com/apps*
2. In the 'Create an App' dialog, give the app a name (e.g. *Who Wants Lunch*) and select the development Slack team where you will be testing the app.
3. Basic Information:
    1. App Credentials: make a note of the **Client ID**, **Client Secret**, and **Verification Token** for later. Note that these must be kept **private**.
    2. Display Information: set the name, description, colour, and image as required.
4. Collborators: add any other Slack users that you wish to allow to make changes to the Slack app.
5. Interactive Messages:
    1. Enable Interactive Messages.
    2. Request URL: set this to: *http://**MY-SERVER-URL**/slack/callback/* (see the Ngrok section below if you don't have one).
    3. Save changes.
6. OAuth & Permissions:
    1. Redirect URLs: Add the following URL: *http://**MY-SERVER-URL**/slack/oauth/* (see the Ngrok section below if you don't have one).
    2. Save URLs.
    2. Permission Scopes: Add the following required scopes:
        * chat:write:bot
        * im:read
        * users:read
7. Bot Users:
    1. Add a Bot User.
    2. Default username: Set this to whatever is required (e.g. *lunchbot*).
    3. Always Show My Bot as Online: Turn this on or off as required.
    4. Add Bot User.
8. Install App:
    1. Install App to Team.

## Run

### Settings
Before running the application, please complete the following configuration in [*WhoWantsLunch/settings.py*](WhoWantsLunch\WhoWantsLunch\settings.py):
- `HOST` - the URL where the application is hosted (e.g. *google.com*). This must be the same URL as used in the Slack setup steps above (see the Ngrok section below if you don't have one).
- `SCHEME` - the protocol used to access the application (e.g. *http*). See above.
- `SLACK_CLIENT_ID` - the Slack app client ID. This can be found in the Slack setup steps above.
- `SLACK_CLIENT_SECRET` - the Slack app client secret. See above.
- `SLACK_VERIFICATION_TOKEN` - the token used to verify that received Slack messages have not been forged. See above.

The following lists each of the commands that can be used to run parts of the application:

### Django
*The web application*
```sh
python manage.py runserver
```

### Ngrok
*Ngrok allows you to test a locally running web application on a temporary Internet-facing server.*
1. Download the latest version of [Ngrok](https://ngrok.com/).
2. Extract the compressed application.
3. Open a command shell in the uncompressed application directory.
4. Enter the following command to run the application:
```sh
.\ngrok.exe http 8000
```
5. Ngrok should now expose the HTTP application running on port 8000 to the Internet. It will notify you of the randomly-generated .ngrok.io address it is using, which you can set in **MY-SERVER-URL** and `HOST` above.