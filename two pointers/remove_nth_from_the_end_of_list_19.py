# this code is just an example, it cant be executed correctly.

# given:
nums = [1,2,3,4,5]
n = 2

# answer:
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = s = head
        
        for _ in range(n):
            f = f.next
        
        print(s)
        
        if not f:
            return s.next
        
        while f.next:
            s = s.next
            f = f.next
        
        s.next = s.next.next 
        return head