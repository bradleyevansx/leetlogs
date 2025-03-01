## Apply Operations to an Array

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Two Pointers`

### Description

You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

    If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.

After performing all the operations, shift all the 0's to the end of the array.

    For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

Return the resulting array.

Note that the operations are applied sequentially, not all at once.

### Examples

**Example 1:**

**Input**: ```nums = [1,0,2,0,0,1]```

**Output**: ```[1,2,1,0,0,0]```

**Example 2:**

**Input**: ```nums = [1,2,3,4,5]```

**Output**: ```[1,2,3,4,5]```

### Constraints

- `1 <= n <= 10^5`

- `0 <= nums[i] <= 10^5`

### Solution

**Description**:

This problem is a simple two pointer problem. I'm fairly certain I could combine the two loops but it wouldn't affect the time complexity very much asymptotically.

**Time Complexity**: O(n) - **Space Complexity**: O(1) 

**The Code:**

```python
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        l = 0
        for r in range(n):
            if nums[r] != 0:
                tmp = nums[r]
                nums[r] = 0
                nums[l] = tmp
                l += 1
        return nums
```