num1=input("enter number1 =")
num2=input("enter number2 =")
num3=input("enter number3 =")
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is",largest)
