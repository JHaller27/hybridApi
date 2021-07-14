from typing import Any, Union
import redis
import os


class Cache:
    def __init__(self) -> None:
        seconds_per_minute = 60
        minutes_per_hour = 60
        self._timeout = seconds_per_minute * minutes_per_hour * 1

        redis_uri = os.environ.get("QOVERY_DATABASE_CALL_CACHE_CONNECTION_URI", "localhost")
        redis_port = os.environ.get("QOVERY_DATABASE_CALL_CACHE_PORT", "7777")

        try:
            self._redis = redis.Redis(host=redis_uri, port=redis_port, db=0)
            self._redis.flushall()
        except redis.exceptions.ConnectionError:
            print("Failed to connect to redis")

    def get(self, key: str) -> Union[Any, None]:
        if self._redis is None:
            return None

        return self._redis.get(key)

    def set(self, key: str, value: Any) -> bool:
        if self._redis is None:
            return False

        return self._redis.set(key, value, ex=self._timeout)
