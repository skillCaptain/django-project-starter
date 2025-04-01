import os
from django.core.management.base import BaseCommand


def snake_case(name):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


CONTROLLER_TEMPLATE = '''

# --- {model_name} Controller ---
from rest_framework.response import Response
from rest_framework import status
from core.base import BaseAPIController
from .services import {model_name}Service
from .dtos import {model_name}CreateDTO


class {model_name}Controller(BaseAPIController):
    service_class = {model_name}Service

    def create(self, request):
        dto = self.get_service().create(request.data)
        return Response(dto.model_dump(), status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        dto = self.get_service().retrieve(pk)
        return Response(dto.model_dump(), status=status.HTTP_200_OK)
'''

SERVICE_TEMPLATE = '''

# --- {model_name} Service ---
from starter_framework.apps.{app_name}.models import {model_name}
from core.base import AbstractCRUDService
from .dtos import {model_name}CreateDTO, {model_name}ResponseDTO


class {model_name}Service(AbstractCRUDService[{model_name}ResponseDTO]):
    def create(self, data):
        dto = {model_name}CreateDTO(**data)
        instance = {model_name}.objects.create(**dto.model_dump())
        return {model_name}ResponseDTO.model_validate(instance)

    def retrieve(self, obj_id):
        instance = {model_name}.objects.get(pk=obj_id)
        return {model_name}ResponseDTO.model_validate(instance)
'''

DTO_TEMPLATE = '''

# --- {model_name} DTOs ---
from pydantic import BaseModel
from typing import Optional


class {model_name}CreateDTO(BaseModel):
    name: str  # change as needed

    class Config:
        from_attributes = True


class {model_name}ResponseDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
'''


class Command(BaseCommand):
    help = 'Generate CRUD code (views, services, dtos) for a given model inside an app (simplified structure)'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Name of the app inside apps/')
        parser.add_argument('model_name', type=str, help='Model name in PascalCase (e.g., Post)')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        model_name = kwargs['model_name']
        app_path = f'starter_framework/apps/{app_name}'

        if not os.path.exists(app_path):
            self.stderr.write(self.style.ERROR(f"App '{app_name}' does not exist at {app_path}."))
            return

        # Append to each target file
        files = {
            'views.py': CONTROLLER_TEMPLATE,
            'services.py': SERVICE_TEMPLATE,
            'dtos.py': DTO_TEMPLATE,
        }

        for filename, template in files.items():
            path = os.path.join(app_path, filename)
            with open(path, 'a') as f:
                f.write(template.format(model_name=model_name, app_name=app_name))

        self.stdout.write(self.style.SUCCESS(f"CRUD for {model_name} added to app '{app_name}'."))
