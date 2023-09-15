class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head
        
        while fast_pointer and fast_pointer.next:
            #print(f'fast_pointer: {fast_pointer}')
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            #print(f'slow_pointer next: {slow_pointer.next}')
            
        return slow_pointer


