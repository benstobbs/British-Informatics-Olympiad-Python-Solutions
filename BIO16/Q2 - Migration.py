data = [[0 for x in range(25)] for y in range(25)]

def inp():#get input
    psn = input().split(" ")
    slist = input().split(" ")
    newslist = []
    for s in slist:
        newslist.append(int(s))
    return [int(psn[0]), int(psn[1]), int(psn[2]), newslist]    

def pgrid(data):#print the 5x5 section of the grid
    for i in range(14, 9, -1):
        rows = ""
        row = data[i]
        for i in range(10, 15):
            rows += str(row[i]) + " "
        print(rows)
    print(" ")

def migrate(data):#migrate every square until they're all done
    done = False
    while done != True:
        done = True
        for x in range(0, len(data)-1):
            for y in range(0, len(data[0])-1):
                if data[x][y] > 3:
                    done = False
                    data[x][y] -= 4
                    data[x+1][y] += 1
                    data[x-1][y] += 1
                    data[x][y+1] += 1
                    data[x][y-1] += 1
    return data

def step(data, pos):
    data[pos[1]+10][pos[0]+10] += 1
    data = migrate(data)
    return data

woop = inp()

p = woop[0]
n = woop[2]
slist = woop[3]

listn = 0
for i in range(0, n):
    pref = p
    count = 1
    while pref > 5:
        pref -= 5
        count += 1
    pos = [pref-1, 6-count-1]
    data = step(data, pos)

    p+= slist[listn]
    while p > 25:
        p -= 25

    listn += 1
    if listn > len(slist)-1:
        listn -= len(slist)
        
pgrid(data)
        
     
