pens = int(input())
markers = int(input())
cleaning = float(input())
percent = int(input())

money = (1-percent/100)*(pens * 5.8 + markers * 7.2 + cleaning * 1.2)

print(f"{money:.3f}")
