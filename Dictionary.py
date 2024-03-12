# Dictionary structure
import email


shopingCard = {
    "name": "whater",
    "number": 10,
    "price": 8000
}

# Keys
# Values
# for key_value in shopingCard.keys(), shopingCard.values():
for key in shopingCard.keys():
    # print(key)
    # print(key_value)
    print(shopingCard[key])


print("-----------------------------------")

# Items
# print(shopingCard.items())
# for item in shopingCard.items():
#     print(item)

for key, value in shopingCard.items():
    print(key, ":", value)

print("-----------------------------------")

# Dict
personalCard = dict(
    name="yasin",
    family="jaferi",
    age=19,
    email="mrjaferi.dev@gmial.com"
)

print(personalCard)

print(personalCard["name"])

# isExist = "email" in personalCard

if "email" in personalCard:
    print(personalCard["email"])
else:
    print("there is no eamil key in personalCard")


isNameExist = "yasin" in personalCard.values()
print(isNameExist)