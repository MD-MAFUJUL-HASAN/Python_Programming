numberofdigits = 0
numberofwords = 0
numberofletters = 0

n = input("Enter your valuable text = ")
for x in n:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberofletters = numberofletters + 1
    elif x >= '0' and x <= '9':
        numberofdigits = numberofdigits + 1
    elif x == ' ':
        numberofwords = numberofwords+ 1
print("Number of Letters = ",numberofletters)
print("Number of Digits = ",numberofdigits)
print("Number of Words = ",numberofwords+1)
