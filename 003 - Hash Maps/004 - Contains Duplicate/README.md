## Contains Duplicate

**Difficulty**: `Easy` - **Tags**: `Hash Set`, `Arrays`

### Description

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### Examples

**Example 1:**

**Input**: ```nums = [1,2,3,1]```

**Output**: ```True```

**Example 2:**

**Input**: ```nums = [1,2,3,4]```

**Output**: ```False```

**Example 3:**

**Input**: ```nums = [1,1,1,3,3,4,3,2,4,2]```

**Output**: ```True```

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^9 <= nums[i] <= 10^9`

### Solution

**Description**:

This problem is the simplest example of using the power of hash sets to your advantage. The brute force to this problem would be O(n^2). By using a hash set, and taking advantage of the constant lookup time, we bring the overall time complexit to O(n). This is a great improvement.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

**The Code:**

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```