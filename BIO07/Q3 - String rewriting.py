inp = input(">")
inp2 = input(">").split()
s = int(inp2[0])
p = int(inp2[1])

mapping = {
    "A":"B",
    "B":"AB",
    "C":"CD",
    "D":"DC",
    "E":"EE"
}

for _ in range(s):
    newstr = ""

    i = 0
    while i < len(inp) and len(newstr) < p+2:
        char = inp[i]
        newstr += mapping[char]
        i += 1
    
    inp = newstr


inp = inp[:p]
outs = ""
for letter in mapping.keys():
    outs += str(inp.count(letter))+" "
print(outs)