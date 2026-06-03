from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*(26)
        for i in tasks:
            freq[ord(i)-65]+=1
        freq.sort(reverse = True)
        ans = (freq[0]-1)*n
        for i in range(1,26):
            ans -= min(freq[0]-1, freq[i])
            
        return len(tasks) + max(0,ans)
        