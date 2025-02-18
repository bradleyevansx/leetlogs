## Group Anagrams

**Difficulty**: `Medium` - **Tags**: `Array`, `Hash Table`, `Sorting`

### Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

### Examples

**Example 1:**

**Input**: ```strs = [eat,sleep,tea,ate]```

**Output**: ```[[eat, tea, ate], [sleep]]```

### Constraints

- `1 <= strs.length <= 1000`

- `1 <= strs[i].length <= 100`

- `strs[i] consists of lowercase English letters.`

### Solution

**Description**:

This solution is really about efficiently storing the anagrams in a structure that can group them together. In addition to this you need an efficient way of telling which group the words belong to. To do this I sorted them and then hash that value into the hash map. This means that the only expensive operation here is sorting each value in nums. Then from there appending to the group is all O(1). This means that the over all complexity is n * nlogn for the sorting n times. This is alright for this question because the maximum length of the words is 100. So the sorting is not that expensive. The space complexity is O(n) because we are storing all the words in the hashmap.

**Time Complexity**: O(n * klogk) - **Space Complexity**: O(n) 

**The Code:**

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for i, s in enumerate(strs):
            key = tuple(sorted(s))
            if key in hm:
                hm[key].append(i)
            else:
                hm[key] = [i]
        
        res = []

        for key in hm:
            indexes = hm[key]
            res.append([strs[i] for i in indexes])
            
        return res
```