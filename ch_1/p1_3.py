#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###
#Time = O(n^2)
#Space = O(1)
###

def urlify(char_arr):
    for idx, ch in enumerate(char_arr):
        if ch == " ":
            char_arr[idx+3:] = char_arr[idx+1:-2]
            char_arr[idx:idx+3] = ['%', '2', '0']
        print(char_arr)

    return char_arr


if __name__ == "__main__":
    assert(urlify(['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', '', '', '', '']) == ['M', 'r', '%', '2', '0', 'J', 'o', 'h', 'n', '%', '2', '0', 'S', 'm', 'i', 't', 'h'])

    print("All tests passed")


