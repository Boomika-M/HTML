import math
def generatePrime(n):
    X = 0
    i = 2
    l1=[]
    flag = False
    while(X < n):
        flag = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if (i%j == 0):
                flag = False
                break
        if(flag):
            l1.append(i)
            X+=1
        i+=1
    return l1   
N=int(input("Enter no of terms"))
l1=generatePrime(N)
n1=0
n2=1
l2=[0,1]
count=0
while count < N:
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       l2.append(nth)
l3=[]
for i in range(N):
     l3.append(l1[i])
     l3.append(l2[i])
b=' '.join(map(str,l3))
print(b)