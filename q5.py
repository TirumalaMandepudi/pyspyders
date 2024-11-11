#w AP to check whether a given input is divisible by 3 or 5. If the condition is satisfied, the number is converted to a string and then string to list.
# 1/p: 30
# o/p: '3','0']

num=(int(input("enter num:- ")))
if (num%3==0 and num%5==0):
    a=str(num)
    b=list(a)
    print(b)
    

    
    
    #print(list(a))
else:
    print("not divisible by 3 and 5")

    