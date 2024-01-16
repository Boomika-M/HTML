a=int(input("Enter the number"))
thislist=[]
for num in range(1,a):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
            else:
                thislist.append(num)
print(thislist[-1])