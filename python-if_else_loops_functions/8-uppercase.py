#!/usr/bin/python3

def uppercase(str):
    result = ""
    for i in str:
        if 97<= ord(i)<=122:
            result = result + chr(ord(i)-32)
        else:
            result = result+i
    print (result)
    
