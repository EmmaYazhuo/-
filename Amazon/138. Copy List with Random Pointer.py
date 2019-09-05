# """
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
# """


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # hash table of original node to copy node
        # if original node alreay has a copy, return copy
        # so that we don't create it again.
        if head is None:
            return head
        curr=head
        dic={}
        while curr:
            if curr not in dic:
                newNode=Node(curr.val, None, None)
                dic[curr]=newNode
                if curr == head: headNode=newNode
            else:
                newNode=dic[curr]

            if curr.random:
                if curr.random not in dic:
                    newrandom=Node(curr.random.val, None, None)
                    dic[curr.random]=newrandom
                else:
                    newrandom=dic[curr.random]
                newNode.random=newrandom

            if curr.next:
                if curr.next not in dic:
                    newnext=Node(curr.next.val, None, None)
                    dic[curr.next]=newnext
                else:
                    newnext=dic[curr.next]
                newNode.next=newnext
            curr=curr.next
        return headNode





