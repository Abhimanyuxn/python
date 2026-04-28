f=open("demo","r")
lines=f.readlines()
for line in lines:
    print(line.strip())
    f.close()