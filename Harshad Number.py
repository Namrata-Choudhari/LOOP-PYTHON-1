a=int(input("Enter the Number:"))
n=a
sum=0
while 0<a:
    x=a%10
    sum=sum+x
    a=a//10
print(sum)
if n%sum==0:
    print("It is harshad Number")
else:
    print("It is not harshad Number")
    