#fname = input("Enter file name: ")
fname = 'extxt/romeo.txt' # 1
l = [] # 1
with open(fname) as fh: # 1
    for line in fh: # 1
        for word in line.split(): # n_lines
            if word not in l: # n_words
                l.append(word) # n_words
l.sort() # 1
print(l) # 1
                