# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:51:51 2020

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
    def sortInsert(self,nd):
        n=Node(nd)
        curr=self.head
        if curr==None:
            n.next=n
            self.head=n
        elif curr.data>=n.data:
            self.push(nd)
        else:
            while curr.next!=self.head and curr.next.data<n.data:
                curr=curr.next
            n.next=curr.next
            curr.next=n
ll=LinkedList()
ll.push(5)
ll.push(3)
ll.push(2)
ll.push(1)
print('Given LinkedList')
ll.printList()
ll.sortInsert(6)
ll.push('\nGenerated LinkedList: ')
ll.printList()
                