#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###
#Time = O(n) 
#Space = O(1)
###

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def appendToTail(self, d):
        end = Node(d)
        n = self

        while n.next != None:
            n = n.next
        n.next = end

    def deleteNode(self, d):
        n = self

        if n.data == d:
            return self.next # moved head

        while n.next != None:
            if n.next.data == d:
                n.next = n.next.next
                return self
            n= n.next
        return self

def kthToLast(head, ith):
    current = head
    runner = head
    count = 0
    while runner != None:
        count += 1
        runner = runner.next
        if count > ith:
            current = current.next  
    return current
    

if __name__ == "__main__":
    a = Node(1)
    a.appendToTail(2)
    a.appendToTail(3)
    a.appendToTail(1)
    a.appendToTail(4)
    a.appendToTail(2)

    n = a
    while n != None:
        print n.data
        n = n.next
   
    k = 3
    kth = kthToLast(a, k).data
    print "{} to last is: {}".format(k, kth)
    
    n = a
    while n != None:
        print n.data
        n = n.next
