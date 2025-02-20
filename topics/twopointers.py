from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import Topic


twopointers = Topic(
    "Two Pointers",
    "",
    [],
    "",
    [
        Problem(
                "121",
                "Best Time to Buy and Sell a Stock",
                '''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.''',
                "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
                "Easy",
                ["Arrays", "Dynamic Programming", "Sliding Window"],
                [
                    Example("prices = [7,1,5,3,6,4]", "5"),
                    Example("prices = [7,6,4,3,1]", "0")
                ],
                [Constraint("1 <= prices.length <= 10^5"), Constraint("0 <= prices[i] <= 10^4")],
                Solution(
                    '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
        return res''',
                    "This problem is Easy but has an optimization that can make all the difference in proving your knowledge of DSA. At first glance the brute force solution is to check every combo of indices. But there is a much better solution that is O(n). This beats O(n^2) by a dramatic amount. The thought process with the final code is that as we move through the array we want to check the lowest points with everything. So as we move through the array we just keep track of the lowest point and then update the response if there is a new max. If there is a new lowest point we update it. The reason this works is because as we move through the array the left pointer only matters to the selling points to the right of it. So if there is a new low it can only apply to the selling points that come after it in the array. Therefore, we just keep track of the low and check the profit at each point to the right of it. If we find a new low, we use it for the next days until a new low occurs.",
                    "O(n)",
                    "O(1)"
                )
            ),
            Problem(
                "11",
                "Container With Most Water",
                '''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.''',
                "https://leetcode.com/problems/container-with-most-water/",
                "Medium",
                ["Arrays", "Two Pointers"],
                [
                    Example("height = [1,8,6,2,5,4,8,3,7]", "49"),
                    Example("height = [1,1]", "1"),
                    Example("height = [4,3,2,1,4]", "16"),
                    Example("height = [1,2,1]", "2")
                ],
                [Constraint("n == height.length"), Constraint("2 <= n <= 10^5"), Constraint("0 <= height[i] <= 10^4")],
                Solution(
                    '''class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        res = 0

        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l] * (r - l))
                l += 1
            else:
                res = max(res, height[r] * (r - l))
                r -= 1
        return res''',
                    "This is a two pointer problem. You have to start with pointers at the outside edges of the array. This problem also a has a greedy aspect to it as you are always trying to choose the next best choice and ignore all the others. At each iteration you move the pointer that is the lowest towards the middle. This is with the hopes that there is a higher point to go to that will leader to a greater response. The algorithm is over whent he pointers are right next to each other.",
                    "O(n)",
                    "O(1)"
                )
            ),
            Problem(
                "153",
                "Find Minimum in Rotated Sorted Array",
                '''Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.''',
                "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/",
                "Medium",
                ["Arrays", "Binary Search", "Two Pointer"],
                [
                    Example("nums = [3,4,5,1,2]", "1"),
                    Example("nums = [4,5,6,7,0,1,2]", "0"),
                    Example("nums = [11,13,15,17]", "11")
                ],
                [Constraint("n == nums.length"), Constraint("1 <= n <= 5000"), Constraint("5000 <= nums[i] <= 5000")],
                Solution(
                    '''class Solution:
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
        return nums[l]''',
                    "This problem is a text book binary search problem. You have a criteria as to how you are supposed to change bounds of the valid search area and you continually narrow it down until you've found your target.",
                    "O(logn)",
                    "O(1)"
                )
            )
    ]
)