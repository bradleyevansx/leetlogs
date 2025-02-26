## Maximum Absolute Sum of Any Subarray

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Dynamic Programming`

### Description

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.


### Examples

**Example 1:**

**Input**: ```nums = [1, -3, 2, 3, -4]```

**Output**: ```5```

**Example 2:**

**Input**: ```nums = [2, -5, 1, -4, 3, -2]```

**Output**: ```8```

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^4 <= nums[i] <= 10^4`

### Solution

**Description**:

This problem is a variation of Kadane's algorithm. Essentially with the standrad Kadane's algo we would get the maximum subarray. Since we need the max abs() subarray we should just do a second pass through of the input with a modified Kadane's algo to get the minimum subarray. And the result would me the max between the abs() of the two.

**Time Complexity**: O(n) - **Space Complexity**: O(1) 

**The Code:**

```python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        absMax = 0
        curr = 0
        for n in nums:
            curr += n
            curr = max(curr, n)
            absMax = max(curr, absMax)
        print(absMax)

        absMin = 0
        curr = 0
        for n in nums:
            curr += n
            curr = min(curr, n)
            absMin = min(curr, absMin)
        return max(abs(absMin), abs(absMax))
```