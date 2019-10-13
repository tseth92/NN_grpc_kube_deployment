FROM tensorflow/tensorflow:1.14.0-py3

RUN mkdir -p /home/nn_train

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl

COPY . /home/nn_train/

RUN pip3 install -r /home/nn_train/requirements.txt

EXPOSE 5000

CMD ["python", "/home/nn_train/nn_sq_train_grpc.py"]
