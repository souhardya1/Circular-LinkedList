# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:23:18 2020

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
        if self.head!=None:
            while True:
                print(curr.data,end=' ')
                curr=curr.next
                if curr==self.head:
                    break
    def delete(self,data):
        if self.head==None:
            return
        if self.head.data==data and self.head.next==self.head:
            self.head=None
            return self.head
        curr=self.head        
        p=None
        if self.head.data==data:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=curr.next
        while curr.next!=self.head and curr.next.data!=data:
            curr=curr.next
        if curr.next.data==data:
            p=curr.next
            curr.next=p.next
        else:
            print('Nothing Found')
ll=LinkedList()
ll.push(10)
ll.push(8)
ll.push(7)
ll.push(5)
print('Given LinkedList')
ll.printList()
print('\nGenerated LinkedList')
ll.delete(8)
ll.printList()