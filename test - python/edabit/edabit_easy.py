#---- 01. SQUARE EVERY DIGIT
# (memangkatkan nilia index, dan output menjadi nilai int dengan output di tentukan)
def data(n):
    c = ''
    a = str(n)
    for x in a:
        b = str(int(x)**2)
        c += b
    return int(c)

print(data(123))
print(data(9119))


#---- 02. FIND THE MISSING NUMBER
# (mencari nilai hilang dengan formula perhitungan)
def data(lst):
    n = len(lst)
    formula_total = (n + 1)*(n + 2)/2
    sum_total = sum(lst)
    return abs(formula_total - sum_total)
print(data([2,3,4,5]))
print(data([7, 2, 3, 6, 5, 9, 1, 4, 8]))


#---- 03. TRAVELING SALESMAN PROBLEM
# (math factorial)
from math import factorial

def data(n):
    if n == 1:
        return 1
    else:
       return n * factorial(n - 1)
print(data(4))
print(data(2))
print(data(1))
print(data(9))


def data(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
print(data(4))
print(data(9))


#---- 04. CONVERT YEAR TO CENTURY
# ()
def data(century):
    return century // 100 + 1
print(data(1801))


#---- 05. FIND ODD INTEGER
# ()
def data(n):
    for x in n:
        if n.count(x) % 2:
            return x
print(data([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))


#---- 06. FILTER OUT STRING FROM AN ARRAY
# (memisahkan int dan str dari dalam array)
def data(n):
    int_num = []

    for x in n:
        if type(x) == int:
            int_num.append(x)
        else:
            pass
    return int_num
print(data([1, 2, "a", "b"]))
print(data([1, "a", "b", 0, 15]))