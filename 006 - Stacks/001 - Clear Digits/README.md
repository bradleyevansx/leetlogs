## Clear Digits

**Difficulty**: `Easy` - **Tags**: `Strings`, `Stacks`

### Description

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

### Examples

**Example 1:**

**Input**: ```s = "abc"```

**Output**: ```"abc"```

**Example 2:**

**Input**: ```s = "cb34"```

**Output**: ```""```

### Constraints

- `1 <= s.length <= 100`

- `s consists only of lowercase English letters and digits.`

- `The input is generated such that it is possible to delete all digits.`

### Solution

**Description**:

My first glance at this problem told me to use a stack to build the response. Anytime a problem uses the language 'remove the most recent item' or 'the one to the left' that is my first instinct. The only think I needed to do with this problem to make it more efficient is actually rearrange the if statement. At first I had the if checking to see if the number was a number. This was inefficient beacuse the nature of the problem is that there will always be at least as many regular characters as there are numbers. This means that yes there will be some test cases where having the number check first is just as efficient as putting the check to see if it is a number first. But for the majority of scenarios there is going to be more letters than numbers. This means checking for that in the if is going to be greatly more efficient.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

**The Code:**

```python
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if c.isalpha():
                stack.append(c)
            else:
                stack.pop()

        return "".join(stack)
```