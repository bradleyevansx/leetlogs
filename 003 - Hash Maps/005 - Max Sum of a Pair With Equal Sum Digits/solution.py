class Solution:
    def getDigitsSum(self, num):
        digitSum = 0
    
        while num > 0:
            digitSum += num % 10
            num //= 10

        return digitSum
    def maximumSum(self, nums: List[int]) -> int:
        hm = {}
        res = -1
        for num in nums:
            curr = self.getDigitsSum(num)
            
            if curr not in hm:
                hm[curr] = num
            else:
                res = max(res, hm[curr] + num)
                hm[curr] = max(hm[curr], num)
        return res