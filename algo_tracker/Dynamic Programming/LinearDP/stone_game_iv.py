class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        cache = {}
        def dfs(rem):
            
            sq = math.isqrt(rem)
            if rem == 0:
                return True
            if(sq*sq == rem):
                return True
            possible = False
            if rem in cache:
                return cache[rem]
            i = 1
            while i*i<=rem:
                possible = possible or (not dfs(rem-(i*i)))
                i+=1
            cache[rem] = possible
            return cache[rem]
        return dfs(n)