from typing import Any, Dict, Iterable, List, Optional, Union, overload

from pynetbox._gen import definitions
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import Record, RecordSet

class Endpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[Record]: ...
    def get(
        self,
    ) -> Optional[Record]: ...
    def filter(
        self,
    ) -> RecordSet[Record]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> Record: ...
    @overload
    def create(
        self,
    ) -> Record: ...
    def create(self, *args: Dict[str, Any], **kwargs: Any) -> Record: ...
    def update(self, objects: Iterable[Record]) -> RecordSet[Record]: ...
    def delete(self, objects: Iterable[Record]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
    ) -> int: ...

class StatusApp(App):
    def __init__(self, api: 'Api', name): ...
