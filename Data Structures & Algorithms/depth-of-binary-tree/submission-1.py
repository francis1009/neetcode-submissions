# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        res = 1
        while q:
            node, k = q.popleft()
            res = max(res, k)
            if node.left:
                q.append((node.left, k+1))
            if node.right:
                q.append((node.right, k+1))
        return res
                