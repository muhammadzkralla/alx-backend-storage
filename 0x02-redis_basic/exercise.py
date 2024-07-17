#!/usr/bin/env python3
""" Redis Basics. """

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store impl. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
