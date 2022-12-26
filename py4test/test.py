struct StructName:
    a = int
    b = float
    c = str
    d = bool
    init(a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


enum EnumName:
    A = 1
    B = 2
    C = 3

a = StructName(1, 2.0, "3", True)
b = EnumName.A
print(a.a, a.b, a.c, a.d)
print(b)

