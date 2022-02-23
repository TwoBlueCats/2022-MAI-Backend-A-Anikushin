from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self._cap = capacity

        self._data = OrderedDict()

    def get(self, key: str) -> str:
        if key not in self._data:
            return ""
        self._data.move_to_end(key, last=True)
        return self._data[key]

    def set(self, key: str, value: str) -> None:
        self._data[key] = value
        self._data.move_to_end(key, last=True)
        if len(self._data) > self._cap:
            self._data.popitem(last=False)

    def rem(self, key: str) -> None:
        if key in self._data:
            self._data.pop(key)
