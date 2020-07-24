fname=input("Enter the file name: ")
handle=open(fname)
count=0
for i in handle:
    i=i.rstrip()
    s=i.split()
    if len(s)<1:
     continue
    if s[0]=="From:":
     continue
    else:
     if s[0]=="From":
        count=count+1
        print(s[1])
     else:
        continue
print("There were",count,"lines in the file with From as the first word")
