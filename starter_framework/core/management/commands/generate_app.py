import os
from django.core.management.base import BaseCommand, CommandError

APP_CONFIG_TEMPLATE = '''from django.apps import AppConfig

class {class_name}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'starter_framework.apps.{app_name}'
'''

MODELS_TEMPLATE = '''from django.db import models

# Create your models here.
'''

URLS_TEMPLATE = '''from django.urls import path

urlpatterns = [
    # path('', SomeController.as_view({'get': 'list'})),
]
'''

def create_file(path, content=''):
    with open(path, 'w') as f:
        f.write(content)

class Command(BaseCommand):
    help = 'Generate a new app under starter_framework/apps with simplified structure'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str)

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        class_name = app_name.capitalize()
        base_path = f'starter_framework/apps/{app_name}'

        if os.path.exists(base_path):
            raise CommandError(f"App '{app_name}' already exists.")

        os.makedirs(base_path)

        create_file(f'{base_path}/__init__.py')
        create_file(f'{base_path}/models.py', MODELS_TEMPLATE)
        create_file(f'{base_path}/views.py')
        create_file(f'{base_path}/services.py')
        create_file(f'{base_path}/dtos.py')
        create_file(f'{base_path}/urls.py', URLS_TEMPLATE)
        create_file(f'{base_path}/admin.py')
        create_file(f'{base_path}/tests.py')
        create_file(f'{base_path}/apps.py', APP_CONFIG_TEMPLATE.format(app_name=app_name, class_name=class_name))

        self.stdout.write(self.style.SUCCESS(f"App '{app_name}' scaffolded successfully."))
