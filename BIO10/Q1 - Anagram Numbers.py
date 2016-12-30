n = int(input(">"))
ls = []
for i in range(2, 10):
    x = str(n*i)
    subl = []
    for char in x:
        subl.append(char)
    ls.append(subl)
goods = []
for i in range(0, len(ls)):
    nos = 0
    trie = ls[i]
    dead = False
    while len(trie) > 0 and dead != True:
        char= trie[0]
        if char in str(n):
            nos += 1
        else:
            dead = True
        trie.remove(char)
    if dead != True:
        goods.append(str(i+2))
if len(goods) == 0:
    print("NO")
else:
    guid = "" 
    for good in goods:
        guid += good +  " "
    print(guid)
