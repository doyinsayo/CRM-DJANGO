"""
WSGI config for CRMPROJECT project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRMPROJECT.settings')


import django
django.setup()

from django.core.management import call_command

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

