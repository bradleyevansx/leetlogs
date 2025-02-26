class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        absMax = 0
        curr = 0
        for n in nums:
            curr += n
            curr = max(curr, n)
            absMax = max(curr, absMax)
        print(absMax)

        absMin = 0
        curr = 0
        for n in nums:
            curr += n
            curr = min(curr, n)
            absMin = min(curr, absMin)
        return max(abs(absMin), abs(absMax))