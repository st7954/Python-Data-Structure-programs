s=0
c=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
       continue
    l=len(line)
    i=line.find(" ")
    a=line[i+1:l]
    d=float(a)
    s=s+d
    c=c+1
avg=s/c
print("Average spam confidence:",avg)
