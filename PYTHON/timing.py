h=int(input("Enter hour:"))
m=int(input("Enter minutes:"))
s=int(input("Enter Seconds:"))
p=input("Enter am or pm:")
if p.lower()=="pm" and h!=12:
    h+=12
elif p.lower()=="am" and h==12:
    h=0
print(f"{h:02d}:{m:02d}:{s:02d}")