# 1*1 + 2*2 + 3*3 + ... + n*n
n = int(input("Enter the value of N = "))
sum = 0
for x in range(1,n+1,1):
    sum = sum + x*x
print("Summation is = ",sum)