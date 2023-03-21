# xargs

def student(*details):          # *details নিলে আলাদা ভাবে parameter declare করা লাগে না
    print(details)
student(8137,"MD MAFUJUL HASAN")

def addition(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        sum = sum + num
    print("Summation = ",sum)


addition(20,30)
addition(20,30,40)
addition(20,30,40,50)