# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:35:23 2020

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
        temp = self.head 
        if self.head!= None: 
            while(True): 
                print (temp.data,end=' ')
                temp = temp.next
                if (temp == self.head): 
                    break
    def split(self,h1,h2):
        temp=self.head
        curr=self.head
        if self.head==None:
            return
        while temp.next!=self.head and temp.next.next!=self.head:
            temp=temp.next.next
            curr=curr.next
        if temp.next.next==self.head:
            temp=temp.next
        h1.head=self.head
        if self.head.next!=self.head:
            h2.head=curr.next
        temp.next=curr.next
        curr.next=self.head
ll=LinkedList()
h1=LinkedList()
h2=LinkedList()
ll.push(12)
ll.push(56)
ll.push(2)
ll.push(11)
print('Given List:')
ll.printList()
ll.split(h1,h2)
print('\n1st Split List:')
h1.printList()
print('2nd split List')
h2.printList()
h2.printList()

            
            
                