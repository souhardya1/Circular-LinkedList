# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:32:41 2020

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
    def prime(self,k):
        lst=[]
        i=1
        if k>1 and k%2!=0:
            while i<=k:
                if k%i==0:
                    lst.append(i)
                i=i+1
        if len(lst)==2:
            return 1
        else:
            return 0
    def delete(self):
        curr=self.head
        while curr.next!=self.head:
            if curr==self.head:
                k=self.prime(curr.data)
                if k==1:
                    self.head=self.head.next
                else:
                    k=self.prime(curr.next.data)
                    if k==1:
                        curr.next=curr.next.next
            else:
                k=self.prime(curr.next.data)
                if k==1:
                    curr.next=curr.next.next
            curr=curr.next
ll=LinkedList()
for i in range(10,1,-1):
    ll.push(i)
print('Given List: ')
ll.printList()
ll.delete()
print('\nGenerated LinkedList: ')
ll.printList()
            
            
            
                    
                
                
                
                
        