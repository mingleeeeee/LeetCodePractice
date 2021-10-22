class MyHashSet:

    def __init__(self):
        self.MyHashSet=set()

    def add(self, key: int) -> None:
        self.MyHashSet.add(key)

    def remove(self, key: int) -> None:
        self.MyHashSet.discard(key)
        #remove() will cause error if the item is not exist
    def contains(self, key: int) -> bool:
        if {key}.intersection(self.MyHashSet):
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)