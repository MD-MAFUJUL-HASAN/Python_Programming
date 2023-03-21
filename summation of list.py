n = input("Enter you desired number = ")
list = n.split()
sum = 0
for num in list:
    sum = sum + int (num)
print("Summation is = ",sum)