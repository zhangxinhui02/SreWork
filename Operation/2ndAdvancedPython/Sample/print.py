class Fib():
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

fb = Fib()
print(fb[20])