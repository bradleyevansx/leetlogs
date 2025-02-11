class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""
        n = len(part)
        for i, c in enumerate(s):
            res += c
            if not i < n - 1 and res[-n:] == part:
                res = res[0:-n]
        return res