text = "X-DSPAM-Confidence:    0.8475"
length=len(text)
index=text.find(" ")
s=text[index:length]
f=float(s)
print(f)
