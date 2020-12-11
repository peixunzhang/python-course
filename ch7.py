# Use words.txt as the file name
fname = input("Enter file name: ")
with open(fname) as fh:
    print(fh.read().upper().rstrip())