def anagram():
    w1 = list(input(">"))
    w2 = list(input(">"))
    anagram = 0
    for char in w1:
        if char in w2:
            w2.remove(char)
        else:
            return False
    return True

if anagram() == True:
    print("Anagrams")
else:
    print("Not anagrams")
