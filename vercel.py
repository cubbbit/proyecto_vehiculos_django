import os
from django.core.wsgi import get_wsgi_application

# Establecer la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Crear el objeto de aplicación WSGI
app = get_wsgi_application()
