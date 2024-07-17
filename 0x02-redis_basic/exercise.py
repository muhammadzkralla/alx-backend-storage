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
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float,
                                                                    None]:
        """ get impl. """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """ get_str impl. """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ get_int impl. """
        return int.from_bytes(data, sys.byteorder)
