memo = {}
def possible_scores(s, d, first_drat=False):
    if (s,d) in memo:
        return memo[(s,d)]

    segments = range(1,21)
    if first_drat:
        segments = [s*2 for s in segments]

    if d == 1:
        if s in segments:
            return 1
        else:
            return 0

    poss = 0
    for seg in segments:
        if seg <= s:
            poss += possible_scores(s-seg, d-1)

    if not first_drat:
        memo[(s,d)] = poss

    return poss

inp = input(">").split(" ")

s = int(inp[0])
d = int(inp[1])

print(possible_scores(s, d, True))