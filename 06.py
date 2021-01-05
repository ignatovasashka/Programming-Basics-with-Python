key = int(input())
sum = 0
multiply = 0
resultNo = False

for a in range (1, 31):
    for b in range (1, 31):
        for c in range (1, 31):
            if a < b and b < c:
                sum = a+b+c
                if sum == key:
                    print(f"{a} + {b} + {c} = {sum}")
                    resultNo = True
            if a > b and b > c:
                multiply = a*b*c
                if multiply == key:
                    print(f"{a} * {b} * {c} = {multiply}")
                    resultNo = True

if resultNo == False:
    print("No!")