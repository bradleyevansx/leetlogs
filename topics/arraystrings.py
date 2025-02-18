from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import SubTopic, Topic


arraystrings =     Topic(
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
            ),
            Problem(
                "238",
                "Product of Array Except Self",
                '''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.''',
                "https://leetcode.com/problems/product-of-array-except-self/",
                "Medium",
                ["Arrays", "Prefix Sum" ],
                [Example("nums = [1,2,3,4]", "[24,12,8,6]"), Example("nums = [-1,1,0,-3,3]", "[0,0,9,0,0]")],
                [Constraint("2 <= nums.length <= 10^5"), Constraint("-30 <= nums[i] <= 30"), Constraint("The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.")],
                Solution(
                    '''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        suff = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suff
            suff *= nums[i]

        return res''',
        "I am familiar with the solution where you build the prefix and postfix separately and then combine them at the end to get the solution. So this time I wanted to challenge myself to see if I can do the leetcode's challenge of O(1) extra space. When I first coded it up I did get the no extra space by creating the res with the prefixes inside it. And to do the postfixes inside the nums array itself I used a previous counter to be able to keep track of what the postfix is before I overwrite the important information. But then I realized I could apply this concept to creating the prefex array as well. This led me to the current solution where I initialize with a pre/post fix of 1, iterate the array forward once building the prefixes. Then the second time I can just take the postfixes and mutiply them directly into the response array. The reason this strategy works is because are building the pre/post fixes as we go from left or right through the array. So we aren't actually using the response array to store the prefixes for any other reason than to return them. Before I was using the array as the method of storing the current prefix.",
        "O(n)",
        "O(1)"
                )
            ),
            Problem(
                "53",
                "Maximum Subarray",
                "Given an integer array nums, find the subarray with the largest sum, and return its sum.",
                "https://leetcode.com/problems/maximum-subarray/",
                "Medium",
                ["Arrays", "Dynamic Programming"],
                [Example("nums = [-2,1,-3,4,-1,2,1,-5,4]", 6), Example("nums = [1]", "1"), Example("nums = [5,4,-1,7,8]", "23")],
                [Constraint("1 <= nums.length <= 10^5"), Constraint("-10^4 <= nums[i] <= 10^4")],
                Solution(
                    '''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = float("-inf"), 0

        for num in nums:
            curr += num
            curr = max(curr, num)
            res = max(curr, res)
        return res''',
                    "If you brute force this problem you would be required to do O(n^2) operations. This is very slow for this problem. By using Kadane's algorithm we can go down to O(n). This is where as we move from left to right through the array, if we find a new starting point that is higher than the current total we are seeing with the subarray then we restart the subarray at that point. This is very similar to the Best Time to Buy and Sell a Stock question. If we find a better entry point to the stock market then we just start there.",
                    "O(n)",
                    "O(1)"
                )

            ),
            Problem(
                "15",
                "Three Sum",
                '''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.''',
                "https://leetcode.com/problems/3sum/",
                "Medium",
                ["Array", "Two Pointers", "Sorting"],
                [Example("nums = [-1,0,1,2,-1,-4]", "[[-1,-1,2],[-1,0,1]]"), Example("nums = [0,1,1]", "[]"), Example("nums = [0, 0, 0]", "[[0, 0, 0]]")],
                [Constraint("0 <= nums.length <= 3000"), Constraint("-10^5 <= nums[i] <= 10^5")],
                Solution(
                    '''class Solution:
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
''',
                    "My solution is slower than average but I feel it is an acceptable solution. It takes a triple nested for loop and makes it only double. So O(n^3) to O(n^2). This is a major improvement. The process for this is to loop through the array checking for a two sum in the rest of the array that adds up to zero with the number that is already fixed. Keeping track of the solutions is a set allows for easy tracking of solutions.",
                    "O(n^2)",
                    "O(n)"
                )

            ),
            Problem(
                "56", 
                "Merge Intervals",
                '''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.''',
                "https://leetcode.com/problems/merge-intervals/",
                "Medium",
                ["Array", "Sorting"],
                [Example("intervals = [[1,3],[2,6],[8,10],[15,18],[17,20]]", "[[1,6],[8,10],[15,20]]")],
                [Constraint("1 <= intervals.length <= 10^4"), Constraint("intervals[i].length == 2"), Constraint("0 <= starti <= endi <= 10^4")],
                Solution(
                    '''class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = []
        n = len(intervals)
        hm = {}

        for start, end in intervals:
            if start in hm:
                hm[start] = max(end, hm[start])
            else:
                hm[start] = end
        
        for key in hm:
            value = [key, hm[key]]
            heapq.heappush(heap, value)

        res = []

        while heap:
            start, end = heapq.heappop(heap)
            while heap and heap[0][0] <= end:
                start2, end2 = heapq.heappop(heap)
                end = max(end2, end)
            res.append([start, end])
        return res''',
                    "This solution is based on the fact that this problem is actually very simple at the face value but requires some pre processing to catch some edge cases. For example, the intervals are not guaranteed to be sorted so to make it easier to process when it's sorted already. The other bit of processing I do it removing any duplicated start points. This allows me to not have to worry about when the start points are the same and just take the one that is the longest to include the most amount overlapped intervals.",
                    "O(n log n)",
                    "O(n)"
                )
            ),
            Problem(
                "49",
                "Group Anagrams",
                "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
                "https://leetcode.com/problems/group-anagrams/",
                "Medium",
                ["Array", "Hash Table", "Sorting"],
                [Example("strs = [eat,sleep,tea,ate]", "[[eat, tea, ate], [sleep]]")],
                [Constraint("1 <= strs.length <= 1000"), Constraint("1 <= strs[i].length <= 100"), Constraint("strs[i] consists of lowercase English letters.")],
                Solution(
                    '''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for i, s in enumerate(strs):
            key = tuple(sorted(s))
            if key in hm:
                hm[key].append(i)
            else:
                hm[key] = [i]
        
        res = []

        for key in hm:
            indexes = hm[key]
            res.append([strs[i] for i in indexes])
            
        return res''',
                    "This solution is really about efficiently storing the anagrams in a structure that can group them together. In addition to this you need an efficient way of telling which group the words belong to. To do this I sorted them and then hash that value into the hash map. This means that the only expensive operation here is sorting each value in nums. Then from there appending to the group is all O(1). This means that the over all complexity is n * nlogn for the sorting n times. This is alright for this question because the maximum length of the words is 100. So the sorting is not that expensive. The space complexity is O(n) because we are storing all the words in the hashmap.",
                    "O(n * klogk)",
                    "O(n)"
                )

            ),
            Problem(
                "33",
                "Search in Rotated Sorted Array",
                '''There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.''',
                "https://leetcode.com/problems/search-in-rotated-sorted-array/",
                "Medium",
                ["Array", "Binary Search"],
                [Example("nums = [4,5,6,7,0,1,2], target = 0", "4"), Example("nums = [1], target = 0", "-1")],
                [Constraint("n == nums.length"), Constraint("1 <= n <= 5000"), Constraint("-10^4 <= nums[i] <= 10^4"), Constraint("All values of nums are unique."), Constraint("nums is an ascending array that is possibly rotated."), Constraint("-10^4 <= target <= 10^4")],
                Solution(
                    '''class Solution:
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
        return -1''',
                    "This problem was pretty tricky for me. I need to get better at binary search problems. This problem all comes down to speeding up the search by knowing first which side of the array from the pivot to search in. This means first finding the pivot and then binary searching to the left or right of the pivot. Luckily we an binary search for the pivot as well. This means that the solution is logn instead of n + logn which would be O(n).",
                    "O(log n)",
                    "O(1)"
                )

            )
                    ]
    )