class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        def get_height(node):
            height = 0

            while node.left:
                height += 1
                node = node.left

            return height

        def exists(index, height, node):
            left = 0
            right = 2 ** height - 1

            for _ in range(height):
                mid = (left + right) // 2

                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1

            return node is not None

        height = get_height(root)

        if height == 0:
            return 1

        # Number of nodes before the last level
        nodes_before_last = 2 ** height - 1

        # Binary search on the last level
        left = 0
        right = 2 ** height - 1

        while left <= right:
            mid = (left + right) // 2

            if exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1

        # left = number of nodes in last level
        return nodes_before_last + left
