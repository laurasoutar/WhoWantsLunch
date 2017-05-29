"""
WSGI config for WhoWantsLunch project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import locale
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WhoWantsLunch.settings")

locale.setlocale(locale.LC_ALL, "")

application = get_wsgi_application()
