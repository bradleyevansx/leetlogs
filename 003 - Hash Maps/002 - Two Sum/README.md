## Two Sum

**Difficulty**: `Easy` - **Tags**: `Arrays`, `Hash Maps`

### Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. There is exactly one solution per input.

### Examples

**Example 1:**

**Input**: ```nums = [2,7,11,15], target = 9```

**Output**: ```[0,1]```

**Example 2:**

**Input**: ```nums = [3,2,4], target = 6```

**Output**: ```[1,2]```

**Example 3:**

**Input**: ```nums = [3,3], target = 6```

**Output**: ```[0,1]```

### Constraints

- `2 <= nums.length <= 10^4`

- `-10^9 <= nums[i] <= 10^9`

- `-10^9 <= target <= 10^9`

- `Exactly one solution exists`

### Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i
```

**Description**:

This problem is possible using brute force by checking every possible combination of indices in the array for the target. But using the seen hash map allows us to maintain a set of numbers we have already seen. If we have seen the number we need, in combination with the current number, to reach the target then we are able to look up the number we need's index in the seen hashmap and return the solution.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

