# -----loops
def data(num):
    a = 0
    for x in num:
        if x > a:
            a = x
    return a
print(data([4, 5, 1, 3]))

# -----return max
def data(num):
    return max(num)
print(data([4, 5, 1, 3]))
