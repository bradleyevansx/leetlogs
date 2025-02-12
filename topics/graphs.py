from sdk.models.problems import Constraint, Example, Problem, Solution


graphs = [
    Problem(
        "547",
        "Number of Provinces",
        '''There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.''',
        "https://leetcode.com/problems/number-of-provinces/description/",
        "Medium",
        ["Adjacency Matric", "Depth First Search", "Union Find", "Graph"],
        [Example("isConnected = [[1,1,0],[1,1,0],[0,0,1]]", "2"), Example("isConnected = [[1,0,0],[0,1,0],[0,0,1]]", "3")],
        [Constraint("1 <= n <= 200"), Constraint("n == isConnected.length == isConnected[i].length"), Constraint("isConnected[i][j] is 1 or 0"), Constraint("isConnected[i][i] == 1"),Constraint("isConnected[i][j] == isConnected[j][i]")],
        Solution(
            '''class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def dfs(start):
            isConnected[start][start] = 0

            for i in range(n):
                if isConnected[start][i] == 1 and isConnected[i][i] == 1:
                    dfs(i)
            
        res = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and isConnected[i][i] == 1:
                    dfs(i)
                    res += 1
        return res''',
        "This problem is a text book DFS or BFS problem on a graph. In this instance the graph is represented by an adjacency matrix. This is probably my least favorite type of graph representation to work with. But for this question it actually works perfectly. You are able to not look at a given row more than once and easily visualize which nodes you have visited. I originally kept track of visited nodes with an array. But I switched to marking the [i][i] element of the matrix to 0 if it's visited. It performs worst speed wise some how. But I think it is is the better solution.",
        "O(n^2)",
        "O(1)"
        )
    )
]