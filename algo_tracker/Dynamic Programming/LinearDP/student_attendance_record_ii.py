from functools import lru_cache
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = int(1e9+7)
        @lru_cache()
        def get_possibs(i , last_a, total_late):
            if(last_a >= 3): return 0
            if(total_late >= 2): return 0
            if i == n:
                a = 1
                if(last_a < 2):
                    a+=1
                if total_late <1:
                    a+=1
                return a
            

            ans = 0
            ans = get_possibs(i+1, 0, total_late)
            ans %= mod
            ans += get_possibs(i+1, last_a+1, total_late)
            ans%=mod
            ans += get_possibs(i+1, 0, total_late+1)
            ans%=mod
            return ans

        return get_possibs(1, 0, 0)