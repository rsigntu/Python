#Example of single try and catch block
print("start")
a=int(input("enter first number"))
b=int(input("enter second number"))
try:
       z=a/b
       print(z)
except(ZeroDivisionError):
       print("second value cannot be zero")
print("end")
