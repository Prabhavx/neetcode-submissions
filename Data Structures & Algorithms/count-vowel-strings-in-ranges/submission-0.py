class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(words)
        req_words = [0]*(n+1)

        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels: req_words[i+1] = 1
        
        for i in range(1,n+1): req_words[i] += req_words[i-1]
        
        res = []
        for start, end in queries:
            res.append(req_words[end+1] - req_words[start])
        
        return res
        