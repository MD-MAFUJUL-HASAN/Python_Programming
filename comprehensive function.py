#[expression for item in list]

num = [1,2,3,4,5]
"""
result = list(map(lambda x: x*x,num))       #map function using lambda function
print(result)
"""
"""
result  = list(filter(lambda x: x%2==0,num)) #filter function using lambda function
print(result)
"""
result = [x*x for x in num]     #comprehensive list for map function
print(result)
result = [x for x in num if x%2==0]     #comprehensive list for filter function
print(result)