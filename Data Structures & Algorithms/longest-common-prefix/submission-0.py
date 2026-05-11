class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def CommonPrefix(s1, s2):
            n = min(len(s1), len(s2))
            i=0
            while i<n:
                if s1[i]==s2[i]: i+=1
                else: break
            return s1[:i]
        
        ans = strs[0]
        n = len(strs)
        for i in range(1,n):
            ans = CommonPrefix(ans, strs[i])
        return ans