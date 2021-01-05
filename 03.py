days = int(input())
roomType = input()
mark = input()
moneyPerRoom = 0.0

if roomType == "room for one person":
    moneyPerRoom = 18.0
elif roomType == "apartment":
    moneyPerRoom = 25.0
    if days <= 10:
        moneyPerRoom = 0.7*moneyPerRoom
    elif days > 10 and days <= 15:
        moneyPerRoom = 0.65*moneyPerRoom
    elif days > 15:
        moneyPerRoom = 0.5*moneyPerRoom
elif roomType == "president apartment":
    moneyPerRoom = 35.0
    if days <= 10:
        moneyPerRoom = 0.9*moneyPerRoom
    elif days > 10 and days <= 15:
        moneyPerRoom = 0.85*moneyPerRoom
    elif days > 15:
        moneyPerRoom = 0.8*moneyPerRoom

if mark == "positive":
    moneyPerRoom += 0.25*moneyPerRoom
else:
    moneyPerRoom -= 0.1*moneyPerRoom

totalMoney = moneyPerRoom*(days-1)

print(f"{totalMoney:.2f}")