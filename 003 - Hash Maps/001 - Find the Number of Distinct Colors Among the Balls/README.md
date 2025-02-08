## Find the Number of Distinct Colors Among the Balls

**Difficulty**: `Medium` - **Tags**: `Arrays`, `Hash Maps`

### Description

You are given an integer `limit` and a 2D array `queries`. limit is the number of balls - 1. So there will be balls 0 all the way to `limit`. Inside queries is arrays [x, y] in which you are meant to assign color y to ball x. After this you return the total amount of distinct colors in the set of balls. Return the array of responses to the queries

### Examples

**Example 1:**

**Input**: ```limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]```

**Output**: ```[1,2,2,3]```

**Example 2:**

**Input**: ```limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]```

**Output**: ```[1,2,2,3,4]```

### Constraints

- `1 <= limit <= 10^9`

- `1 <= n == queries.length <= 10^5`

- `queries[i].length == 2`

- `0 <= queries[i][0] <= limit`

- `1 <= queries[i][1] <= 10^9`

### Solution

**Description**:

This solution is actually very simple. The description tells us after each query we need to know the total amount of distinct colors among the ball set. Intuition tells us to get the amount of colors we need the balls grouped by color. That means a hashmap. This hashmap would go 'color' -> '[ball1, ball2]'. The problem we now face is knowing which color key in the hashmap to remove the ball from if the color of the ball is reassigned. To do this we will keep track of the colors of the balls in a separate hashmap. This hashmap will look like 'ball' -> 'color'. So now on each iteration through the queries we: 1. check if the balls color is being reassigned 2. if it is then we remove is from the array at the end of the balls old color 3. if the array at the end of the old color is empty remove it from the hashmap 4. set the balls color to the new color 5. put the ball in the color it belongs to in the color hashmap 6. append the length of the color hashmap to the response 7. return response. The trade off of creating the second hashmap is well worth the time speed up. This setup reminds me of a database setup where the ball would be the entity and the color to balls hash map is a sort of cash for some critical values you frequently need. So the hashmaps are just a representation of that sort of situation.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

**The Code:**

```python
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
```