#wap to check whether given input is divisible by 2 and 6. If the condition is satisfied, convert the given number into a complex number
num=(int(input("enter num:- ")))
if (num%2==0 and num%6==0):
    print("divisible by 2 and 6")
    print(complex(num))
else:
    print("not divisible by 2 and 6")