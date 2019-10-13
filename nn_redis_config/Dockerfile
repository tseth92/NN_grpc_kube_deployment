FROM redislabs/redis-py


RUN mkdir -p /home/nn_redis_config

RUN apt-get update && apt-get install -y \
   python3-pip \
    curl

RUN pip3 install redis 

COPY . /home/nn_redis_config

CMD ["python3", "/home/nn_redis_config/nn_redis.py"]
