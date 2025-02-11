class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = float("-inf"), 0

        for num in nums:
            curr += num
            curr = max(curr, num)
            res = max(curr, res)
        return res