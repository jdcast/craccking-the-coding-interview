#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###
#Time = All ops O(1)
#Space = O(n)
###
    
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = None

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top == None:
            print('Empty Stack')
            return

        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, d):
        t = StackNode(d)
        if self.top != None:
            if d <= self.top.min:
                t.min = d
                self.top.min = d
            else:
                t.min =  self.top.min
            
            t.next = self.top
        else:
            t.min = d

        self.top = t

    def peek(self):
        if self.top == None:
            print('Empty Stack')
            return

        return self.top.data

    def isEmpty(self):
        return self.top == None

    def stackMin(self):
        return self.top.min


if __name__ == "__main__":
    stack = Stack()
    
    stack.push(2)
    print(stack.top.data)
    print(stack.stackMin())
    print('')
    stack.push(1)
    print(stack.top.data)
    print(stack.stackMin())
    print('')
    stack.push(-1)
    print(stack.top.data)
    print(stack.stackMin())
    print('')
    stack.push(3)
    print(stack.top.data)
    print(stack.stackMin())
    print('')
    stack.push(0)
    print(stack.top.data)
    print(stack.stackMin())
    print('')

    assert(stack.stackMin() == -1)
    print("All tests passed")
