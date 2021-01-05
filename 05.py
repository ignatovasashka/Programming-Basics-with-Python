parts = int(input())
moneyPerPoint = float(input())
points = 0.0
totalPoints = 0.0
sum = 0.0

for parts in range(0,parts):
    points = int(input())

    if parts % 2 != 0:
        points = points*2

    totalPoints += points

sum = totalPoints*moneyPerPoint

print(f"The project prize was {sum:.2f} lv.")