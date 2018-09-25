#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###
#Time = O(n^2) (currently a bug exists if head is a duplicate...head is reached first and doesn't get removed)
#Space = O(n)
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

def removeDups(head):
    buff = []
    
    n = head
     
    while n.next != None:
        print "At node {}".format(n.data)
        if n.data not in buff:
            buff.append(n.data)
        else:
            print "in: removing: {}".format(n.data)
            head.deleteNode(n.data)
        n = n.next

    if n.data in buff:
        print "post: removing: {}".format(n.data)
        head.deleteNode(n.data)
    

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

    removeDups(a)
    
    n = a
    while n != None:
        print n.data
        n = n.next
