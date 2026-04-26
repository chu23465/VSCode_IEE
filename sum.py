class add():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def sum(self):
        return (a + b)
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))
x = add(a, b)
print(x.sum())