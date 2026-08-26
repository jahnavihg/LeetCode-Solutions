class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # First element of preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find root position in inorder
        mid = inorder.index(root_val)

        # Left subtree
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )

        # Right subtree
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        return root
