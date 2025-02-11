## Product of Array Except Self

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Prefix Sum`

### Description

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

### Examples

**Example 1:**

**Input**: ```nums = [1,2,3,4]```

**Output**: ```[24,12,8,6]```

**Example 2:**

**Input**: ```nums = [-1,1,0,-3,3]```

**Output**: ```[0,0,9,0,0]```

### Constraints

- `2 <= nums.length <= 10^5`

- `-30 <= nums[i] <= 30`

- `The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.`

### Solution

**Description**:

I am familiar with the solution where you build the prefix and postfix separately and then combine them at the end to get the solution. So this time I wanted to challenge myself to see if I can do the leetcode's challenge of O(1) extra space. When I first coded it up I did get the no extra space by creating the res with the prefixes inside it. And to do the postfixes inside the nums array itself I used a previous counter to be able to keep track of what the postfix is before I overwrite the important information. But then I realized I could apply this concept to creating the prefex array as well. This led me to the current solution where I initialize with a pre/post fix of 1, iterate the array forward once building the prefixes. Then the second time I can just take the postfixes and mutiply them directly into the response array. The reason this strategy works is because are building the pre/post fixes as we go from left or right through the array. So we aren't actually using the response array to store the prefixes for any other reason than to return them. Before I was using the array as the method of storing the current prefix.

**Time Complexity**: O(n) - **Space Complexity**: O(1) 

**The Code:**

```python
class Solution:
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

        return res
```