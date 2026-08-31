class Solution:
    def goodNodes(self, root):

        def dfs(node, max_so_far):

            # Empty node contributes nothing
            if node is None:
                return 0

            count = 0

            # Check if current node is a good node
            if node.val >= max_so_far:
                count = 1

            # Update maximum value seen on the path
            max_so_far = max(max_so_far, node.val)

            # Explore left and right subtrees
            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)

            return count + left + right

        return dfs(root, root.val)