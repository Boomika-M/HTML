n=str(input("Enter the string:"))
a=''.join(reversed(n))
if a==n:
    print("Palindrome")
else:
    print("Not a palindrome")