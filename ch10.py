# name = input("Enter file:")
name = 'extxt/mbox-short.txt'
watime = dict()
#if len(name) < 1 : name = "mbox-short.txt"
with open(name) as handle:
    for line in handle:
        if line.startswith('From '):
            line = (line.split()[5])
            line = (line.split(':')[0])
            watime[line] = watime.get(line, 0) +1
lis = list()
for h, c in watime.items():
    newtup = (h, c)
    lis.append(newtup)
lis = sorted(lis)
for h, c in lis:
    print(h, c)
