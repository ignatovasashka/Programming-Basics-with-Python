import math
days = int(input())
food = int(input())
firstDogFood = float(input())
secondDogFood = float(input())
thirdDogFood = float(input())

foodEaten = (firstDogFood +secondDogFood +thirdDogFood) * days

if food >= foodEaten:
    print(f"{math.floor(food-foodEaten)} kilos of food left.")
else:
    print(f"{math.ceil(foodEaten-food)} more kilos of food are needed.")