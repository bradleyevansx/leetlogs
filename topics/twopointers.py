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
            )
    ]
)