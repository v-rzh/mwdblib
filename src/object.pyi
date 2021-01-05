from .api import MalwarecageAPI
from typing import Any, Dict, List, Union, Optional
from .comment import MWDBComment
from .share import MWDBShare
from datetime import datetime
from .file import MWDBFile
from .config import MWDBConfig
from .blob import MWDBBlob


class MWDBElement:
    api: MalwarecageAPI = ...
    data: Dict[str, Any] = ...
    def __init__(self, api: MalwarecageAPI, data: Dict[str, Any]) -> None: ...


class MWDBObject(MWDBElement):
    URL_TYPE: str = ...
    TYPE: str = ...
    @staticmethod
    def create(api: MalwarecageAPI, data: Dict[str, Any]) -> Optional[Union[MWDBFile, MWDBConfig, MWDBBlob]]: ...
    @property
    def id(self) -> str: ...
    @property
    def object_type(self) -> str: ...
    @property
    def sha256(self) -> str: ...
    @property
    def tags(self) -> List[str]: ...
    @property
    def comments(self) -> List[MWDBComment]: ...
    @property
    def shares(self) -> List[MWDBShare]: ...
    @property
    def metakeys(self) -> Dict[str, List[str]]: ...
    @property
    def upload_time(self) -> datetime: ...
    @property
    def parents(self) -> List["MWDBObject"]: ...
    @property
    def children(self) -> List["MWDBObject"]: ...
    @property
    def content(self) -> Union[str, bytes]: ...
    def add_child(self, child: Union["MWDBObject", str]) -> None: ...
    def add_tag(self, tag: str) -> None: ...
    def remove_tag(self, tag: str) -> None: ...
    def add_comment(self, comment: str) -> None: ...
    def add_metakey(self, key: str, value: str) -> None: ...
    def share_with(self, group: str) -> None: ...
    data: Dict[str, Any] = ...
    def flush(self) -> None: ...


MalwarecageElement = MWDBElement
MalwarecageObject = MWDBObject
