name=input("Enter the file name ")
if len(name)<1:
   name="mbox-short.txt"
fhand=open(name)
lis=list()
hours=dict()
for i in fhand:
    i=i.split()
    if len(i)<1:
       continue
    else:
       if i[0]=="From":
         stuff=i[5].split(":")
         lis.append(stuff[0])
for a in lis:
    hours[a]=hours.get(a,0)+1
temp=sorted(hours.items())
for b,c in temp:
    print(b,c)
