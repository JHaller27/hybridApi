from typing import Any, Union
import redis
import os


class Cache:
    def __init__(self) -> None:
        seconds_per_minute = 60
        minutes_per_hour = 60
        self._timeout = seconds_per_minute * minutes_per_hour * 1

        redis_uri = os.environ.get("QOVERY_REDIS_Z7EF0B380_HOST", "localhost")
        redis_port = os.environ.get("QOVERY_REDIS_Z7EF0B380_PORT", "7777")
        redis_db_name = os.environ.get("QOVERY_REDIS_Z7EF0B380_DEFAULT_DATABASE_NAME", "0")
        redis_uname = os.environ.get("QOVERY_REDIS_Z7EF0B380_LOGIN", None)
        redis_passwd = os.environ.get("QOVERY_REDIS_Z7EF0B380_PASSWORD", None)

        try:
            self._redis = redis.Redis(host=redis_uri, port=redis_port, db=redis_db_name, password=redis_passwd, username=redis_uname)
            self._redis.flushall()
        except redis.exceptions.ConnectionError:
            print("Failed to connect to redis")

    def get(self, key: str) -> Union[Any, None]:
        if self._redis is None:
            return None

        try:
            return self._redis.get(key)
        except redis.exceptions.ConnectionError:
            return None

    def set(self, key: str, value: Any) -> bool:
        if self._redis is None:
            return False

        try:
            return self._redis.set(key, value, ex=self._timeout)
        except redis.exceptions.ConnectionError:
            return False
