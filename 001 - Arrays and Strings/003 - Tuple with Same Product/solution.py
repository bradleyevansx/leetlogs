class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        hm = {}

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] * nums[j] in hm:
                    count, pairs =  hm[nums[i] * nums[j]]

                    hm[nums[i] * nums[j]] = (count + 1, pairs + count)
                else:
                    hm[nums[i] * nums[j]] = (1, 0)
        
        res = 0

        for key in hm:
            count, pairs = hm[key]
            res += pairs * 8 
            
        return res