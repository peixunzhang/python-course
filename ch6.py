text = "X-DSPAM-Confidence:    0.8475";
numpos = text.find('0')
n = int(numpos)
num = text[n:]
print(float(num))