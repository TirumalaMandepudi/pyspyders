#13. WAP to check whether a given value is divisible by 5 and 7. If the value is divisible, to display the square of the values.
num=int(input("enter value:- "))
if(num%7==0 and num%5==0):
    print(num**2)
else:
    print(" not divisible by both ")