# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x03\x61pi\"\x1c\n\nApiRequest\x12\x0e\n\x06length\x18\x01 \x01(\x05\"!\n\x05Items\x12\x18\n\x05items\x18\x01 \x03(\x0b\x32\t.api.Item\" \n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x18\n\x05Hello\x12\x0f\n\x07message\x18\x01 \x01(\t2\x88\x01\n\x03\x41pi\x12+\n\x08sayHello\x12\x11.api.HelloRequest\x1a\n.api.Hello\"\x00\x12\'\n\x06getAll\x12\x0f.api.ApiRequest\x1a\n.api.Items\"\x00\x12+\n\tgetStream\x12\x0f.api.ApiRequest\x1a\t.api.Item\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_APIREQUEST']._serialized_start=18
  _globals['_APIREQUEST']._serialized_end=46
  _globals['_ITEMS']._serialized_start=48
  _globals['_ITEMS']._serialized_end=81
  _globals['_ITEM']._serialized_start=83
  _globals['_ITEM']._serialized_end=115
  _globals['_HELLOREQUEST']._serialized_start=117
  _globals['_HELLOREQUEST']._serialized_end=145
  _globals['_HELLO']._serialized_start=147
  _globals['_HELLO']._serialized_end=171
  _globals['_API']._serialized_start=174
  _globals['_API']._serialized_end=310
# @@protoc_insertion_point(module_scope)
