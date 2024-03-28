import redis
import json


class RedisCache:

    def __init__(self, host, port, password=None) -> None:

        self.redis_connector = redis.Redis(
            host=host,
            port=port,
            password=password
        )

    def __call__(self):

        if self.redis_connector.ping():
            return self.redis_connector

    def __str__(self) -> str:
        return f"Connected with {self.redis_connector}"

    def __getitem__(self):
        return self.redis_connector

    def __del__(self):

        try:
            self.redis_connector.close()

        except redis.exceptions.RedisError:
            pass


def get_cache(key, redis_cache):

    try:
        redis_result = redis_cache.get(key)
        return json.loads(redis_result) if redis_result else None

    except redis.exceptions.RedisError:
        return None


def set_cache(key, value, redis_cache, expiry=86400):

    try:
        redis_cache.set(key, json.dumps(value), expiry)
        return True

    except redis.exceptions.RedisError:
        return False
