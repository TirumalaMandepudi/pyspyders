#14. WAP to check whether the given value's last digit is greater than 5 or not. if greater, to perform the bitwise right shift operator (skipping value is 2)
num=int(input("enter value:- "))
a=str(num)
b=a[-1]
c=int(b)
if(c>5):
    print(num+3)
else:
    print("not greater")
