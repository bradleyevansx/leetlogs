## Three Sum

**Difficulty**: `Medium` - **Tags**: `Array`, `Two Pointers`, `Sorting`

### Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

### Examples

**Example 1:**

**Input**: ```nums = [-1,0,1,2,-1,-4]```

**Output**: ```[[-1,-1,2],[-1,0,1]]```

**Example 2:**

**Input**: ```nums = [0,1,1]```

**Output**: ```[]```

**Example 3:**

**Input**: ```nums = [0, 0, 0]```

**Output**: ```[[0, 0, 0]]```

### Constraints

- `0 <= nums.length <= 3000`

- `-10^5 <= nums[i] <= 10^5`

### Solution

**Description**:

My solution is slower than average but I feel it is an acceptable solution. It takes a triple nested for loop and makes it only double. So O(n^3) to O(n^2). This is a major improvement. The process for this is to loop through the array checking for a two sum in the rest of the array that adds up to zero with the number that is already fixed. Keeping track of the solutions is a set allows for easy tracking of solutions.

**Time Complexity**: O(n^2) - **Space Complexity**: O(n) 

**The Code:**

```python
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

```