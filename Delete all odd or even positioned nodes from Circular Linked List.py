# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:01:48 2020

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
    def deleteOdd(self):
        p=self.head
        while p.next!=self.head:
            p=p.next
        p.next=self.head.next
        i=1
        p=self.head
        self.head=self.head.next
        p.next=None
        curr=self.head
        while True:
            i=i+1
            if i%2==0:
                i=i+1
                curr.next=curr.next.next
            curr=curr.next
            if curr==self.head:
                break
    def deleteEven(self):
        curr=self.head
        i=1
        while True:
            if i%2!=0:
                i=i+1
                curr.next=curr.next.next
            curr=curr.next
            i=i+1
            if curr.next==self.head:
                break
ll=LinkedList()
for i in range(5,0,-1):
    ll.push(i)
ll.printList()
print('\nGenerated LinkedList:')
ll.deleteOdd()
# ll.deleteEven()
ll.printList()         
            
            
            
            