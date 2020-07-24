filename=input("Enter the file name")
f=open(filename)
for i in f:
    i=i.rstrip()
    i=i.upper()
    print(i)
