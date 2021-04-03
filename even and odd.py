i=1
count=0
count1=0
sum=0
sum1=0
while i<=100:    
    if i%2==0:
        count=count+1
        sum=sum+i
        avg=sum/count       
    else:
        count1=count+1
        sum1=sum1+i
        avg1=sum1/count1
    i=i+1 
print(avg)                
print(avg1) 
