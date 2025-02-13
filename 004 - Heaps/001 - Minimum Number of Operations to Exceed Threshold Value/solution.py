class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)

        while nums[0] < k:
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)

            newVal = (min1 * 2) + min2

            heapq.heappush(nums, newVal)
            res += 1
        return res