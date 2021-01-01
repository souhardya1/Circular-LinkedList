# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:37:17 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        curr=self.head
        if self.head!=None:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
        else:
            new_node.next=new_node
        self.head=new_node
    def printList(self):
        curr=self.head
        while True:
            print(curr.data,end=' ')
            curr=curr.next
            if curr==self.head:
                break
    def execute(self,n,m):
        l=n
        c=1
        k=None
        curr=self.head
        while l!=1:
            k=None
            if c==m:
                k=curr.next
                curr.next=k.next
                l=l-1
                c=1
                curr=curr.next
            
            else:
                curr=curr.next
                c=c+1
                if c==m-1:
                    k=curr.next
                    curr.next=k.next
                    l=l-1
                    c=1
        return curr.data
ll=LinkedList()
for i in range(4,0,-1):
    ll.push(i)
print('Given List:')
ll.printList()
print('\nYou are free, Number: ',ll.execute(4,2))