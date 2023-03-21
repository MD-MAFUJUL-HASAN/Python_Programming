file = open("student.txt","r+")
#print(file.readable())

text = file.read()          # for read file
print(text)
"""
text = file.readlines()          # for list file
print(text)
"""
#using for loop
"""
for line in file:
    print(line)
"""
"""
size = len(text)            # for length
print(size)
"""
file.close()