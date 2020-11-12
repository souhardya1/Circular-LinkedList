# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 00:59:42 2020

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
        if self.head !=None:
            while (curr.next!=self.head):
                curr=curr.next
            curr.next=new_node
        else:
            new_node.next=new_node
        self.head=new_node
    def printList(self):
        curr=self.head
        if self.head!=None:
            while True:
                print(curr.data,end=' ')
                curr=curr.next
                if curr==self.head:
                    break
ll=LinkedList()
ll.push(10)
ll.push(8)
ll.push(7)
ll.push(5)
ll.push(2)
print('Circular LinkedList is: ')
ll.printList()
                
                