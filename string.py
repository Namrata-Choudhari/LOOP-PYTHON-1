string="studentsofnavagurukul"
print(len(string))
counter=0
while counter<len(string):
    if string[counter]=="o":
        counter+=1
        continue
    if string[counter]=="f":
        counter+=1
        continue
    print(string[counter])
    counter+=1
