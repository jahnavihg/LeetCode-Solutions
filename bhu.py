class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            # Check if current has duplicates
            if current.next and current.val == current.next.val:

                duplicate_value = current.val

                # Skip all nodes with this value
                while current and current.val == duplicate_value:
                    current = current.next

                prev.next = current

            else:
                prev = current
                current = current.next

        return dummy.next
