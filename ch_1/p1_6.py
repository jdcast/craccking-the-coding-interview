#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###
#Time = O(n + p^2) where n is length of string and p is number of sequences (naive string concatenation is very slow)
#Space = O(n)
###

def strCompress(string):
    res = ""
    curr_ch = ""
    curr_count = 0
    for idx, ch in enumerate(string):
        if curr_ch == "":
            curr_ch = ch
            curr_count = 1
        elif curr_ch != ch:
            res += curr_ch
            res += str(curr_count)
            curr_ch = ch
            curr_count = 1
        else:
            curr_count += 1
    res += curr_ch
    res += str(curr_count)
   
    if len(res) >= len(string):
        return string
    else:
        return res
    

if __name__ == "__main__":
    assert(strCompress("taco cat") == "taco cat")
    assert(strCompress("aardvark") == "aardvark")
    assert(strCompress("mmooonnb") == "mmooonnb")
    assert(strCompress("mmmmmmmooonnbbbbb") == "m7o3n2b5")
    print("All tests passed")


