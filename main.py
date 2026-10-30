#users input

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))

#logical part(comparison)

if num1>=num2 and num1>=num3:
    largest=num1

if num2>=num1 and num2>=num3:
    largest=num2

if num3>=num1 and num3>=num2:
    largest=num3

    #display largest number

print("The largest number is:",largest)

