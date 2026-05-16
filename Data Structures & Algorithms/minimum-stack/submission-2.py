class MinStack:

    def __init__(self):
        self.l = []
        self.pref_min = [10**19]

    def push(self, val: int) -> None:
        self.l.append(val)
        self.pref_min.append(min(self.pref_min[-1], val))

    def pop(self) -> None:
        self.l.pop()        
        self.pref_min.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        if len(self.pref_min) == 1: return NULL
        return self.pref_min[-1]
        
