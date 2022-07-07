# module
import os,sys

# coding
os.system("clear")
def convert(ask = ""):
    return [bin(ord(x))[2:].zfill(8) for x in ask]

text = str(input("Test > "))
binary = convert(text)
print("Binary > "+str(binary))
