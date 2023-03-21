from array import *
input = [[1,1,1,1], [12,12,12,12], [0,2]]
print("Array before Deletion of elements: ")
print(input)

del(input[1])
print("Array after Deletion of elements: ")
for x in input:
    for y in x:
        print(y,end = " ")
    print()