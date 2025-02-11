## Remove All Occurrences of a Substring

**Difficulty**: `Medium` - **Tags**: `Strings`, `Stacks`

### Description

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

### Examples

**Example 1:**

**Input**: ```s = "daabcbaabcbc", part = "abc"```

**Output**: ```"dab"```

**Example 2:**

**Input**: ```s = "axxxxyyyyb", part = "xy"```

**Output**: ```"ab"```

### Constraints

- `1 <= s.length, part.length <= 1000`

- `s and part consists of lowercase English letters.`

### Solution

**Description**:

This problem begs for some data structure that can pop like a stack. Originally I solved this problem using an array as the stack that I use to build the solution. But ultimately converting that to a string to compare to the part we are removing on every iteration was too costly. So I switched to a string as my 'stack' and would just remove from the end of it on an iteration where the end of the stack matched the part. The reason this solution works is because the only time you would need to remove from the stack when iterating through the input left to right is when the last letters in the stack match the part. Removing all of these letters allows you to still have the chaining affect where removing one set of the part leaves you with another set of the part in a candy crush style combo.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

**The Code:**

```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""
        n = len(part)
        for i, c in enumerate(s):
            res += c
            if not i < n - 1 and res[-n:] == part:
                res = res[0:-n]
        return res
```