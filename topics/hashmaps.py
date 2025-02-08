from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import Topic


hashmaps =     Topic(
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
            ),
            Problem(
                "217",
                "Contains Duplicate",
                '''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.''',
                "https://leetcode.com/problems/contains-duplicate/",
                "Easy",
                ["Hash Set", "Arrays"],
                [Example("nums = [1,2,3,1]", "True"), Example("nums = [1,2,3,4]", "False"), Example("nums = [1,1,1,3,3,4,3,2,4,2]", "True")],
                [Constraint("1 <= nums.length <= 10^5"), Constraint("-10^9 <= nums[i] <= 10^9")],
                Solution(
                    '''class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False''',
        "This problem is the simplest example of using the power of hash sets to your advantage. The brute force to this problem would be O(n^2). By using a hash set, and taking advantage of the constant lookup time, we bring the overall time complexit to O(n). This is a great improvement.",
        "O(n)",
        "O(n)"
                )
            )
        ],
        )