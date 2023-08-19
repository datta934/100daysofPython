bill = float(input("Please enter bill amount in $:"))
tip = int(input("Please enter tip 10, 12 or 15:"))
people = int(input("How many people should split it?"))
total_bill = (bill * (tip/100)) + bill
print(f"Each person should pay {round(total_bill/people, 2)}")