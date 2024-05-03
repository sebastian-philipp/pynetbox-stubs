from typing import Any, Dict, Iterable, List, Optional, Union, overload

from pynetbox._gen import definitions
from pynetbox.core.api import Api
from pynetbox.core.app import App
from pynetbox.core.endpoint import Endpoint
from pynetbox.core.response import Record, RecordSet

class Data_filesEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.DataFile]: ...
    def get(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__empty: Optional[str] = None,
        created__gt: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lt: Optional[str] = None,
        created__lte: Optional[str] = None,
        created__n: Optional[str] = None,
        created_by_request: Optional[str] = None,
        hash: Optional[str] = None,
        hash__empty: Optional[bool] = None,
        hash__ic: Optional[str] = None,
        hash__ie: Optional[str] = None,
        hash__iew: Optional[str] = None,
        hash__isw: Optional[str] = None,
        hash__n: Optional[str] = None,
        hash__nic: Optional[str] = None,
        hash__nie: Optional[str] = None,
        hash__niew: Optional[str] = None,
        hash__nisw: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        last_updated: Optional[str] = None,
        last_updated__empty: Optional[str] = None,
        last_updated__gt: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lt: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        last_updated__n: Optional[str] = None,
        limit: Optional[int] = None,
        modified_by_request: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        path: Optional[str] = None,
        path__empty: Optional[bool] = None,
        path__ic: Optional[str] = None,
        path__ie: Optional[str] = None,
        path__iew: Optional[str] = None,
        path__isw: Optional[str] = None,
        path__n: Optional[str] = None,
        path__nic: Optional[str] = None,
        path__nie: Optional[str] = None,
        path__niew: Optional[str] = None,
        path__nisw: Optional[str] = None,
        q: Optional[str] = None,
        size: Optional[int] = None,
        size__empty: Optional[bool] = None,
        size__gt: Optional[int] = None,
        size__gte: Optional[int] = None,
        size__lt: Optional[int] = None,
        size__lte: Optional[int] = None,
        size__n: Optional[int] = None,
        source: Optional[str] = None,
        source__n: Optional[str] = None,
        source_id: Optional[int] = None,
        source_id__n: Optional[int] = None,
        updated_by_request: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.DataFile]: ...
    def filter(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__empty: Optional[str] = None,
        created__gt: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lt: Optional[str] = None,
        created__lte: Optional[str] = None,
        created__n: Optional[str] = None,
        created_by_request: Optional[str] = None,
        hash: Optional[str] = None,
        hash__empty: Optional[bool] = None,
        hash__ic: Optional[str] = None,
        hash__ie: Optional[str] = None,
        hash__iew: Optional[str] = None,
        hash__isw: Optional[str] = None,
        hash__n: Optional[str] = None,
        hash__nic: Optional[str] = None,
        hash__nie: Optional[str] = None,
        hash__niew: Optional[str] = None,
        hash__nisw: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        last_updated: Optional[str] = None,
        last_updated__empty: Optional[str] = None,
        last_updated__gt: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lt: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        last_updated__n: Optional[str] = None,
        limit: Optional[int] = None,
        modified_by_request: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        path: Optional[str] = None,
        path__empty: Optional[bool] = None,
        path__ic: Optional[str] = None,
        path__ie: Optional[str] = None,
        path__iew: Optional[str] = None,
        path__isw: Optional[str] = None,
        path__n: Optional[str] = None,
        path__nic: Optional[str] = None,
        path__nie: Optional[str] = None,
        path__niew: Optional[str] = None,
        path__nisw: Optional[str] = None,
        q: Optional[str] = None,
        size: Optional[int] = None,
        size__empty: Optional[bool] = None,
        size__gt: Optional[int] = None,
        size__gte: Optional[int] = None,
        size__lt: Optional[int] = None,
        size__lte: Optional[int] = None,
        size__n: Optional[int] = None,
        source: Optional[str] = None,
        source__n: Optional[str] = None,
        source_id: Optional[int] = None,
        source_id__n: Optional[int] = None,
        updated_by_request: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.DataFile]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.DataFile: ...
    @overload
    def create(
        self,
    ) -> definitions.DataFile: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.DataFile: ...
    def update(
        self, objects: Iterable[definitions.DataFile]
    ) -> RecordSet[definitions.DataFile]: ...
    def delete(self, objects: Iterable[definitions.DataFile]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__empty: Optional[str] = None,
        created__gt: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lt: Optional[str] = None,
        created__lte: Optional[str] = None,
        created__n: Optional[str] = None,
        created_by_request: Optional[str] = None,
        hash: Optional[str] = None,
        hash__empty: Optional[bool] = None,
        hash__ic: Optional[str] = None,
        hash__ie: Optional[str] = None,
        hash__iew: Optional[str] = None,
        hash__isw: Optional[str] = None,
        hash__n: Optional[str] = None,
        hash__nic: Optional[str] = None,
        hash__nie: Optional[str] = None,
        hash__niew: Optional[str] = None,
        hash__nisw: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        last_updated: Optional[str] = None,
        last_updated__empty: Optional[str] = None,
        last_updated__gt: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lt: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        last_updated__n: Optional[str] = None,
        limit: Optional[int] = None,
        modified_by_request: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        path: Optional[str] = None,
        path__empty: Optional[bool] = None,
        path__ic: Optional[str] = None,
        path__ie: Optional[str] = None,
        path__iew: Optional[str] = None,
        path__isw: Optional[str] = None,
        path__n: Optional[str] = None,
        path__nic: Optional[str] = None,
        path__nie: Optional[str] = None,
        path__niew: Optional[str] = None,
        path__nisw: Optional[str] = None,
        q: Optional[str] = None,
        size: Optional[int] = None,
        size__empty: Optional[bool] = None,
        size__gt: Optional[int] = None,
        size__gte: Optional[int] = None,
        size__lt: Optional[int] = None,
        size__lte: Optional[int] = None,
        size__n: Optional[int] = None,
        source: Optional[str] = None,
        source__n: Optional[str] = None,
        source_id: Optional[int] = None,
        source_id__n: Optional[int] = None,
        updated_by_request: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class Data_sourcesEndpoint(Endpoint):
    def all(
        self, limit=0, offset=None
    ) -> RecordSet[definitions.DataSource]: ...
    def get(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__empty: Optional[str] = None,
        created__gt: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lt: Optional[str] = None,
        created__lte: Optional[str] = None,
        created__n: Optional[str] = None,
        created_by_request: Optional[str] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        enabled: Optional[bool] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        last_updated: Optional[str] = None,
        last_updated__empty: Optional[str] = None,
        last_updated__gt: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lt: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        last_updated__n: Optional[str] = None,
        limit: Optional[int] = None,
        modified_by_request: Optional[str] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        status__n: Optional[str] = None,
        tag: Optional[str] = None,
        tag__n: Optional[str] = None,
        type: Optional[str] = None,
        type__n: Optional[str] = None,
        updated_by_request: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.DataSource]: ...
    def filter(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__empty: Optional[str] = None,
        created__gt: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lt: Optional[str] = None,
        created__lte: Optional[str] = None,
        created__n: Optional[str] = None,
        created_by_request: Optional[str] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        enabled: Optional[bool] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        last_updated: Optional[str] = None,
        last_updated__empty: Optional[str] = None,
        last_updated__gt: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lt: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        last_updated__n: Optional[str] = None,
        limit: Optional[int] = None,
        modified_by_request: Optional[str] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        status__n: Optional[str] = None,
        tag: Optional[str] = None,
        tag__n: Optional[str] = None,
        type: Optional[str] = None,
        type__n: Optional[str] = None,
        updated_by_request: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.DataSource]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.DataSource: ...
    @overload
    def create(
        self,
        name: str,
        type: str,
        source_url: str,
        enabled: Optional[bool] = None,
        description: Optional[str] = None,
        comments: Optional[str] = None,
        parameters: Optional[Any] = None,
        ignore_rules: Optional[str] = None,
        custom_fields: Optional[Any] = None,
    ) -> definitions.DataSource: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.DataSource: ...
    def update(
        self, objects: Iterable[definitions.DataSource]
    ) -> RecordSet[definitions.DataSource]: ...
    def delete(self, objects: Iterable[definitions.DataSource]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[int] = None,
        created: Optional[str] = None,
        created__empty: Optional[str] = None,
        created__gt: Optional[str] = None,
        created__gte: Optional[str] = None,
        created__lt: Optional[str] = None,
        created__lte: Optional[str] = None,
        created__n: Optional[str] = None,
        created_by_request: Optional[str] = None,
        description: Optional[str] = None,
        description__empty: Optional[bool] = None,
        description__ic: Optional[str] = None,
        description__ie: Optional[str] = None,
        description__iew: Optional[str] = None,
        description__isw: Optional[str] = None,
        description__n: Optional[str] = None,
        description__nic: Optional[str] = None,
        description__nie: Optional[str] = None,
        description__niew: Optional[str] = None,
        description__nisw: Optional[str] = None,
        enabled: Optional[bool] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        last_updated: Optional[str] = None,
        last_updated__empty: Optional[str] = None,
        last_updated__gt: Optional[str] = None,
        last_updated__gte: Optional[str] = None,
        last_updated__lt: Optional[str] = None,
        last_updated__lte: Optional[str] = None,
        last_updated__n: Optional[str] = None,
        limit: Optional[int] = None,
        modified_by_request: Optional[str] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        status__n: Optional[str] = None,
        tag: Optional[str] = None,
        tag__n: Optional[str] = None,
        type: Optional[str] = None,
        type__n: Optional[str] = None,
        updated_by_request: Optional[str] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class JobsEndpoint(Endpoint):
    def all(self, limit=0, offset=None) -> RecordSet[definitions.Job]: ...
    def get(
        self,
        id: Optional[int] = None,
        completed: Optional[str] = None,
        completed__after: Optional[str] = None,
        completed__before: Optional[str] = None,
        created: Optional[str] = None,
        created__after: Optional[str] = None,
        created__before: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        interval: Optional[int] = None,
        interval__empty: Optional[bool] = None,
        interval__gt: Optional[int] = None,
        interval__gte: Optional[int] = None,
        interval__lt: Optional[int] = None,
        interval__lte: Optional[int] = None,
        interval__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        object_id: Optional[int] = None,
        object_id__empty: Optional[bool] = None,
        object_id__gt: Optional[int] = None,
        object_id__gte: Optional[int] = None,
        object_id__lt: Optional[int] = None,
        object_id__lte: Optional[int] = None,
        object_id__n: Optional[int] = None,
        object_type: Optional[int] = None,
        object_type__n: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        scheduled: Optional[str] = None,
        scheduled__after: Optional[str] = None,
        scheduled__before: Optional[str] = None,
        started: Optional[str] = None,
        started__after: Optional[str] = None,
        started__before: Optional[str] = None,
        status: Optional[str] = None,
        status__n: Optional[str] = None,
        user: Optional[int] = None,
        user__n: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> Optional[definitions.Job]: ...
    def filter(
        self,
        id: Optional[int] = None,
        completed: Optional[str] = None,
        completed__after: Optional[str] = None,
        completed__before: Optional[str] = None,
        created: Optional[str] = None,
        created__after: Optional[str] = None,
        created__before: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        interval: Optional[int] = None,
        interval__empty: Optional[bool] = None,
        interval__gt: Optional[int] = None,
        interval__gte: Optional[int] = None,
        interval__lt: Optional[int] = None,
        interval__lte: Optional[int] = None,
        interval__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        object_id: Optional[int] = None,
        object_id__empty: Optional[bool] = None,
        object_id__gt: Optional[int] = None,
        object_id__gte: Optional[int] = None,
        object_id__lt: Optional[int] = None,
        object_id__lte: Optional[int] = None,
        object_id__n: Optional[int] = None,
        object_type: Optional[int] = None,
        object_type__n: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        scheduled: Optional[str] = None,
        scheduled__after: Optional[str] = None,
        scheduled__before: Optional[str] = None,
        started: Optional[str] = None,
        started__after: Optional[str] = None,
        started__before: Optional[str] = None,
        status: Optional[str] = None,
        status__n: Optional[str] = None,
        user: Optional[int] = None,
        user__n: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> RecordSet[definitions.Job]: ...
    @overload
    def create(self, *args: Dict[str, Any]) -> definitions.Job: ...
    @overload
    def create(
        self,
    ) -> definitions.Job: ...
    def create(
        self, *args: Dict[str, Any], **kwargs: Any
    ) -> definitions.Job: ...
    def update(
        self, objects: Iterable[definitions.Job]
    ) -> RecordSet[definitions.Job]: ...
    def delete(self, objects: Iterable[definitions.Job]) -> bool: ...
    def choices(self) -> dict: ...
    def count(
        self,
        id: Optional[int] = None,
        completed: Optional[str] = None,
        completed__after: Optional[str] = None,
        completed__before: Optional[str] = None,
        created: Optional[str] = None,
        created__after: Optional[str] = None,
        created__before: Optional[str] = None,
        id__empty: Optional[bool] = None,
        id__gt: Optional[int] = None,
        id__gte: Optional[int] = None,
        id__lt: Optional[int] = None,
        id__lte: Optional[int] = None,
        id__n: Optional[int] = None,
        interval: Optional[int] = None,
        interval__empty: Optional[bool] = None,
        interval__gt: Optional[int] = None,
        interval__gte: Optional[int] = None,
        interval__lt: Optional[int] = None,
        interval__lte: Optional[int] = None,
        interval__n: Optional[int] = None,
        limit: Optional[int] = None,
        name: Optional[str] = None,
        name__empty: Optional[bool] = None,
        name__ic: Optional[str] = None,
        name__ie: Optional[str] = None,
        name__iew: Optional[str] = None,
        name__isw: Optional[str] = None,
        name__n: Optional[str] = None,
        name__nic: Optional[str] = None,
        name__nie: Optional[str] = None,
        name__niew: Optional[str] = None,
        name__nisw: Optional[str] = None,
        object_id: Optional[int] = None,
        object_id__empty: Optional[bool] = None,
        object_id__gt: Optional[int] = None,
        object_id__gte: Optional[int] = None,
        object_id__lt: Optional[int] = None,
        object_id__lte: Optional[int] = None,
        object_id__n: Optional[int] = None,
        object_type: Optional[int] = None,
        object_type__n: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        q: Optional[str] = None,
        scheduled: Optional[str] = None,
        scheduled__after: Optional[str] = None,
        scheduled__before: Optional[str] = None,
        started: Optional[str] = None,
        started__after: Optional[str] = None,
        started__before: Optional[str] = None,
        status: Optional[str] = None,
        status__n: Optional[str] = None,
        user: Optional[int] = None,
        user__n: Optional[int] = None,
        **kwargs: Optional[Any]
    ) -> int: ...

class CoreApp(App):
    def __init__(self, api: 'Api', name):
        self.data_files: Data_filesEndpoint = ...
        self.data_sources: Data_sourcesEndpoint = ...
        self.jobs: JobsEndpoint = ...
