class Solution:
    def invertTree(self, root):

        # If the current node is empty
        if root is None:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Invert the left subtree
        self.invertTree(root.left)

        # Invert the right subtree
        self.invertTree(root.right)

        # Return the inverted tree
        return root