# runtime error / incorrect input / incorrect code

# type_error
"""
when we don't use int but do the program as int then it should be a
type error of string

num = input("Enter a number = ")
result = 20/num        #here we enter any number but it return a type error
print(result)
"""
# zero_division_error
"""
when we take 0 as input then it gives us a zero division error in the output
num = int(input("Enter a number = "))
result = 20/num         #when number is 0 then it was a zero division error
print(result)
"""
# index_error
"""
text = "Tonmoy"
print(text[6])      #it gives a index error bcz we know index starts at 0
"""
# exception_handling
try:
    num = [20,0,30]
    result = num[0] / num[1]        #when index is more than 2 than it should be a index error
    print(result)
except ZeroDivisionError:
    print("Dividing by 0 is not possioble")
except IndexError:
    print("Index Error")
finally:            #এটা থাকলে program এ ভুল থাকলেও এর ভিতরের অংশ কাজ করবে
    print("Successful")