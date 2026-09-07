# time complexity : O(N)
# space complexity : O(1)
class HouseRobber:
    def rob(self, nums: list[int]) -> int:
        s0 = 0
        s1 = 0
        for i in nums:
            new_s0 = max(s0,s1)
            new_s1 = max(s0+i,s1)
            s0 = new_s0
            s1 = new_s1
        return max(s0, s1)