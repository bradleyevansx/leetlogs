## Minimum Number of Operations to Exceed Threshold Value

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Min Heap`

### Description

You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

    Take the two smallest integers x and y in nums.
    Remove x and y from nums.
    Add min(x, y) * 2 + max(x, y) anywhere in the array.

Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

### Examples

**Example 1:**

**Input**: ```nums = [2,11,10,1,3], k = 10```

**Output**: ```2```

**Example 2:**

**Input**: ```nums = [1,1,2,4,9], k = 20```

**Output**: ```4```

### Constraints

- `2 <= nums.length <= 2 * 10^5`

- `1 <= nums[i] <= 10^9`

- `1 <= k <= 10^9`

- `The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are greater than or equal to k.`

### Solution

**Description**:

Anytime a problem talks about keeping track of the min element I think of using a min heap. Most of the time it's going to be faster overall to heapify and keep track of the heap as opposed to searching for the min on each iteration. This is each more true for this problem because we need two min values on every iteration. This problem is fairly simple when you see the min heap solution.

**Time Complexity**: O(nLogn) - **Space Complexity**: O(n) 

**The Code:**

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)

        while nums[0] < k:
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)

            newVal = (min1 * 2) + min2

            heapq.heappush(nums, newVal)
            res += 1
        return res
```