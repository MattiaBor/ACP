from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Item(_message.Message):
    __slots__ = ("id", "prodotto")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODOTTO_FIELD_NUMBER: _ClassVar[int]
    id: int
    prodotto: str
    def __init__(self, id: _Optional[int] = ..., prodotto: _Optional[str] = ...) -> None: ...

class Stringmessage(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
