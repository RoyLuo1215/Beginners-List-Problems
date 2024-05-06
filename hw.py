1
numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
print(max(numsList))
print(min(numsList))
average = sum(numsList) / len(numsList)
print(average)

2
stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

count = 0
for string in stringsList:
    if string[0].lower() == string[-1].lower():
        count += 1

print("Number of strings with same start and end characters:", count)

3
iLikePesto = []
otherFoods = []

for _ in range(8):
    favorite_food = input("What is your favourite food? ")
    if favorite_food.lower() == 'pesto':
        iLikePesto.append(favorite_food)
    else:
        otherFoods.append(favorite_food)

print("Pesto is loved by", len(iLikePesto), "people!")
for _ in range(len(iLikePesto)):
    print("I like pesto")

print("\nOther Foods:")
for food in otherFoods:
    print(food)

4
cerealList = []

while True:
    cereal = input("Enter Cereal: ")
    if cereal.lower() == 'sultana and bran' or cereal.lower() == 'weetbix':
        break
    else:
        cerealList.append(cereal)

print(cerealList)
