# OAuth-security-app
An application that allows you to authenticate using Gsuite's OAuth servers and saves user's info, including IPs.

Its made in Django, using the app https://github.com/python-social-auth/social-app-django, of python-social-auth ecosystem, for communication with the google-OAuth backend .
Configuration happens within the app's settings.py in a section described OAuth config.

Use Django's admin interface to see info about the users. IPs are at the buttom.
