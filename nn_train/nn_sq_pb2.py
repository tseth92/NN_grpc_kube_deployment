# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nn_sq.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nn_sq.proto',
  package='nn_sq',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bnn_sq.proto\x12\x05nn_sq\"2\n\tNNRequest\x12\x11\n\toperation\x18\x01 \x01(\x05\x12\x12\n\nmodel_name\x18\x02 \x01(\t\"\x1e\n\nNNResponse\x12\x10\n\x08progress\x18\x01 \x01(\t2I\n\x0eNNTrainPredict\x12\x37\n\x0cPredictModel\x12\x10.nn_sq.NNRequest\x1a\x11.nn_sq.NNResponse\"\x00\x30\x01\x62\x06proto3')
)




_NNREQUEST = _descriptor.Descriptor(
  name='NNRequest',
  full_name='nn_sq.NNRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='nn_sq.NNRequest.operation', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='nn_sq.NNRequest.model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=22,
  serialized_end=72,
)


_NNRESPONSE = _descriptor.Descriptor(
  name='NNResponse',
  full_name='nn_sq.NNResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='progress', full_name='nn_sq.NNResponse.progress', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=74,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['NNRequest'] = _NNREQUEST
DESCRIPTOR.message_types_by_name['NNResponse'] = _NNRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NNRequest = _reflection.GeneratedProtocolMessageType('NNRequest', (_message.Message,), {
  'DESCRIPTOR' : _NNREQUEST,
  '__module__' : 'nn_sq_pb2'
  # @@protoc_insertion_point(class_scope:nn_sq.NNRequest)
  })
_sym_db.RegisterMessage(NNRequest)

NNResponse = _reflection.GeneratedProtocolMessageType('NNResponse', (_message.Message,), {
  'DESCRIPTOR' : _NNRESPONSE,
  '__module__' : 'nn_sq_pb2'
  # @@protoc_insertion_point(class_scope:nn_sq.NNResponse)
  })
_sym_db.RegisterMessage(NNResponse)



_NNTRAINPREDICT = _descriptor.ServiceDescriptor(
  name='NNTrainPredict',
  full_name='nn_sq.NNTrainPredict',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=106,
  serialized_end=179,
  methods=[
  _descriptor.MethodDescriptor(
    name='PredictModel',
    full_name='nn_sq.NNTrainPredict.PredictModel',
    index=0,
    containing_service=None,
    input_type=_NNREQUEST,
    output_type=_NNRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NNTRAINPREDICT)

DESCRIPTOR.services_by_name['NNTrainPredict'] = _NNTRAINPREDICT

# @@protoc_insertion_point(module_scope)
