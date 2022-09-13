class Tetrahedron:
    def __init__(self, int: s1, int: s2, int: s3, int: s4, int: s5, int: s6) -> None:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def square(self) -> float:
        p1 = (self.s1 + self.s2 + self.s3) / 2
        p2 = (self.s1 + self.s4 + self.s5) / 2
        p3 = (self.s2 + self.s5 + self.s6) / 2
        p4 = (self.s3 + self.s4 + self.s6) / 2
        sq1 = (p1 * (p1 - self.s1) * (p1 - self.s2) * (p1 - self.s3) ) ** 0.5
        sq2 = (p2 * (p2 - self.s1) * (p2 - self.s4) * (p2 - self.s5) ) ** 0.5
        sq3 = (p3 * (p3 - self.s2) * (p3 - self.s5) * (p3 - self.s6) ) ** 0.5
        sq4 = (p4 * (p4 - self.s3) * (p4 - self.s4) * (p4 - self.s6) ) ** 0.5
        return sq1 + sq2 + sq3 + sq4

    def volume(self):
        return None

t1 = Tetrahedron(2, 2, 2, 2, 2, 2)
print(t1.square())
