import math

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(h, w, c):
    area = math.ceil((h * w) / c)
    print(f"You'll need {area} cans of paint.")


paint_calc(test_h, test_w, coverage)
