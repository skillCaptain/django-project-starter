from typing import Generic, TypeVar, Dict

T = TypeVar('T')

class AbstractCRUDService(Generic[T]):
    def create(self, data: Dict) -> T:
        raise NotImplementedError

    def retrieve(self, obj_id) -> T:
        raise NotImplementedError

    def update(self, obj_id, data: Dict) -> T:
        raise NotImplementedError

    def delete(self, obj_id) -> None:
        raise NotImplementedError
