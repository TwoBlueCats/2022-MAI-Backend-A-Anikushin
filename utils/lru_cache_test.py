from lru_cache import LRUCache


class TestLRUCache:
    def test_simple(self):
        cache = LRUCache(100)
        cache.set('Jesse', 'Pinkman')
        cache.set('Walter', 'White')
        cache.set('Jesse', 'James')
        assert cache.get('Jesse') == "James"
        cache.rem('Walter')
        assert cache.get('Walter') == ""

    def test_overflow(self):
        cache = LRUCache(2)
        cache.set("one", "one")
        cache.set("two", "two")
        cache.set("three", "three")

        assert cache.get("one") == ""
        assert cache.get("two") == "two"
        assert cache.get("three") == "three"
