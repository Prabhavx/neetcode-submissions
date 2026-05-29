class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = 2*(len(s))+1
        t = ''
        for i in s:
            t += '#' + i
        t += '#'

        p = [1]*(n)
        l,r = 1,1

        for i in range(n):
            p[i] = max(0, min(r-i, p[l+r-i]))
            while i+p[i]<n and i-p[i]>=0 and t[i-p[i]] == t[i+p[i]]:
                p[i] += 1
            if i+p[i] > r:
                l = i-p[i]
                r = i+p[i]
        
        i = p.index(max(p))
        if i%2==1: 
            return (s[i//2 - (p[i]-1)//2: i//2 + (p[i]-1)//2+1])
        else:
            print(i)
            print(p[i])
            return (s[i//2 - (p[i]-1)//2: i//2+(p[i]-1)//2])




        