hrs = input("Enter Hours:")
rates = input("Enter Rates:")
h = float(hrs)
r = float(rates)
if h <= 40:
    pay = h * r
else:
    pay = 40 * r + (h-40) * r *1.5
print(pay)
