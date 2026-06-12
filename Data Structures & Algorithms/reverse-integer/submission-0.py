class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0: x*=-1; sign=-1

        rev = 0
        while x!=0:
            rev*=10
            rev += x%10
            x//=10
        if sign==-1: rev*=-1

        if rev>pow(2,31)-1 or rev<-pow(2,31): return 0
        else: return rev
            
        