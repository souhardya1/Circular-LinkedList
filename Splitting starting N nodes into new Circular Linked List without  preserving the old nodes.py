# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:15:44 2020

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
    def split(self,h1,k):
        temp=self.head
        c=1
        while temp.next!=self.head:
            if c==k:
                h1.head=temp.next
                temp.next=self.head
            c=c+1
            temp=temp.next
        curr=h1.head
        while curr.next!=self.head:
            curr=curr.next
        curr.next=h1.head
ll=LinkedList()
l1=LinkedList()
for i in range(5,0,-1):
    ll.push(i)
print('Given List:')
ll.printList()
print('\n1st List:')
ll.split(l1,3)
ll.printList()
print('\n2nd List:')
l1.printList()
                
                
            
        