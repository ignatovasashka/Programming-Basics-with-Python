boughtFood = int(input())
command = ""
eatenFood = 0
totalFood = 0

while command != "Adopted":
    command = input()

    if command != "Adopted":
        eatenFood = int(command)
    else:
        break

    totalFood += eatenFood

if totalFood <= boughtFood*1000:
    print(f"Food is enough! Leftovers: {(boughtFood*1000)-totalFood} grams.")
else:
    print(f"Food is not enough. You need {totalFood-(boughtFood*1000)} grams more.")