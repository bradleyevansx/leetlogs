## Sum of All Subset XOR Totals

**Difficulty**: `Easy` - **Tags**: `Arrays`, `Math`, `Backtracking`, `Combinatorics`

### Description

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty. Given an array nums, return the sum of all XOR totals for every subset of nums. Note: Subsets with the same elements should be counted multiple times.

### Examples

**Example 1:**

**Input**: ```nums = [1,3]```

**Output**: ```6```

**Example 2:**

**Input**: ```nums = [5,1,6]```

**Output**: ```28```

**Example 3:**

**Input**: ```nums = [3,4,5,6,7,8]```

**Output**: ```480```

### Constraints

- `1 <= nums.length <= 12`

- `1 <= nums[i] <= 20`

### Solution

```python
class Solution:
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

        return res
```

**Description**:

The heart of this problem really lies in the backtracking part where you generate all the subset combinations for the array. I do this recursively. In this case the decision at each node of the decision tree is to add the current index or to not add it. Add the leafs of the tree you have all the different subsets. Then from there you can just iterate over the subsets and get the XOR of all the elements in each subset and add it to the response. This solution will be beat out by all the people who use the solution where you use the sum and length of the array to do fancy math and get the answer without any manipulation of the data structure.

**Time Complexity**: O(2^n * n) - **Space Complexity**: O(2^n * n) 

