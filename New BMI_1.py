
def bmi_():
    try:
        height = float(input("inter your height, please: "))  # in meters e.g., 1.55
        weight = int(input("inter your weight, please: "))  # in kilograms e.g., 72
    except ValueError:
        print("please enter an integer number and try again aa ")
        bmi_()
    else:
        # Your code below this line 👇
        bmi = weight / (height * height)
        if bmi < 18.5:
            print(f"Your bmi is {bmi}, you are underweight.")
        elif bmi < 25:
            print(f"Your bmi is {bmi}, you have a normal weight.")
        elif bmi < 30:
            print(f"Your bmi is {bmi}, you are slightly overweight.")
        elif bmi < 35:
            print(f"Your bmi is {bmi}, you are obese.")
        else:
            print(f"Your bmi is {bmi}, you are clinically obese.")


bmi_()
