#lambda function এর কোনো নাম থাকবে না
# lambda parameter : expression
"""
def calculate(a,b):
    return a*a + 2*a*b + b*b
"""
a = (lambda a,b: a*a + 2*a*b + b*b)(3,2)
print(a)