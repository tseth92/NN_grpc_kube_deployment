FROM tensorflow/tensorflow:latest-py3

RUN mkdir -p /home/nn_predict

RUN apt-get update && apt-get install -y \
    python3-pip
    

RUN pip3 install numpy matplotlib keras flask flask-api 

COPY . /home/nn_predict/

CMD ["python3", "/home/nn_predict/nn_sq_predict_grpc.py"]
