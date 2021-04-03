a=int(input("Enter the Number:"))
j=0
while (j<=a):
    count=0
    i=1
    while i<=j:
        if j%i==0:
            count+=1
        i+=1
    if count==2:
        print(j)
    j=j+1
# 1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97