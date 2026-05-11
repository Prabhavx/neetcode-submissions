class MyHashSet:

    def __init__(self):
        l = [0]*(10**6+1)
        self.l = l

    def add(self, key: int) -> None:
        self.l[key]=1

    def remove(self, key: int) -> None:
        self.l[key]-=1

    def contains(self, key: int) -> bool:
        if self.l[key]==1: return True
        else: return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)