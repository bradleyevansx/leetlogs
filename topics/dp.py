from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import Topic


dp = Topic(
    "Dynamic Programming",
    "",
    [],
    "",
    [
        Problem(
            "1749",
            "Maximum Absolute Sum of Any Subarray",
            '''You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.
''',
            "https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/",
            "Medium",
            ["Arrays", "Dynamic Programming"],
            [Example("nums = [1, -3, 2, 3, -4]", "5"), Example("nums = [2, -5, 1, -4, 3, -2]", "8")],
            [Constraint("1 <= nums.length <= 10^5"), Constraint("-10^4 <= nums[i] <= 10^4")],
            Solution(
                '''class Solution:
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
        return max(abs(absMin), abs(absMax))''',
                "This problem is a variation of Kadane's algorithm. Essentially with the standrad Kadane's algo we would get the maximum subarray. Since we need the max abs() subarray we should just do a second pass through of the input with a modified Kadane's algo to get the minimum subarray. And the result would me the max between the abs() of the two.",
                "O(n)",
                "O(1)"
            )

        )
    ]
)