class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers to the head of the linked list.
        slow = fast = head
        
        # Traverse the linked list using the fast pointer.
        while fast and fast.next:
            # Move the slow pointer one step at a time.
            slow = slow.next
            # Move the fast pointer two steps at a time.
            fast = fast.next.next
        
        # When the fast pointer reaches the end (or goes beyond it), 
        # the slow pointer will be at the middle node.
        return slow
