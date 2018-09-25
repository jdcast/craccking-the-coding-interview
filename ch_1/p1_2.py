#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def isPerm(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    map_1 = {}
    for ch in str_1:
        if ch in map_1:
            map_1[ch] += 1
        else:
            map_1[ch] = 1
    
    map_2 = {}
    for ch in str_2:
        if ch in map_2:
            map_2[ch] += 1
        else:
            map_2[ch] = 1

    for key in map_1:
        if key not in map_2 or map_2[key] != map_1[key]:
            return False

    return True


if __name__ == "__main__":
    assert(isPerm("god", "dog") == True)
    assert(isPerm("God", "dog") == False)

    print("All tests passed")


