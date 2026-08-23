class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)

        small_current = small
        large_current = large

        current = head

        while current:
            if current.val < x:
                small_current.next = current
                small_current = small_current.next
            else:
                large_current.next = current
                large_current = large_current.next

            current = current.next

        # Connect both lists
        small_current.next = large.next

        # Important: end the list
        large_current.next = None

        return small.next
