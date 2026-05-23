from bisect import bisect
class TimeMap:
    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d: self.d[key].append((timestamp, value))
        else: self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        else:
            indx = bisect(self.d[key],(timestamp,chr(127)))
            if indx == 0: return ""
            else: return self.d[key][indx-1][1]
        
