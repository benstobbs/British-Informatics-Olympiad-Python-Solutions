rule = input(">")
p1 = input(">")
p2 = input(">")

def expandblock(symbol, block):
    if symbol == "?":
        return ["",block]
    else:
        poss = []
        cpos = ""
        while len(cpos) <= 12:
            poss.append(cpos)
            cpos = cpos + block
        return poss

def genpos(ruleset):
    if len(ruleset) == 1:
        return ruleset[0]
    else:
        poss = []
        for r in ruleset[0]:
            [poss.append(r + g) for g in genpos(ruleset[1:])]
        return poss

def compare(pw,allposs):
    def match (password, r):
        if len(password) != len(r):
            return False
        i = 0
        for char in password:
            if r[i] == "d":
                if int(char) >= int(password[i-1]):
                    return False
            elif r[i] == "u":
                if int(char) <= int(password[i-1]):
                    return False    
            i += 1
        return True

    for p in allposs:
        if match(pw, p):
            return True
    return False

i = 0

ruleset = []

for char in rule:
    if char == "*" or char == "?":
        if rule[i-1] == ")":
            bracketcounter = i-2
            while rule[bracketcounter] != "(":
                bracketcounter -= 1
            block = rule[bracketcounter+1:i-1]
            for _ in range(i-bracketcounter):
                ruleset.pop(-1)
        else:
            block = rule[i-1]
            ruleset.pop(-1)
        ruleset.append(expandblock(char, block))
    else:
        ruleset.append([char])

    i += 1

allposs = genpos(ruleset)

for p in [p1,p2]:
    if compare(p, allposs):
        print("Yes")
    else:
        print("No")
