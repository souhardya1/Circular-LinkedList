# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:25:39 2020

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
    def count(self):
        c=0
        curr=self.head
        while curr.next!=self.head:
            c=c+1
            curr=curr.next
        return print('Length of Circular LinkedList is: ',c)
ll=LinkedList()
for i in range(5,0,-1):
    ll.push(i)
ll.count()