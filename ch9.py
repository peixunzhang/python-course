who = dict()
#name = input("Enter file:")
name = 'extxt/mbox-short.txt'
with open(name) as handle:
    for line in handle:
        line = line.rstrip()
        if line.startswith('From '):
            line = (line.split()[1])
            who[line] = who.get(line, 0) + 1
            
count = None
memails = None
for pp,num in who.items():
    if count is None or num > count:
        count = num
        memails = pp
print(memails, count)