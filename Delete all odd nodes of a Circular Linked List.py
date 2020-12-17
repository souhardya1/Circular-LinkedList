# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:04:47 2020

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
    def delete(self):
        curr=self.head
        while True:
            if self.head.data%2!=0:
                self.head=self.head.next
            if curr.next.data%2!=0:
                curr.next=curr.next.next
            curr=curr.next
            if curr==self.head:
                break
ll=LinkedList()
ll.push(20)
ll.push(13)
ll.push(6)
ll.push(32)
ll.push(11)
ll.push(9)
ll.printList()
ll.delete()
print('\nGenerated LinkedList:')
ll.printList()
            