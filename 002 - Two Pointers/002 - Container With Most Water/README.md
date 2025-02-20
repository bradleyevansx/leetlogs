## Container With Most Water

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Two Pointers`

### Description

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

### Examples

**Example 1:**

**Input**: ```height = [1,8,6,2,5,4,8,3,7]```

**Output**: ```49```

**Example 2:**

**Input**: ```height = [1,1]```

**Output**: ```1```

**Example 3:**

**Input**: ```height = [4,3,2,1,4]```

**Output**: ```16```

**Example 4:**

**Input**: ```height = [1,2,1]```

**Output**: ```2```

### Constraints

- `n == height.length`

- `2 <= n <= 10^5`

- `0 <= height[i] <= 10^4`

### Solution

**Description**:

This is a two pointer problem. You have to start with pointers at the outside edges of the array. This problem also a has a greedy aspect to it as you are always trying to choose the next best choice and ignore all the others. At each iteration you move the pointer that is the lowest towards the middle. This is with the hopes that there is a higher point to go to that will leader to a greater response. The algorithm is over whent he pointers are right next to each other.

**Time Complexity**: O(n) - **Space Complexity**: O(1) 

**The Code:**

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        res = 0

        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l] * (r - l))
                l += 1
            else:
                res = max(res, height[r] * (r - l))
                r -= 1
        return res
```