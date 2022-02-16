
from aenum import Enum
import time


class CacheSize(Enum):
    DEFAULT = 20


class CacheEntry:

    k = None
    v = None
    created_at = None
    last_used_at = None

    def __init__(
            self,
            _k,
            _v):
        self.k = _k
        self.v = _v

    def update_created_at(self):
        current = time.time()
        self.created_at = current
        self.last_used_at = current

    def update_last_used_at(self):
        current = time.time()
        self.last_used_at = current


class Cache:

    kv: dict = None
    size: int = CacheSize.DEFAULT

    def __init__(
            self,
            _size: int = None):
        if _size:
            self.size = _size

        self.kv = {}

    def insert(
            self,
            entry: CacheEntry):
        if len(self.kv) < self.size:
            self.kv[entry.k] = entry.v
            entry.update_created_at()

        else:
            # evict
            pass



