name=input("Enter the file ")
fhand=open(name)
count=dict()
lis=list()
for i in fhand:
    i=i.rstrip()
    s=i.split()
    if len(s)<1:
       continue
    else:
        if s[0]=="From":
           lis.append(s[1])
        else:
           continue
for c in lis:
    count[c]=count.get(c,0)+1
max=None
word=None
for x,y in count.items():
    if max is None or max<y:
       max=y
       word=x
print(word,max)
    
