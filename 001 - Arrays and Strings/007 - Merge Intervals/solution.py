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