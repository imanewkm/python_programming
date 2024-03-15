def computepay(h, r):    
    if(h < 40):
        pay = h * r
    else:
        h = h - 40
        pay = (40 * r) + h * (r * 1.5)
        print("Pay", pay)
    return(pay)

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
    computepay(h, r)
except:
    print("Error, please enter numeric input")
    quit()