hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
if(h < 40):
    pay = h * r
else:
    h = h - 40
    pay = (40 * r) + h * (r * 1.5)
print(pay)