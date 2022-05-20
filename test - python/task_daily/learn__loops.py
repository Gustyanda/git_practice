# --------------looping find laregest number
def data(a):
    max_number = 0
    for x in a:
        if x > max_number:
            max_number = x
    return max_number
print(data([4, 5, 1, 3]))


