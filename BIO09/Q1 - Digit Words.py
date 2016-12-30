w = input(">")
digits = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
goods = 0
for i in range(1, len(digits)):
    digit = digits[i]
    good = True
    tempw = list(w)
    #print(tempw)
    for char in digit:
        if char in tempw:
            #print(char)
            for i in range(0, tempw.index(char)+1):
                tempw.pop(0)
        else:
            good = False
    if good == True:
        print(digits.index(digit))
        goods += 1
if goods == 0:
    print("NO")
