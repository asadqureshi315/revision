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

# [2,4,3]+[5,6,4]=[7,0,8]
# initilize a tail and head to tail
# we are given 2 linked lists and have to add the number of both linkedlist value
# our loop will run if l1.val or l2.val or carry exist so even if either of the list ends we continue creating the new list and if both end then the carry will be used
# for every iteration we create a new node and move tail to the new node.
# set new node val to the sum of l1 val, l2 val and carry
# % for base, // for carry
# move p1 and p2
# return head.next
def addTwoNumbers(self, l1, l2):
  p1=l1
  p2=l2
  carry=0
  tail=ListNode(-1)
  head=tail
  while p1 or p2 or carry:
    newNode=ListNode()
    p1Val = p1.val if p1 else 0
    p2Val = p2.val if p2 else 0
    add=p1Val+p2Val+carry
    if add>=10:
      carry=add//10
      newNode.val=add%10
    else:
      newNode.val=add
      carry=0
    if p1:
      p1=p1.next
    if p2:
      p2=p2.next
    tail.next=newNode
    tail=newNode
  return head.next
