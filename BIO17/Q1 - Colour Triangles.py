inp = list(input(">"))
while len(inp) > 1:
    newinp = []
    for i in range(1, len(inp)):
        if inp[i] == inp[i-1]:
            newinp.append(inp[i])
        else:
            cols = ["R","G","B"]
            cols.remove(inp[i])
            cols.remove(inp[i-1])
            newinp.append(cols[0])
    inp = newinp
print(inp[0])
