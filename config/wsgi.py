"""
WSGI config for OperonEvoDB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import site

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/virtualenvs/operon-evo-db/local/lib/python2.7/site-packages')

# Activate the virtual env
activate_env = os.path.expanduser("/virtualenvs/operon-evo-db/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
