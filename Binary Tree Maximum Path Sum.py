class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through current node
            current_sum = node.val + left + right

            self.max_sum = max(self.max_sum, current_sum)

            # Return one side to parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
