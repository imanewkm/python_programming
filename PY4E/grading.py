try:
    score = float(input("Enter a score between 0.0 and 1.0: "))
    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Error: Score must be between 0.0 and 1.0.")
except ValueError:
    print("Error: Please enter a valid numeric score between 0.0 and 1.0")