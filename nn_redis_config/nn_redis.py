import redis

redis_db = redis.StrictRedis(host="nn-sq-svc", port=6379, db=0)
print(redis_db.keys())
redis_db.set('n_samples',100000)
redis_db.set('epochs', 150)
redis_db.set('batch_size', 1000)
redis_db.set('mid_range', 10)
