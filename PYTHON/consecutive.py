print("Enter the number:")
n=input()
for i in range(len(n)-2):
    if(int(n[i])==int(n[i+1])-1==int(n[i+2])-2)or(int(n[i])==int(n[i+1])+1==int(n[i+2])+2):
        print("Yes")
        break
    else:
        print("No")
        break