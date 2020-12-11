score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("not a number")
    quit()
if s >= 0.9 and s <= 1.0:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
elif s < 0.6 and s >= 0.0:
    print('F')
else:
    print("worng score")