clock1 = 0
clock2 = 0
inp = input(">").split(" ")
offset1 = int(inp[0])+60
offset2 = int(inp[1])+60

def add():
    global clock1
    global clock2
    clock1 += offset1
    if clock1 > 1399:
        clock1 -= 1440
    clock2 += offset2
    if clock2 > 1399:
        clock2 -= 1440
        
add()
while clock1 != clock2:
    add()

hours = 0
while clock1 > 59:
    hours += 1
    clock1 -= 60
while hours > 23:
    hours -= 24

hours = str(hours)
minutes = str(clock1)

if len(hours) == 1:
    hours = "0" + hours
if len(minutes) == 1:
    minutes = "0" + minutes
    
print(hours + ":" + minutes)
