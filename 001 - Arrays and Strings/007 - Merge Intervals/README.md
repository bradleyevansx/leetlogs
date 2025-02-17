## Merge Intervals

**Difficulty**: `Medium` - **Tags**: `Array`, `Sorting`

### Description

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Examples

**Example 1:**

**Input**: ```intervals = [[1,3],[2,6],[8,10],[15,18],[17,20]]```

**Output**: ```[[1,6],[8,10],[15,20]]```

### Constraints

- `1 <= intervals.length <= 10^4`

- `intervals[i].length == 2`

- `0 <= starti <= endi <= 10^4`

### Solution

**Description**:

This solution is based on the fact that this problem is actually very simple at the face value but requires some pre processing to catch some edge cases. For example, the intervals are not guaranteed to be sorted so to make it easier to process when it's sorted already. The other bit of processing I do it removing any duplicated start points. This allows me to not have to worry about when the start points are the same and just take the one that is the longest to include the most amount overlapped intervals.

**Time Complexity**: O(n log n) - **Space Complexity**: O(n) 

**The Code:**

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = []
        n = len(intervals)
        hm = {}

        for start, end in intervals:
            if start in hm:
                hm[start] = max(end, hm[start])
            else:
                hm[start] = end
        
        for key in hm:
            value = [key, hm[key]]
            heapq.heappush(heap, value)

        res = []

        while heap:
            start, end = heapq.heappop(heap)
            while heap and heap[0][0] <= end:
                start2, end2 = heapq.heappop(heap)
                end = max(end2, end)
            res.append([start, end])
        return res
```