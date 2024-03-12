# Dictionary methods
from tkinter import N


personalCard = dict(
    name="yasin",
    family="jaferi",
    age=19,
    email="mrjaferi.dev@gmial.com"
)

print(personalCard)

print('----------------------------------------')

# clear
# print(personalCard.clear())

print('----------------------------------------')

# copy
copyPersonalCard = personalCard.copy()
print(copyPersonalCard)

print('----------------------------------------')

# fromkeys
user_1 = {"name": "unknown", "family": "unknown"}
user_2 = {}.fromkeys(["name"], "unknown")
user_3 = dict.fromkeys(["name"], "unknown")
print(user_2)
print(user_3)

print('----------------------------------------')

# get
print(personalCard.get("name"))
print(personalCard.get("phone"))
