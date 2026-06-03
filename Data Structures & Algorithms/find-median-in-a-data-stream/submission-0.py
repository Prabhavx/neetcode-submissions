import heapq
class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        self.mid = 0.0
        heapq.heapify(self.heap1)
        heapq.heapify(self.heap2)
        self.le1 = 0
        self.le2 = 0

    def addNum(self, num: int) -> None:
        if self.le1 == 0:
            self.mid = num
            heapq.heappush(self.heap1, -num)
            self.le1 += 1
            
        elif self.le1 == self.le2:

            if num > self.heap2[0]:
                heapq.heappush(self.heap2, num)
                self.mid = self.heap2[0]
                self.le2 += 1

            else:
                heapq.heappush(self.heap1, -num)
                self.mid = -self.heap1[0]
                self.le1 += 1
        
        else:
            if self.le1 > self.le2:
                heapq.heappush(self.heap1, -num)
                x = -heapq.heappop(self.heap1)
                heapq.heappush(self.heap2, x)
                self.mid = (-self.heap1[0] + self.heap2[0]) / 2
                self.le2 += 1
            else:
                heapq.heappush(self.heap2, num)
                x = heapq.heappop(self.heap2)
                heapq.heappush(self.heap1, -x)
                self.mid = (-self.heap1[0] + self.heap2[0]) / 2
                self.le1 += 1

    def findMedian(self) -> float:
        return self.mid
        