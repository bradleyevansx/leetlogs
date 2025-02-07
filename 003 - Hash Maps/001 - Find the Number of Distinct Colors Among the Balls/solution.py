class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {}
        colorToBalls = {}
        res = []
        for ball, color in queries:
            if ball in ballToColor:
                colorToBalls[ballToColor[ball]].remove(ball)
                if len(colorToBalls[ballToColor[ball]]) == 0:
                    del colorToBalls[ballToColor[ball]]
            

            ballToColor[ball] = color
            if color in colorToBalls:
                colorToBalls[color].append(ball)
            else:
                colorToBalls[color] = [ball]
            res.append(len(colorToBalls))
        
        return res