from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class BaseAPIController(ViewSet):
    service_class = None  # to be overridden

    def get_service(self):
        if not self.service_class:
            raise NotImplementedError("Set service_class in your controller")
        return self.service_class()
