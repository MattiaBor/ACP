# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\tqualsiasi\"\x1f\n\x04Msg1\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x13\n\x04Msg2\x12\x0b\n\x03msg\x18\x01 \x01(\t2g\n\x07Service\x12-\n\tServizio1\x12\x0f.qualsiasi.Msg1\x1a\x0f.qualsiasi.Msg2\x12-\n\tServizio2\x12\x0f.qualsiasi.Msg2\x1a\x0f.qualsiasi.Msg1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MSG1']._serialized_start=28
  _globals['_MSG1']._serialized_end=59
  _globals['_MSG2']._serialized_start=61
  _globals['_MSG2']._serialized_end=80
  _globals['_SERVICE']._serialized_start=82
  _globals['_SERVICE']._serialized_end=185
# @@protoc_insertion_point(module_scope)