class Solution:
    def kthSmallest(self, root, k):

        def inorder(node):
            if node is None:
                return None

            # Visit the left subtree first
            left_result = inorder(node.left)

            if left_result is not None:
                return left_result

            # Current node is visited
            nonlocal k
            k -= 1

            if k == 0:
                return node.val

            # Visit the right subtree
            return inorder(node.right)

        return inorder(root)
        