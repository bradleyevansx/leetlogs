class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        rightMost = nums[n - 1]
        mid = None
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > rightMost:
                l = l + 1
            elif nums[mid] < rightMost:
                r = r - 1

        if mid == None:
            return 0 if nums[0] == target else -1
        
        if target >= nums[0] and target <= nums[mid]:
            l, r = 0, mid
        else:
            l, r = mid + 1, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1