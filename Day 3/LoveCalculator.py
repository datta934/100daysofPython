print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1+name2
t = name.lower().count("t")
r = name.lower().count("r")
u = name.lower().count("u")
e = name.lower().count("e")
true = t + r + u +e
l = name.lower().count("l")
o = name.lower().count("o")
v = name.lower().count("v")
e = name.lower().count("e")
love = l + o + v + e
truelove = int(str(true) + str(love))

if(truelove < 10) or (truelove > 90):
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif(truelove >= 40) and (truelove <=50):
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")