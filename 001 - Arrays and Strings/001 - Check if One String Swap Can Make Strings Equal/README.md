## Check if One String Swap Can Make Strings Equal

**Difficulty**: `Easy` - **Tags**: `Hash Table`, `String`, `Counting`

### Description

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices. Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

### Examples

**Example 1:**

**Input**: ```s1 = "bank", s2 = "kanb"```

**Output**: ```True```

**Example 2:**

**Input**: ```s1 = "attack", s2 = "defend"```

**Output**: ```False```

**Example 3:**

**Input**: ```s1 = "kelb", s2 = "kelb"```

**Output**: ```True```

### Constraints

- `1 <= s1.length, s2.length <= 100`

- `s1.length == s2.length`

- `s1 and s2 consist of only lowercase English letters`

### Solution

**Description**:

The solution is to check if the two strings are equal. If they are, return True. Otherwise, find the indexes of the characters that are different and store them in a list. If the length of the list is not 2, return False. Otherwise, check if the characters at the indexes in the list are equal. If they are, return True. Otherwise, return False.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        res = 0
        h1, h2 = set(), set()

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                h1.add(s1[i])
                h2.add(s2[i])
                res += 1
        
        if res == 0 or res == 2:
            if h1 == h2:
                return True
        return False
```