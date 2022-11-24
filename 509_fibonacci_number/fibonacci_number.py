class Solution:
    def fib(self, n: int) -> int:
        stored = [0,1]
        
        for i in range(2, n + 1):
            stored.append(stored[i - 1] + stored[i - 2])
        
        return stored[n]
