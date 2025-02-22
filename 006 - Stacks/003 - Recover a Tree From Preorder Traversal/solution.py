# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)

        i = 0
        pre = []
        while i < n:
            curr = 0
            while traversal[i] == "-":
                i += 1
                curr += 1
            
            num = ""
            while i < n and traversal[i] != "-":
                num += traversal[i]
                i += 1
            pre.append((int(num), curr))
        pre = deque(pre)
        rootVal, depth = pre.popleft()
        head = TreeNode(val=rootVal)
        stack = [(depth, head)]

        while pre:
            currVal, currDepth = pre.popleft()

            while stack and stack[-1][0] != currDepth - 1:
                stack.pop()
            
            parent = stack[-1][1]

            newNode = TreeNode(val=currVal)

            if not parent.left:
                parent.left = newNode
            else:
                parent.right = newNode
            
            stack.append((currDepth, newNode))

        return head