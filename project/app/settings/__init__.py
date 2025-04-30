# https://www.geeksforgeeks.org/how-to-manage-local-vs-production-settings-in-django/
import os

env = os.environ.get('DJANGO_ENV', 'develop')

if env == 'production':
    from .production import *
else:
    from .develop import *
