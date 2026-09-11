class Solution:
    def maxPathSum(self, root):

        max_sum = float('-inf')

        def dfs(node):

            # Empty node contributes 0
            if node is None:
                return 0

            # Take only positive contributions from left and right
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through the current node
            current_path = left + node.val + right

            # Update the overall maximum path sum
            nonlocal max_sum
            max_sum = max(max_sum, current_path)

            # Return one branch to the parent
            return node.val + max(left, right)

        dfs(root)

        return max_sum
        