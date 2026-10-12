num1=int(input("enter a number:"))
num2=int(input("enter a number2:"))
num3=int(input("enter a number3:"))
if(num2<num1 and num3<num1):
    print("the largest number is num1")
elif(num1<num2 and num3<num2):
    print("the largest number is num2")
else:
    print("the largest number is num3")
