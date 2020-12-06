# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:01:03 2020

@author: Souhardya
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        curr=self.head
        while True:
            print(curr.data,end=' ')
            curr=curr.next
            if curr==self.head:
                break
    def addBegin(self,new_data):
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
        return self.head
    def addEnd(self,data):
        curr=self.head
        if self.head==None:
            return self.addEmpty(data)
        while True:
            curr=curr.next
            if curr.next==self.head:
                break
        new_node=Node(data)
        new_node.next=self.head
        curr.next=new_node
    def addBetween(self,data,item):
        if self.head==None:
            return
        new_node=Node(data)
        curr=self.head
        while curr.data!=item:
            curr=curr.next
        new_node.next=curr.next
        curr.next=new_node
        
        
        
ll=LinkedList()

ll.addBegin(2)
ll.addBegin(1)
ll.addEnd(8)
ll.addEnd(12)
ll.addBetween(9,8)
ll.printList()
            
        
        