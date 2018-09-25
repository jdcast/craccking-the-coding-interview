#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###
#Time = O(n)
#Space = O(n)
###

def isPalinedromePerm(string):
    char_set = {}
    numTwo = 0
    numSpaces = 0
    for idx, ch in enumerate(string):
        if ch != " ":
            if ch in char_set.keys():
                char_set[ch] += 1
                if char_set[ch] > 2:
                    return False
                else:
                    numTwo += 1
            else:
                char_set[ch] = 1
        else:
            numSpaces += 1

    if (len(string) - numSpaces) % 2 == 0 and numTwo == (len(string) - numSpaces):
        return True
    elif (len(string) - numSpaces) % 2 != 0 and numTwo == (len(string) - numSpaces - 1)/2:
        return True
    else:
        return False


if __name__ == "__main__":
    assert(isPalinedromePerm("taco cat") == True)
    assert(isPalinedromePerm("bob") == True)
    assert(isPalinedromePerm("cat") == False)

    print("All tests passed")


