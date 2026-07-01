class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        weight_sum = []
        for i in range(n-1):
            weight_sum.append(weights[i]+weights[i+1])
        weight_sum.sort()
        return sum(weight_sum[n-k:]) - sum(weight_sum[:k-1])
        