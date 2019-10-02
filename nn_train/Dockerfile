FROM tensorflow/tensorflow:latest-py3

RUN mkdir -p /home/nn_train

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl

RUN pip3 install numpy matplotlib keras flask flask_api redis

COPY . /home/nn_train/

CMD ["python", "/home/nn_train/nn_sq_train_grpc.py"]
