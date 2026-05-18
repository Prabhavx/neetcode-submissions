class StockSpanner:

    def __init__(self):
        self.stk = []        

    def next(self, price: int) -> int:
        if not self.stk: 
            self.stk.append([price,1])
            return 1

        if price<self.stk[-1][0]: self.stk.append([price,1])
        else:
            val = 1
            while self.stk and price>=self.stk[-1][0]:
                val += self.stk.pop()[1]
            self.stk.append([price,val])
        
        return self.stk[-1][1]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)