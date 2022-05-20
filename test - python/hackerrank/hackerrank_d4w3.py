# ----- mencari nilai reantangan 1 - 100 dengan pembagian dari parameter
def getTotalX(a,b):
    c = []
    d = []
    e = []
    for x in range(1, 101):
        for num in a:
            if x % num == 0:
                c.append(x)
        for num1 in b :
            if num1 % x == 0:
                d.append(x)
    z = c+d
    for y in range(len(z)):
        if z.count(z[y]) == len(a+b):
            e.append(z[y])
    return len(set(e))
print(getTotalX([3, 4],[24,48]))

# ----- mencari nilai record
def data(scores):
    count_high = 0
    highest_scores = scores[0]
    count_low = 0
    lowest_scores = scores[0]
    for x in range(1,len(scores)):
        if highest_scores < scores[x]:
            highest_scores = scores[x]
            count_high += 1
    for y in range(1,len(scores)):
        if lowest_scores > scores[y]:
            lowest_scores = scores[y]
            count_low += 1
    return count_high,count_low
print(data([10,5,20,20,4,5,2,25,1]))
print(data([3,4,21,36,10,28,35,5,24,42]))
print(data([0,9,3,10,2,20]))