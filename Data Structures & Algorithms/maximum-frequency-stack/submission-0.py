class FreqStack:

    def __init__(self):
        self.freq = {}
        self.grp = [[]for _ in range(20001)]
        self.mxfreq = 0

    def push(self, val: int) -> None:
        if val in self.freq: self.freq[val]+=1
        else: self.freq[val]=1

        self.mxfreq = max(self.mxfreq, self.freq[val])
        self.grp[self.freq[val]].append(val)

    def pop(self) -> int:
        ans = self.grp[self.mxfreq].pop()
        if len(self.grp[self.mxfreq])==0: 
            self.mxfreq-=1
        self.freq[ans]-=1
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()