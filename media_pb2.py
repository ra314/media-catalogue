# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: media.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='media.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmedia.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"#\n\tCatalogue\x12\x16\n\x06medias\x18\x01 \x03(\x0b\x32\x06.Media\"r\n\x05Media\x12\x0e\n\x06rating\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x04type\x18\x03 \x01(\x0e\x32\n.MediaType\x12\x31\n\rdate_finished\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*O\n\tMediaType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05MOVIE\x10\x01\x12\n\n\x06TVSHOW\x10\x02\x12\x08\n\x04GAME\x10\x03\x12\t\n\x05NOVEL\x10\x04\x12\t\n\x05\x43OMIC\x10\x05\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_MEDIATYPE = _descriptor.EnumDescriptor(
  name='MediaType',
  full_name='MediaType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOVIE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TVSHOW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAME', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOVEL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMIC', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=201,
  serialized_end=280,
)
_sym_db.RegisterEnumDescriptor(_MEDIATYPE)

MediaType = enum_type_wrapper.EnumTypeWrapper(_MEDIATYPE)
UNKNOWN = 0
MOVIE = 1
TVSHOW = 2
GAME = 3
NOVEL = 4
COMIC = 5



_CATALOGUE = _descriptor.Descriptor(
  name='Catalogue',
  full_name='Catalogue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='medias', full_name='Catalogue.medias', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=83,
)


_MEDIA = _descriptor.Descriptor(
  name='Media',
  full_name='Media',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rating', full_name='Media.rating', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Media.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Media.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_finished', full_name='Media.date_finished', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=199,
)

_CATALOGUE.fields_by_name['medias'].message_type = _MEDIA
_MEDIA.fields_by_name['type'].enum_type = _MEDIATYPE
_MEDIA.fields_by_name['date_finished'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Catalogue'] = _CATALOGUE
DESCRIPTOR.message_types_by_name['Media'] = _MEDIA
DESCRIPTOR.enum_types_by_name['MediaType'] = _MEDIATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Catalogue = _reflection.GeneratedProtocolMessageType('Catalogue', (_message.Message,), {
  'DESCRIPTOR' : _CATALOGUE,
  '__module__' : 'media_pb2'
  # @@protoc_insertion_point(class_scope:Catalogue)
  })
_sym_db.RegisterMessage(Catalogue)

Media = _reflection.GeneratedProtocolMessageType('Media', (_message.Message,), {
  'DESCRIPTOR' : _MEDIA,
  '__module__' : 'media_pb2'
  # @@protoc_insertion_point(class_scope:Media)
  })
_sym_db.RegisterMessage(Media)


# @@protoc_insertion_point(module_scope)
