user=int(input("Enter the Number:"))
count=0
i=1
while i<=user:
    if user%i==0:
        count+=1
    i+=1
if count==2:
    print(user,"It is Prime Number")
else:
    print(user,"It is not a Prime Number")




        
    
   


        
