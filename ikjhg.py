class Solution:
    def buildTree(self, inorder, postorder):
        index_map = {}

        for i in range(len(inorder)):
            index_map[inorder[i]] = i

        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            if left > right:
                return None

            # Last element in postorder is the root
            root_val = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_val)

            mid = index_map[root_val]

            # IMPORTANT: build right first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
