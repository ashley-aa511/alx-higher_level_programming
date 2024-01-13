#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, sub, divide, multiply
sum_result = add(a,b)
diff_result = sub(a,b)
quotient_result = divide(a,b)
prod_result = multiply(a,b)
print("Sum: {}".format(sum_result))
print("Difference: {}".format(diff_result))
print("Product: {}".format(prod_result))
print("Quotient: {}".format(quotient_result))
