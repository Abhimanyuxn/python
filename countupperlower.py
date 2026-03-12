a = input("enter text")

b=0
c=0

for ch in a:
    if ch.isupper():
        b=b+1
    elif ch.islower():
        c=c+1

print("lower alphabets are " , c)
print("upper alphabets are " , b)