# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/more_messages.proto

from googlepb.protobuf import descriptor as _descriptor
from googlepb.protobuf import message as _message
from googlepb.protobuf import reflection as _reflection
from googlepb.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/more_messages.proto',
  package='googlepb.protobuf.internal',
  serialized_pb='\n,google/protobuf/internal/more_messages.proto\x12\x18googlepb.protobuf.internal\"h\n\x10OutOfOrderFields\x12\x17\n\x0foptional_sint32\x18\x05 \x01(\x11\x12\x17\n\x0foptional_uint32\x18\x03 \x01(\r\x12\x16\n\x0eoptional_int32\x18\x01 \x01(\x05*\x04\x08\x04\x10\x05*\x04\x08\x02\x10\x03:C\n\x0foptional_uint64\x12*.googlepb.protobuf.internal.OutOfOrderFields\x18\x04 \x01(\x04:B\n\x0eoptional_int64\x12*.googlepb.protobuf.internal.OutOfOrderFields\x18\x02 \x01(\x03')


OPTIONAL_UINT64_FIELD_NUMBER = 4
optional_uint64 = _descriptor.FieldDescriptor(
  name='optional_uint64', full_name='googlepb.protobuf.internal.optional_uint64', index=0,
  number=4, type=4, cpp_type=4, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
OPTIONAL_INT64_FIELD_NUMBER = 2
optional_int64 = _descriptor.FieldDescriptor(
  name='optional_int64', full_name='googlepb.protobuf.internal.optional_int64', index=1,
  number=2, type=3, cpp_type=2, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_OUTOFORDERFIELDS = _descriptor.Descriptor(
  name='OutOfOrderFields',
  full_name='googlepb.protobuf.internal.OutOfOrderFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optional_sint32', full_name='googlepb.protobuf.internal.OutOfOrderFields.optional_sint32', index=0,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optional_uint32', full_name='googlepb.protobuf.internal.OutOfOrderFields.optional_uint32', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optional_int32', full_name='googlepb.protobuf.internal.OutOfOrderFields.optional_int32', index=2,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(4, 5), (2, 3), ],
  serialized_start=74,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['OutOfOrderFields'] = _OUTOFORDERFIELDS

class OutOfOrderFields(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OUTOFORDERFIELDS

  # @@protoc_insertion_point(class_scope:googlepb.protobuf.internal.OutOfOrderFields)

OutOfOrderFields.RegisterExtension(optional_uint64)
OutOfOrderFields.RegisterExtension(optional_int64)

# @@protoc_insertion_point(module_scope)
