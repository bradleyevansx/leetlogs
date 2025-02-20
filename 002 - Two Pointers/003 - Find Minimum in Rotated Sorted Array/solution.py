class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n - 1
        mid = None
        rightMost = nums[-1]

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] > rightMost:
                l = mid + 1
            else: 
                r = mid 
        return nums[l]