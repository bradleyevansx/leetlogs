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