from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Sensor(_message.Message):
    __slots__ = ("_id", "data_type")
    _ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    _id: int
    data_type: str
    def __init__(self, _id: _Optional[int] = ..., data_type: _Optional[str] = ...) -> None: ...

class StringMessage(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class MeanRequest(_message.Message):
    __slots__ = ("_id", "data_type")
    _ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    _id: int
    data_type: str
    def __init__(self, _id: _Optional[int] = ..., data_type: _Optional[str] = ...) -> None: ...
