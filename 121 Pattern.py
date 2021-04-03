col=1
while col<=5:
    n=1
    while n<=5-col:
        print(end=" ")
        n+=1
    row=1
    while row<col:
        print(row,end=" ")
        row+=1
    j=0
    while j>0:
        print(j,end=" ")
        j=j+5
    print()
    col+=1