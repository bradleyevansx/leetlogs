class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if c.isalpha():
                stack.append(c)
            else:
                stack.pop()

        return "".join(stack)