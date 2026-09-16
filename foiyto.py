class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right
