# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:29:57 2020

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
        print('\n')
    def delete(self,k):
        curr=self.head
        c=1
        while True:
            if curr.next==self.head and curr==self.head:
                break
            while c<k-1:
                curr=curr.next
                c=c+1
            if curr.next==self.head:
                curr.next=curr.next.next
                self.head=curr.next
                self.printList()
            else:
                curr.next=curr.next.next
                self.printList()
            c=0
            
            
                
            
ll=LinkedList()
for i in range(5,0,-1):
    ll.push(i)
print('Given List: ')
ll.printList()
print('Generated List: ')
ll.delete(3)
                
        
        
        
        
        