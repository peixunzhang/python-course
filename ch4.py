def computepay(h,r):
    if h <= 40:
        return (h * r)
    elif h > 40:
        return (40 * r + (h-40) * r * 1.5)

hrs = input("Enter Hours:")
rates = input("Enter Rates:")
r = float(rates)
h = float(hrs)
p = computepay(h,r)
print("Pay",p)