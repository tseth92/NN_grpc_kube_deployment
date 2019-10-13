FROM tensorflow/tensorflow:latest-py3

RUN mkdir -p /home/nn_predict

RUN apt-get update && apt-get install -y \
    python3-pip
     

COPY . /home/nn_predict/

RUN pip3 install -r /home/nn_predict/requirements.txt

CMD ["python3", "/home/nn_predict/nn_sq_predict_grpc.py"]
