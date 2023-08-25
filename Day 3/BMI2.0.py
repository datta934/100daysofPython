height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = int(weight) / float(height ** 2)


def switch(bmi):
    if bmi < 18.5:
        return f"Your BMI is {bmi}, you are underweight."
    elif 18.5 < bmi < 25:
        return f"Your BMI is {bmi}, you have a normal weight."
    elif 25 < bmi < 30:
        return f"Your BMI is {bmi}, you are slightly overweight."
    elif 30 < bmi < 35:
        return f"Your BMI is {bmi}, you are obese."
    elif bmi > 35:
        return f"Your BMI is {bmi}, you are clinically obese."


print(switch(round(bmi)))
