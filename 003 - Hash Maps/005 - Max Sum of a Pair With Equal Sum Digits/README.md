## Max Sum of a Pair With Equal Sum Digits

**Difficulty**: `Medium` - **Tags**: `Hash Maps`, `Arrays`

### Description

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

### Examples

**Example 1:**

**Input**: ```nums = [18,43,36,13,7]```

**Output**: ```54```

**Example 2:**

**Input**: ```nums = [10,12,19,14]```

**Output**: ```-1```

### Constraints

- `1 <= nums.length <= 10^5`

- `1 <= nums[i] <= 10^9`

### Solution

**Description**:

Just by reading the title I could tell this problems trick would be to use a hash map. Anytime I see a problem where we need the pair with a certain constraint I think it will imply brute forcing it with nested for loops. But you can often optimize these problems by creating a lookup data structure for the values you have previously seen. In this case we store the values of the sum of the digits as the key and the number associated with that value in a hash map. This allows us to just look up to see if the value of digits has been seen before. If it has check to see if the previous value + this one is greater than the response so far. After that you can update the highest value you have seen with that digit sum accordingly. We only care about the highest value associated with a digit sum at any given. So creating a list and sorting it is not necessary.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

**The Code:**

```python
class Solution:
    def getDigitsSum(self, num):
        digitSum = 0
    
        while num > 0:
            digitSum += num % 10
            num //= 10

        return digitSum
    def maximumSum(self, nums: List[int]) -> int:
        hm = {}
        res = -1
        for num in nums:
            curr = self.getDigitsSum(num)
            
            if curr not in hm:
                hm[curr] = num
            else:
                res = max(res, hm[curr] + num)
                hm[curr] = max(hm[curr], num)
        return res
```