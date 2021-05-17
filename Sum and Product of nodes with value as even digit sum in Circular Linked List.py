# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:41:03 2020

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
    def digit(self,k):
            s=0
            while k and k>=1:
                s=s+int((k%10))

                k/=10
            if s%2==0:
                return 0
            else:
                return 1
    def addMul(self):
        curr=self.head
        a=0
        m=1
        while True:
            d=self.digit(curr.data)
            if d==0:
                a=a+curr.data
                m=m*curr.data
            curr=curr.next
            if curr==self.head:
                break
        return print('\nSum of Nodes: ',a,'Product of Nodes',m)
ll=LinkedList()

ll.push(13)
ll.push(6)
ll.push(8)
ll.push(16)
ll.push(15)
print('Given LinkedList:')
ll.printList()
ll.addMul()
            