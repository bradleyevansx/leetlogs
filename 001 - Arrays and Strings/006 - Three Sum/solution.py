class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            seen = set()
            curr1 = nums[i]
            target = 0 - curr1
            for j in range(i + 1, n):
                curr2 = nums[j]
                if target - curr2 in seen:
                    res.add(tuple([curr1, target - curr2, curr2]))
                seen.add(curr2)
        return [[i[0], i[1], i[2]] for i in res]
