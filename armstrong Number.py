a=int(input("Enter the Number:"))
n=a
k=0
while a>0:
    b=a%10
    k=k+b**3
    a=a//10
print(k)
if n==k:
    print("It is armstrong Number")
else:
    print("It is not armstrong Number")
