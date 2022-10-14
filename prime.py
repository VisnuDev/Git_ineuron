

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
    
limit= input("Enter the limit: ")

for num in range(2, limit+1):
    res= prime(num)
    if res:
        print(f"{num} is a prime number")
