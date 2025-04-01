from typing import Type, TypeVar
from django.db.models import Model

T = TypeVar('T', bound=Model)

class BaseRepository:
    def __init__(self, model: Type[T]):
        self.model = model

    def get(self, **kwargs) -> T:
        return self.model.objects.get(**kwargs)

    def filter(self, **kwargs):
        return self.model.objects.filter(**kwargs)
