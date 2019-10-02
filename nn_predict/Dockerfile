FROM tensorflow/tensorflow

RUN mkdir -p /home/nn_train

RUN apt-get update && apt-get install -y \
    python3-pip
    

RUN pip3 install numpy matplotlib 

COPY . /home/nn_train/

CMD ["python3", "/home/nn_train/nn_sq_predict_grpc.py"]
