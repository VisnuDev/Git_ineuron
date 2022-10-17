

def prime(n):
    flag=0
    for i in range(2, n):
        if n%i == 0:
            flag=1
            break
    if flag==0:
        return True
    else:
        return False
    
lower_limit= input("Enter the lower limit: ")
upper_limit= input("Enter the upper limit: ")



for num in range(lower_limit, upper_limit+1):
    res= prime(num)
    if res:
        print(f"{num} is a prime number")
