# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:36:57 2020

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
        while curr.next!=self.head:
            curr=curr.next
        temp=curr
        curr=self.head        
        while curr.next!=self.head:
            c= self.digit(curr.data)
            if c==0:
                if curr==self.head:
                    curr=curr.next
                    temp.next=curr
                    self.head=curr
                else:    

                    curr=curr.next
                    temp.next=curr
            else:
                curr=curr.next
                temp=temp.next
    def digit(self,k):
            s=0
            while k and k>=1:
                s=s+int((k%10))

                k/=10
            if s%2==0:
                return 0
            else:
                return 1
ll=LinkedList()
ll.push(10)
ll.push(17)
ll.push(21)
ll.push(16)
ll.push(11)
ll.push(15)
print('Given LinkedList:')
ll.printList()
ll.delete()
print('\nGenerated LinkedList:')
ll.printList()
                    
                
            
            
        
        