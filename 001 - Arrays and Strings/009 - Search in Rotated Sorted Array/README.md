## Search in Rotated Sorted Array

**Difficulty**: `Medium` - **Tags**: `Array`, `Binary Search`

### Description

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

### Examples

**Example 1:**

**Input**: ```nums = [4,5,6,7,0,1,2], target = 0```

**Output**: ```4```

**Example 2:**

**Input**: ```nums = [1], target = 0```

**Output**: ```-1```

### Constraints

- `n == nums.length`

- `1 <= n <= 5000`

- `-10^4 <= nums[i] <= 10^4`

- `All values of nums are unique.`

- `nums is an ascending array that is possibly rotated.`

- `-10^4 <= target <= 10^4`

### Solution

**Description**:

This problem was pretty tricky for me. I need to get better at binary search problems. This problem all comes down to speeding up the search by knowing first which side of the array from the pivot to search in. This means first finding the pivot and then binary searching to the left or right of the pivot. Luckily we an binary search for the pivot as well. This means that the solution is logn instead of n + logn which would be O(n).

**Time Complexity**: O(log n) - **Space Complexity**: O(1) 

**The Code:**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        rightMost = nums[n - 1]
        mid = None
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > rightMost:
                l = l + 1
            elif nums[mid] < rightMost:
                r = r - 1

        if mid == None:
            return 0 if nums[0] == target else -1
        
        if target >= nums[0] and target <= nums[mid]:
            l, r = 0, mid
        else:
            l, r = mid + 1, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
```