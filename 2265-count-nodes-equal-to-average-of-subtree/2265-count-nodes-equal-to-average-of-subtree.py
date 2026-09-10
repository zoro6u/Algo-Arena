from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        count = 0
        stats = {None: (0, 0)}
        visited_children = set()
        stack = [root]

        while stack:
            node = stack[-1]
            if node not in visited_children:
                visited_children.add(node)
                if node.left and node.left not in stats:
                    stack.append(node.left)
                if node.right and node.right not in stats:
                    stack.append(node.right)
            else:
                left_sum, left_n = stats.get(node.left, (0, 0))
                right_sum, right_n = stats.get(node.right, (0, 0))
                total_sum = left_sum + right_sum + node.val
                total_n = left_n + right_n + 1
                stats[node] = (total_sum, total_n)
                if total_sum // total_n == node.val:
                    count += 1
                stack.pop()

        return count 