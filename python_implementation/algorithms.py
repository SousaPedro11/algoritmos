from abc import ABC, ABCMeta, abstractmethod
from functools import reduce


class Problema(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def solv(self):
        raise NotImplementedError('Falta implementar')


class Fatorial(Problema):
    def __init__(self, n: int) -> None:
        self.n = n

    def solv(self) -> int:
        if self.n <= 1:
            return 1
        else:
            fat = 1
            for i in range(2, self.n+1):
                fat *= i
            return fat


class FatorialReduce(Problema):
    def __init__(self, n: int) -> None:
        self.n = n

    def solv(self):
        return 1 if self.n in (0, 1) else reduce(
            lambda x, y: x * y, range(1, self.n + 1))


class Fibonacci(Problema):
    def __init__(self, n: int) -> None:
        self.n = n

    def solv(self):
        a, b = 0, 1

        for _ in range(1, self.n + 1):
            a, b = b, a + b
        return a


class FibonacciLambda(Problema):
    def __init__(self, n: int) -> None:
        self.n = n

    def solv(self):
        def fib(n): return reduce(lambda x, _: [
            x[1], x[0]+x[1]], range(n), [0, 1])[0]
        return fib(self.n)


class FibonacciValue(Problema):
    def __init__(self, n: int) -> None:
        self.n = n

    def solv(self):
        a, b = 0, 1
        while b <= self.n:
            print(a)
            a, b = b, a + b
        return a
