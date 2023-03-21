marks= int(input("Enter your marks = "))

if marks >= 80:
    print("A+")
elif 70 <= marks < 80:
    print("A")
elif 60 <= marks < 70:
    print("A-")
elif 50 <= marks <60:
    print("B")
elif 40 <= marks <50:
    print("C")
elif 33 <= marks < 40:
    print("D")
else:
    print("F")