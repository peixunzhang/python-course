#fname = input("Enter file name: ")
fname = 'extxt/mbox-short.txt'
count = 0
with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        if line.startswith('From '):
            print('Words', line)
            print(line.split()[1])
            count = count + 1
    #     for emails in line:
    #         emails.split('@')

            
            
    # count = count+1
print("There were", count, "lines in the file with From as the first word")
