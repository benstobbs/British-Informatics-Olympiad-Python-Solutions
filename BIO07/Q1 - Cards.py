points = 0
def sumto15(numbers, partial = [], target = 15):
    if len(partial) == 2 and partial[0] == partial[1]:
        global points
        points += 1

    s = sum(partial)
    if s == target:
        global points
        points += 1
    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        sumto15(remaining, partial + [n])

cards = input(">").split(" ")
cards = [int(n) for n in cards]
sumto15(cards)
print(points)
