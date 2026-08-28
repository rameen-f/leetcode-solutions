class Solution:
    def diameterOfBinaryTree(self, root):

        diameter = 0

        def height(node):

            # Empty node has height 0
            if node is None:
                return 0

            # Find the height of left and right subtrees
            left = height(node.left)
            right = height(node.right)

            # Diameter passing through the current node
            nonlocal diameter
            diameter = max(diameter, left + right)

            # Return height of the current node
            return max(left, right) + 1

        height(root)

        return diameter
        