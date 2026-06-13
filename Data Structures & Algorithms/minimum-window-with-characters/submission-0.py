class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def compare_arr(a,b):
            for i,j in zip(a,b):
                if i<j: return False
            return True
        
        t_freq = [0]*(60)
        for i in t: t_freq[ord(i)-65]+=1

        n = len(s)
        i,j = 0,0
        s_freq = [0]*(60)
        min_i, min_j = 0,n+1

        while i<n:
            if compare_arr(s_freq, t_freq) == False: 
                if j == n: break
                s_freq[ord(s[j])-65] += 1
                j += 1
            else:
                if j-i < min_j-min_i: min_j, min_i = j,i
                s_freq[ord(s[i])-65] -= 1
                i += 1

        return "" if min_j == n+1 else s[min_i: min_j]