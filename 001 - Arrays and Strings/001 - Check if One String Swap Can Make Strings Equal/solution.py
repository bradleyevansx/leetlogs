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