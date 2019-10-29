# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import nn_sq_pb2 as nn__sq__pb2


class NNTrainPredictStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PredictModel = channel.unary_stream(
        '/nn_sq.NNTrainPredict/PredictModel',
        request_serializer=nn__sq__pb2.NNRequest.SerializeToString,
        response_deserializer=nn__sq__pb2.NNResponse.FromString,
        )


class NNTrainPredictServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PredictModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NNTrainPredictServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PredictModel': grpc.unary_stream_rpc_method_handler(
          servicer.PredictModel,
          request_deserializer=nn__sq__pb2.NNRequest.FromString,
          response_serializer=nn__sq__pb2.NNResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nn_sq.NNTrainPredict', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
