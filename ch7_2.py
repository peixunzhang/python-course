# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
with open(fname) as fh:
    count = 0
    agg = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        count = count + 1
        cut = float(line[19:].rstrip())
        agg = agg + cut
avg = agg/count
print("Average spam confidence:" ,avg)
