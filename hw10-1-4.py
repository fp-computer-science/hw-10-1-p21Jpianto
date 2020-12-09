# Author: JAp (amdg) 12/9/20

def weightfinder():
    weight = float(input("Please put your weight in lbs"))
    height = float(input("Please put your height in inches"))

    bmi = weight / (height ** 2)

    print(str(bmi) + " is you bmi.")

    if bmi >= 40:
        print("You are extremely obese")
    elif bmi >= 30:
        print("You are obese")
    elif bmi >= 25:
        print("You are a bit overweight")
    elif bmi >= 19:
        print(" You are in a healthy weight class")
    else:
        print("you are underweight")


print(weightfinder())
