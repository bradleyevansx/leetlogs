## Recover a Tree From Preorder Traversal

**Difficulty**: `Hard` - **Tags**: `Tree`, `Stacks`

### Description

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

### Examples

**Example 1:**

**Input**: ```s = "1-2--3--4-5--6--7"```

**Output**: ```[[1],[2,5],[3,6],[4,7]]```

### Constraints

- `The number of nodes in the original tree is in the range [1, 1000]`

- `1 <= Node.val <= 109`

### Solution

**Description**:

My thought process was obviously to do some sort of dfs as soon as I saw the problem. When I saw the input data I thought to put the data into a queue and build to the tree until the tree is clearly not expanding downwards anymore. When this happens you simply need a way to know where to pick up at in the imaginary stack. Pre process the array to allow for easy depth tracking and maitenance of the Nodes that we may want to append to the right of later on. Pre processing it allows us to think less about the hyphens and the input we are given to just focus on the abnormal dfs we are performing.

**Time Complexity**: O(n) - **Space Complexity**: O(n) 

**The Code:**

```python
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
```