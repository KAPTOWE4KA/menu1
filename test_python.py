#В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
import math


def test_filter():
    assert list(filter(lambda x:x>5, [2,7,5,6])) == [7, 6]
    assert list(filter(lambda x: x == 0, [2, 7, 5, 6])) == []

def test_map():
    assert list(map(lambda x:x-1, [2,7,5,6])) == [1,6,4,5]
    assert list(map(lambda x: -1*x/x, [2, 7, 5, 6])) == [-1, -1, -1, -1]

def test_sorted():
    assert sorted([2,7,5,6]) == [2,5,6,7]
    assert sorted([1, 3, 2, 3]) == [1, 2, 3, 3]

def test_pi():
    assert math.pi == 3.141592653589793

def test_sqrt():
    assert math.sqrt(25) == 5
    assert math.sqrt(1) == 1

def test_pow():
    assert math.pow(2,3) == 8
    assert math.pow(5, -1) == 0.2

def test_hypot():
    assert math.hypot(2, 3) == math.sqrt(2 * 2 + 3 * 3)
