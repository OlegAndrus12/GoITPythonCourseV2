"""
In this example, the change made in the list did affect another list, indicating the list is shallowly copied.
Important Points: The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
"""


# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print("The original elements before shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print("The original elements after shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")
