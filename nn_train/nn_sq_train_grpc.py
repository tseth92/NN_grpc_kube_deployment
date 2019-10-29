# -*- coding: utf-8 -*-
"""neural_network square.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tseth92/NeuralNet_Square/blob/master/neural_network_square.ipynb
"""

'''Training a neural network to predict the square of a number'''
import numpy as np
import matplotlib.pyplot as pp
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers.core import Dense
from keras import backend
import pickle
import time
import grpc
from flask import request
from flask import Response
from flask import json
from flask_api import FlaskAPI
from flask import Response
import nn_sq_pb2_grpc
import nn_sq_pb2
import threading
import multiprocessing
from multiprocessing import Process, Manager
import os
import redis
'''configurations for neural net'''

APP = FlaskAPI(__name__)

'''creates random samples of n_samples rows which are between 0 to 1.
mid_range decides the range under which the samples will be created.'''
def get_data(n_samples, mid_range):
  X = np.random.random((n_samples,1))*mid_range-(mid_range/2)
  # eg. if n_samples = 10000, mid_range = 10 then it will create samples b/w
  # 0 and 5 positive and negative
  y = X*X
  #print(X)
  return X,y

''' creating the neural net model of 1:20:1; relu activation, mse as loss and
adam optimizer'''
def get_model():
  model = Sequential()
  model.add(Dense(20, input_shape=(1,), activation='relu'))
  model.add(Dense(1))
  print(model.summary())
  model.compile(loss='mse', optimizer='adam')
  return model

''' train the model for specified number of epochs, batch_size'''
@APP.route("/trainNNSq", methods=['GET'])
def train_model():
  print('in train model')
  #return "hello"
  manager = Manager()
  m_dict = manager.dict()
  n_samples = 100000 # number of samples between 0 and mid_range
  epochs = 20
  batch_size = 1000
  mid_range = 10 # range within which data is required
  #IP = 'nn-sq-predict-svc'
  IP = 'localhost'
  PORT = ':5001'
  response = 'Failure'
  X,y = get_data(n_samples, mid_range)
  #pp.figure(figsize=(10,3))
  #pp.plot(X,y,'.')
  model = get_model()
  validation_split = 0.2
  verbose = 1
  queue = multiprocessing.Queue()
  t1 = Process(target = fit_model, args=(model, X, y, validation_split, epochs, batch_size, verbose, queue, m_dict))
  t1.start()
  t1.join()
  print('going to dump model')
  model_name = m_dict['model_name']
  print('model_name_received: ', model_name)
 
  #//////////////// GRPC CALL ////////////////#
  channel = grpc.insecure_channel(IP+PORT)
  #with grpc.insecure_channel(IP+PORT) as channel:
  print('in with')
  stub = nn_sq_pb2_grpc.NNTrainPredictStub(channel)
  pred_request = nn_sq_pb2.NNRequest(operation=2,model_name='nn_sq_'+model_name)
  print(pred_request)
  def yield_response(pred_request):
    print('in yield_response')
    for resp in stub.PredictModel(pred_request):
      print(resp.progress)
      yield str(resp.progress)+'\n'
  print('going to call yield_response')
  return Response(yield_response(pred_request))
  #return 'hello'

def fit_model(model, X, y, validation_split, epochs, batch_size, verbose, queue, m_dict):
  print('pid child is: ', os.getpid())
  h = model.fit(X, y, validation_split=0.2,
               epochs=epochs,
               batch_size=batch_size,
               verbose=1)
  model_name = str(time.time()).split('.')[0]
  print('putting to queue_model_name', model_name)
  queue.put('nn_sq_'+model_name)
  m_dict['model_name'] = model_name
  pickle.dump(model, open('/mnt/nn-disk/nn_sq_'+model_name, 'wb'))
  

if __name__ == '__main__' :
  print('in main')
  APP.run(host='0.0.0.0', port=5000)
