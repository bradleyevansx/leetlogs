from typing import List

from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import SubTopic, Topic
from sdk.utils.filecrud import init
from sdk.utils.topics import handleTopic

topics: List[Topic] = [
    Topic(
        "Arrays and Strings", 
        "Arrays and Strings are two of the most commonly used data structures. Therefore, it is important to be familiar with all of the different ways you can use them. Arrays are the data structure you look to when you want a convenient way to store groups of information. Strings are the data structure most commonly know for storing arrays of characters, otherwise known as words.",
        [
            SubTopic(
                "Basics of accessing elements within a Array/String",
                "The most basic operation you can do with an array is to access an element at a specific index. This is done by using the square brackets operator. For example, if you have an array called `arr`, you can access the first element by using `arr[0]`.",
                []
            ),
        ],
        "Arrays and Strings are the building blocks used in many algorithms you will interact with on a daily basic. Getting familiar with all the different algorithms related to these data structures will help you greatly in the long run.",
        [
            Problem(
                "1790",
                "Check if One String Swap Can Make Strings Equal",
                "You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices. Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.",
                "https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/",
                "Easy",
                ["Hash Table", "String", "Counting"],
                [
                    Example(
                        's1 = "bank", s2 = "kanb"',
                        'True'  
                    ),
                    Example(
                        's1 = "attack", s2 = "defend"',
                        'False'
                    ),
                    Example(
                        's1 = "kelb", s2 = "kelb"',
                        'True'
                    )
                ],
                [
                    Constraint("1 <= s1.length, s2.length <= 100"),
                    Constraint("s1.length == s2.length"),
                    Constraint("s1 and s2 consist of only lowercase English letters"),
                ],
                Solution(
                    """class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        res = 0
        h1, h2 = set(), set()

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                h1.add(s1[i])
                h2.add(s2[i])
                res += 1
        
        if res == 0 or res == 2:
            if h1 == h2:
                return True
        return False""",
                    "The solution is to check if the two strings are equal. If they are, return True. Otherwise, find the indexes of the characters that are different and store them in a list. If the length of the list is not 2, return False. Otherwise, check if the characters at the indexes in the list are equal. If they are, return True. Otherwise, return False.",
                    "O(n)",
                    "O(n)"
                )
            ),
            Problem(
                "1863",
                "Sum of All Subset XOR Totals",
                "The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty. Given an array nums, return the sum of all XOR totals for every subset of nums. Note: Subsets with the same elements should be counted multiple times.",
                "https://leetcode.com/problems/sum-of-all-subset-xor-totals",
                "Easy",
                ["Arrays", "Math", "Backtracking", "Combinatorics"],
                [
                    Example("nums = [1,3]", "6"),
                    Example("nums = [5,1,6]", "28"),
                    Example("nums = [3,4,5,6,7,8]", "480")
                ],
                [
                    Constraint("1 <= nums.length <= 12"),
                    Constraint("1 <= nums[i] <= 20")
                ],
                Solution('''class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def generateSubsets(i, subset):
            if i == len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[i])
            generateSubsets(i + 1, subset)

            subset.pop()
            generateSubsets(i + 1, subset)

        generateSubsets(0, [])

        res = 0

        for sub in subsets:
            curr = 0
            for n in sub:
                curr = curr ^ n

            res += curr

        return res''', 
        "The heart of this problem really lies in the backtracking part where you generate all the subset combinations for the array. I do this recursively. In this case the decision at each node of the decision tree is to add the current index or to not add it. Add the leafs of the tree you have all the different subsets. Then from there you can just iterate over the subsets and get the XOR of all the elements in each subset and add it to the response. This solution will be beat out by all the people who use the solution where you use the sum and length of the array to do fancy math and get the answer without any manipulation of the data structure.",
        "O(2^n * n)",
        "O(2^n * n)"
        )
            ),
            Problem(
                "1726",
                "Tuple with Same Product",
                "Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.",
                "https://leetcode.com/problems/tuple-with-same-product/",
                "Medium",
                ["Array", "Hash Table", "Counting"],
                [
                    Example("nums = [2,3,4,6]", "8"),
                    Example("nums = [1,2,4,5,10]", "16")
                ],
                [
                    Constraint("1 <= nums.length <= 1000"),
                    Constraint("1 <= nums[i] <= 104"),
                    Constraint("All elements in nums are distinct."),
                ],
                Solution(
                    '''class Solution:
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
            
        return res''',
        "The core of this solution is the math involved with determining how many pairs you can make out of the total amount of the total amount of Tuples that equal the given product. So our strategy is to have a hashmap that keeps track of the different products you can achieve by checking each pair of integers in the array. From each pair we will increase the count of elements that have this product by one. With each count is a number of pairs that we can make from that count. Each time we increase the count we increase the amount of pairs by the count of products we previously had. This allows us to simply find the products that have a count > 1 in the hashmap and multiply the pairs associated with those pairs by 8. Add up all of these results and return it. A factor that plays into our favor is that each element in nums is disctinct. The space complexity of this is O(n^2) but that is the worst case. In practice this algorithm would be much more efficient than that. However, the high time complexity is unavoidable. We are required to check the product of every pair in the array.",
        "O(n^2)",
        "O(n^2)"
                )
            )
        ]
    ),
    Topic("Two Pointers"),
    Topic(
        "Hash Maps",
        "",
        [],
        "", 
        [
            Problem(
                "3160",
                "Find the Number of Distinct Colors Among the Balls",
                "You are given an integer `limit` and a 2D array `queries`. limit is the number of balls - 1. So there will be balls 0 all the way to `limit`. Inside queries is arrays [x, y] in which you are meant to assign color y to ball x. After this you return the total amount of distinct colors in the set of balls. Return the array of responses to the queries",
                "https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/",
                "Medium",
                [
                    "Arrays",
                    "Hash Maps",
                ],
                [
                    Example("limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]","[1,2,2,3]"),
                    Example("limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]","[1,2,2,3,4]"),
                ],
                [
                    Constraint("1 <= limit <= 10^9"),
                    Constraint("1 <= n == queries.length <= 10^5"),
                    Constraint("queries[i].length == 2"),
                    Constraint("0 <= queries[i][0] <= limit"),
                    Constraint("1 <= queries[i][1] <= 10^9"),
                ],
                Solution(
                    '''class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {}
        colorToBalls = {}
        res = []
        for ball, color in queries:
            if ball in ballToColor:
                colorToBalls[ballToColor[ball]].remove(ball)
                if len(colorToBalls[ballToColor[ball]]) == 0:
                    del colorToBalls[ballToColor[ball]]
            

            ballToColor[ball] = color
            if color in colorToBalls:
                colorToBalls[color].append(ball)
            else:
                colorToBalls[color] = [ball]
            res.append(len(colorToBalls))
        
        return res''',
                "This solution is actually very simple. The description tells us after each query we need to know the total amount of distinct colors among the ball set. Intuition tells us to get the amount of colors we need the balls grouped by color. That means a hashmap. This hashmap would go 'color' -> '[ball1, ball2]'. The problem we now face is knowing which color key in the hashmap to remove the ball from if the color of the ball is reassigned. To do this we will keep track of the colors of the balls in a separate hashmap. This hashmap will look like 'ball' -> 'color'. So now on each iteration through the queries we: 1. check if the balls color is being reassigned 2. if it is then we remove is from the array at the end of the balls old color 3. if the array at the end of the old color is empty remove it from the hashmap 4. set the balls color to the new color 5. put the ball in the color it belongs to in the color hashmap 6. append the length of the color hashmap to the response 7. return response. The trade off of creating the second hashmap is well worth the time speed up. This setup reminds me of a database setup where the ball would be the entity and the color to balls hash map is a sort of cash for some critical values you frequently need. So the hashmaps are just a representation of that sort of situation.",
                "O(n)",
                "O(n)"
                )
            ),
            Problem(
                "1",
                "Two Sum",
                "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. There is exactly one solution per input.",
                "https://leetcode.com/problems/two-sum/",
                "Easy",
                ["Arrays", "Hash Maps"],
                [
                    Example("nums = [2,7,11,15], target = 9","[0,1]"),
                    Example("nums = [3,2,4], target = 6","[1,2]"),
                    Example("nums = [3,3], target = 6", "[0,1]")
                ],
                [
                    Constraint("2 <= nums.length <= 10^4"),
                    Constraint("-10^9 <= nums[i] <= 10^9"),
                    Constraint("-10^9 <= target <= 10^9"),
                    Constraint("Exactly one solution exists"),
                ],
                Solution(
                    '''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i''',
            "This problem is possible using brute force by checking every possible combination of indices in the array for the target. But using the seen hash map allows us to maintain a set of numbers we have already seen. If we have seen the number we need, in combination with the current number, to reach the target then we are able to look up the number we need's index in the seen hashmap and return the solution.",
            "O(n)",
            "O(n)"
                )
            ),
            Problem(
                "2349",
                "Design a Number Container System",
                '''Design a number container system that can do the following:

    Insert or Replace a number at the given index in the system.
    Return the smallest index for the given number in the system.

Implement the NumberContainers class:

    NumberContainers() Initializes the number container system.
    void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
    int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
''',
                "https://leetcode.com/problems/design-a-number-container-system/",
                "Medium",
                ["Hash Maps", "Min Heap"],
                [
                    Example('''["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]''', "[null, -1, null, null, null, null, 1, null, 2]"),
                ],
                [Constraint("1 <= index, number <= 10^9"), Constraint("At most 10^5 calls will be made in total to change and find")],
                Solution(
                    '''class NumberContainers:

    def __init__(self):
        self.numbersToIndex = {}       
        self.indexToNumber = {}       


    def change(self, index: int, number: int) -> None:
        if index in self.indexToNumber and self.indexToNumber[index] == number:
            return

        if number in self.numbersToIndex:
            heapq.heappush(self.numbersToIndex[number], index)
        else:
            self.numbersToIndex[number] = [index]
        if index in self.indexToNumber:
            oldNumber = self.indexToNumber[index]
            self.numbersToIndex[oldNumber].remove(index)
            if len(self.numbersToIndex[oldNumber]) == 0:
                del self.numbersToIndex[oldNumber]
            else:
                heapq.heapify(self.numbersToIndex[oldNumber])
        self.indexToNumber[index] = number
        

    def find(self, number: int) -> int:
        if number not in self.numbersToIndex:
            return -1
        return  self.numbersToIndex[number][0]''',
        "This solution is the typical double hash map solution to speed up querying. The only trick to this question is storing the indices of the numbers in sorted order somehow. Leetcode suggests and ordered set, but I couldn't see one easily accessible in python so I used a min heap. The only slow part to this algorithm would be re-heapifying the indices after removing one from the list. That is O(logn)",
        "O(logn)",
        "O(n)"
                )
            )
        ],
        ),
    Topic("Sliding Windows"),
    Topic("Stacks"),
    Topic("Linked Lists"),
    Topic("Trees"),
    Topic("Matricies"),
    Topic("Intervals"),
    Topic("Dynamic Programming"),
]

def main():
    init()
   
    for i, topic in enumerate(topics):
        handleTopic(topic, i)


if __name__ == "__main__":
    main()
