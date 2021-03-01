class Machine():
    def __init__(self):
        self.rot1vals = ["A","B","C","D"]
        self.rot2vals = ["A","B","C","D"]

        self.makerot1(self.rot1vals)
        self.makerot2(self.rot2vals)

        self.reflector = {
            "A":"D",
            "B":"C",
            "C":"B",
            "D":"A",
        }

        self.rot1rev = self.genrev(self.rot1)
        self.rot2rev = self.genrev(self.rot2)

    def makerot1(self, v):
        self.rot1 = {
            v[0]:v[0],
            v[1]:v[3],
            v[2]:v[1],
            v[3]:v[2],
        }

    def makerot2(self, v):
        self.rot2 = {
            v[0]:v[0],
            v[1]:v[2],
            v[2]:v[1],
            v[3]:v[3]
        }

    
    def genrev(self, rotor):
        d = {}
        for k in rotor:
            d[rotor[k]] = k
        return d

    def rotatevals(self, vals):
        return [vals[3], vals[0], vals[1], vals[2]]

    def rotateRot1(self):
        self.rot1vals = self.rotatevals(self.rot1vals)
        self.makerot1(self.rot1vals)
        self.rot1rev = self.genrev(self.rot1)

    def rotateRot2(self):
        self.rot2vals = self.rotatevals(self.rot2vals)
        self.makerot2(self.rot2vals)
        self.rot2rev = self.genrev(self.rot2)

    def encrypt(self, letter):
        return self.rot1rev[self.rot2rev[self.reflector[self.rot2[self.rot1[letter]]]]]


n = int(input(">"))
n %= 16
s = input(">")

m = Machine()

i = 0
outs = ""
while i < (n + len(s)):
    if i >= n:
        outs += m.encrypt(s[i-n])
    m.rotateRot1()
    if i % 4 == 3:
        m.rotateRot2()
    i += 1

print(outs)