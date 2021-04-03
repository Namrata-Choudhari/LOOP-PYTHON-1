a=int(input("Enter the number of rows:"))
# i=1
row=0
while row<a:
    space=a-row
    while space>0:
        print(end=" ")
        space=space-1
    num=row+1
    while num>0:
        print(num,end=" ")
        num=num-1
    row=row+2
    print()