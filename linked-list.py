class LinkedNode:
  def __init__(self,val):
    self.next=next
    self.val=val

node1=LinkedNode(1)
node2=LinkedNode(2)
node3=LinkedNode(3)

node1.next=node2
node2.next=node3

# we initialize a pointer to head and tail to None
# we iterate over the list using pointer
# for each iteration we find the next node
# move tail to pointer, pointer to next node
def reverseLinkedList(head):
  pointer=head
  tail=None
  while pointer:
    nextNode=pointer.next
    pointer.next=tail
    tail=pointer
    pointer=nextNode
  return tail

# we use 2 pointer approach
# move slow pointer one at a time and fast pointer twice as fast
# our while condition is that loop till we have a fast and fast's next node
# we could think of using slow.next and fast.next but it wouldnt work because slow.next will always exist if fast.next exist since its twice as slow
# if the while condition is correct then there sure is a cycle 
# else there is an end to the list and we will get out of the loop
def hasCycle(self, head: Optional[ListNode]) -> bool:
  if head==None:
    return False
  slow=head
  fast=head
  while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
      return True
  return False
