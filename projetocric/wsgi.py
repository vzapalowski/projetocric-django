"""
WSGI config for projetocric project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetocric.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

