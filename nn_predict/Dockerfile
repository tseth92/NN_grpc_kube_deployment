FROM tensorflow/tensorflow:1.14.0-py3

RUN mkdir -p /home/nn_predict

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl

COPY . /home/nn_predict/

RUN pip3 install -r /home/nn_predict/requirements.txt


EXPOSE 5001

CMD ["python3", "/home/nn_predict/nn_sq_predict_grpc.py"]
