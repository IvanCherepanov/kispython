class Mealy:
    state = "A"

    def order(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "F":
            self.state = "G"
            return 9
        if self.state == "E":
            self.state = "A"
            return 8
        if self.state == "C":
            self.state = "F"
            return 4
        raise KeyError

    def peep(self):
        if self.state == "B":
            self.state = "B"
            return 2
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "G"
            return 6
        if self.state == "E":
            self.state = "F"
            return 7
        raise KeyError

    def coat(self):
        if self.state == "D":
            self.state = "E"
            return 5
        if self.state == "B":
            self.state = "C"
            return 1
        raise KeyError


def main():
    o = Mealy()
    return o



o = main()
print(o.order()) # 0
print(o.peep()) # 2
print(o.coat()) # 1
print(o.coat()) # KeyError
print(o.peep()) # 3
print(o.coat()) # 5
print(o.order()) # 8
print(o.order()) # 0
print(o.coat()) # 1
print(o.order()) # 4
print(o.peep()) # KeyError
print(o.order()) # 9

o = main()
print("=====================")
print(o.order()) # 0
print(o.order()) # KeyError
print(o.coat()) # 1
print(o.coat()) # KeyError
print(o.peep()) # 3
print(o.coat()) # 5
print(o.order()) # 8
print(o.order()) # 0
print(o.peep()) # 2
print(o.peep()) # 2
print(o.coat()) # 1
print(o.peep()) # 3
print(o.order()) # KeyError
print(o.coat()) # 5
print(o.peep()) # 7
print(o.order()) # 9