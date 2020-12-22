# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 18:02:43 2020

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
    def swap(self):
        curr=self.head
        temp=self.head
        while curr.next!=self.head:
            curr=curr.next
        temp.data,curr.data=curr.data,temp.data
ll=LinkedList()
for i in range(5,0,-1):
    ll.push(i)
print('Given List:')
ll.printList()
ll.swap()
print('\nAfter Swapping: ')
ll.printList()
            