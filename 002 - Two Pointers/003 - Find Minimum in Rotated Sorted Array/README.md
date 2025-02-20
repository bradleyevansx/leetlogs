## Find Minimum in Rotated Sorted Array

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Binary Search`, `Two Pointer`

### Description

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

### Examples

**Example 1:**

**Input**: ```nums = [3,4,5,1,2]```

**Output**: ```1```

**Example 2:**

**Input**: ```nums = [4,5,6,7,0,1,2]```

**Output**: ```0```

**Example 3:**

**Input**: ```nums = [11,13,15,17]```

**Output**: ```11```

### Constraints

- `n == nums.length`

- `1 <= n <= 5000`

- `5000 <= nums[i] <= 5000`

### Solution

**Description**:

This problem is a text book binary search problem. You have a criteria as to how you are supposed to change bounds of the valid search area and you continually narrow it down until you've found your target.

**Time Complexity**: O(logn) - **Space Complexity**: O(1) 

**The Code:**

```python
class Solution:
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
        return nums[l]
```