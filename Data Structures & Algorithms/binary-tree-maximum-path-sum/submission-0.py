# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float("-inf")

        def solve(node):
            nonlocal maxi

            if node is None:
                return 0

            leftsum = max(0, solve(node.left))
            rightsum = max(0, solve(node.right))

            maxi = max(maxi, leftsum + node.val + rightsum)

            return node.val + max(leftsum, rightsum)

        solve(root)
        return maxi
        