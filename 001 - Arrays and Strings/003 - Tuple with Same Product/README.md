## Tuple with Same Product

**Difficulty**: `Medium` - **Tags**: `Array`, `Hash Table`, `Counting`

### Description

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

### Examples

**Example 1:**

**Input**: ```nums = [2,3,4,6]```

**Output**: ```8```

**Example 2:**

**Input**: ```nums = [1,2,4,5,10]```

**Output**: ```16```

### Constraints

- `1 <= nums.length <= 1000`

- `1 <= nums[i] <= 104`

- `All elements in nums are distinct.`

### Solution

**Description**:

The core of this solution is the math involved with determining how many pairs you can make out of the total amount of the total amount of Tuples that equal the given product. So our strategy is to have a hashmap that keeps track of the different products you can achieve by checking each pair of integers in the array. From each pair we will increase the count of elements that have this product by one. With each count is a number of pairs that we can make from that count. Each time we increase the count we increase the amount of pairs by the count of products we previously had. This allows us to simply find the products that have a count > 1 in the hashmap and multiply the pairs associated with those pairs by 8. Add up all of these results and return it. A factor that plays into our favor is that each element in nums is disctinct. The space complexity of this is O(n^2) but that is the worst case. In practice this algorithm would be much more efficient than that. However, the high time complexity is unavoidable. We are required to check the product of every pair in the array.

**Time Complexity**: O(n^2) - **Space Complexity**: O(n^2) 

**The Code:**

```python
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        hm = {}

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] * nums[j] in hm:
                    count, pairs =  hm[nums[i] * nums[j]]

                    hm[nums[i] * nums[j]] = (count + 1, pairs + count)
                else:
                    hm[nums[i] * nums[j]] = (1, 0)
        
        res = 0

        for key in hm:
            count, pairs = hm[key]
            res += pairs * 8 
            
        return res
```