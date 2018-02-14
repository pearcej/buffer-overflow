'''
Python allows various ways to create and manipulate arrays.
If you use an array of a predetermined size you may encounter a buffer overflow.

From: http://cis1.towson.edu/~cssecinj/modules/cs0/buffer-overflow-cs0-python/
'''

buffer=[0]*5 #allocates array with 5 0s in it
importantData = 100
for i in range(0, 6):
    buffer[i]=7
print("after buffer overflow")
print(importantData)

