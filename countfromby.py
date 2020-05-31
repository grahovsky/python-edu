class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        super().__init__()
        self.val = v
        self.incr = i
    
    def __repr__(self) -> str:
        return str(self.val)

    def increase(self) -> None:
        self.val += self.incr

# g = CountFromBy(100, 10)
g = CountFromBy()
g.increase()

print(type(g))
print(id(g))
print(hex(id(g)))

print(g)

v = [1, 3, 5]
print(*v)

# Double asterisks example
kv = {'i': 10, 'v': 100}
j = CountFromBy(**kv)
print(j)
j.increase()
print(j)