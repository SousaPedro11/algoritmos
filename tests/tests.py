import unittest
from python_implementation.algorithms import (
    Fatorial,
    FatorialReduce,
    Fibonacci,
    FibonacciLambda,
    FibonacciValue,
)


class TestFatorial(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(Fatorial(0).solv(), 1)
        self.assertEqual(Fatorial(1).solv(), 1)
        self.assertEqual(Fatorial(2).solv(), 2)
        self.assertEqual(Fatorial(3).solv(), 6)
        self.assertEqual(Fatorial(4).solv(), 24)
        self.assertEqual(Fatorial(5).solv(), 120)
        self.assertEqual(Fatorial(6).solv(), 720)
        self.assertEqual(Fatorial(7).solv(), 5040)
        self.assertEqual(Fatorial(8).solv(), 40320)
        self.assertEqual(Fatorial(9).solv(), 362880)
        self.assertEqual(Fatorial(10).solv(), 3628800)

    def test_fatorial_reduce(self):
        self.assertEqual(FatorialReduce(0).solv(), 1)
        self.assertEqual(FatorialReduce(1).solv(), 1)
        self.assertEqual(FatorialReduce(2).solv(), 2)
        self.assertEqual(FatorialReduce(3).solv(), 6)
        self.assertEqual(FatorialReduce(4).solv(), 24)
        self.assertEqual(FatorialReduce(5).solv(), 120)
        self.assertEqual(FatorialReduce(6).solv(), 720)
        self.assertEqual(FatorialReduce(7).solv(), 5040)
        self.assertEqual(FatorialReduce(8).solv(), 40320)
        self.assertEqual(FatorialReduce(9).solv(), 362880)
        self.assertEqual(FatorialReduce(10).solv(), 3628800)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_value(self):
        self.assertEqual(FibonacciValue(0).solv(), 0)
        self.assertEqual(FibonacciValue(1).solv(), 1)
        self.assertEqual(FibonacciValue(2).solv(), 2)
        self.assertEqual(FibonacciValue(3).solv(), 3)
        self.assertEqual(FibonacciValue(4).solv(), 3)
        self.assertEqual(FibonacciValue(5).solv(), 5)
        self.assertEqual(FibonacciValue(6).solv(), 5)
        self.assertEqual(FibonacciValue(7).solv(), 5)
        self.assertEqual(FibonacciValue(8).solv(), 8)
        self.assertEqual(FibonacciValue(9).solv(), 8)
        self.assertEqual(FibonacciValue(10).solv(), 8)
        self.assertEqual(FibonacciValue(11).solv(), 8)
        self.assertEqual(FibonacciValue(12).solv(), 8)
        self.assertEqual(FibonacciValue(13).solv(), 13)

    def test_fibonacci(self):
        self.assertEqual(Fibonacci(0).solv(), 0)
        self.assertEqual(Fibonacci(1).solv(), 1)
        self.assertEqual(Fibonacci(2).solv(), 1)
        self.assertEqual(Fibonacci(3).solv(), 2)
        self.assertEqual(Fibonacci(4).solv(), 3)
        self.assertEqual(Fibonacci(5).solv(), 5)
        self.assertEqual(Fibonacci(6).solv(), 8)
        self.assertEqual(Fibonacci(7).solv(), 13)
        self.assertEqual(Fibonacci(8).solv(), 21)
        self.assertEqual(Fibonacci(9).solv(), 34)
        self.assertEqual(Fibonacci(10).solv(), 55)

    def test_fibonacci_lambda(self):
        self.assertEqual(FibonacciLambda(0).solv(), 0)
        self.assertEqual(FibonacciLambda(1).solv(), 1)
        self.assertEqual(FibonacciLambda(2).solv(), 1)
        self.assertEqual(FibonacciLambda(3).solv(), 2)
        self.assertEqual(FibonacciLambda(4).solv(), 3)
        self.assertEqual(FibonacciLambda(5).solv(), 5)
        self.assertEqual(FibonacciLambda(6).solv(), 8)
        self.assertEqual(FibonacciLambda(7).solv(), 13)
        self.assertEqual(FibonacciLambda(8).solv(), 21)
        self.assertEqual(FibonacciLambda(9).solv(), 34)
        self.assertEqual(FibonacciLambda(10).solv(), 55)
