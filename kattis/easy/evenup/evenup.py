class node:
    def __init__(self,val,next=None):
        self.next=next
        self.even=(val%2==0)
        
input()

nums = list(map(int,input().split()))
head=None
prev=None
curr=None
for num in nums:
    curr=node(num)

    if prev is not None:
        prev.next=curr
    if head is None:
        head=curr
    prev=curr
    

curr=head
prev=None
while curr!=None:
    if curr.next is not None and curr.even==curr.next.even:
        if prev is None:
            head=curr.next.next
            curr=head
        else:
            prev.next=curr.next.next
            curr=prev.next
    else:
        prev=curr
        curr=curr.next

curr=head
i=0
while curr!=None:
    i+=1
    curr=curr.next

print(i)
