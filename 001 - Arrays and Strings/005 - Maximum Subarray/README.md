## Maximum Subarray

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Dynamic Programming`

### Description

Given an integer array nums, find the subarray with the largest sum, and return its sum.

### Examples

**Example 1:**

**Input**: ```nums = [-2,1,-3,4,-1,2,1,-5,4]```

**Output**: ```6```

**Example 2:**

**Input**: ```nums = [1]```

**Output**: ```1```

**Example 3:**

**Input**: ```nums = [5,4,-1,7,8]```

**Output**: ```23```

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^4 <= nums[i] <= 10^4`

### Solution

**Description**:

If you brute force this problem you would be required to do O(n^2) operations. This is very slow for this problem. By using Kadane's algorithm we can go down to O(n). This is where as we move from left to right through the array, if we find a new starting point that is higher than the current total we are seeing with the subarray then we restart the subarray at that point. This is very similar to the Best Time to Buy and Sell a Stock question. If we find a better entry point to the stock market then we just start there.

**Time Complexity**: O(n) - **Space Complexity**: O(1) 

**The Code:**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = float("-inf"), 0

        for num in nums:
            curr += num
            curr = max(curr, num)
            res = max(curr, res)
        return res
```