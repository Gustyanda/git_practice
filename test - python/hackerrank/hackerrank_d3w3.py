# ----- membandingkan nilai dan membulatkan
def data(grades):
    for x in range(len(grades)):
        input = grades[x]
        result = input % 5
        if grades[x] < 38:
            grades[x] = input
        else:
            if result == 3:
                input += 2
                grades[x] = input
            elif result == 4:
                input += 1
                grades[x] = input
    return grades
print(data([73,67,38,33]))

# ----- mencari jumlah himpunan bagian
def data(s,t,a,b,apples,oranges):
    count_apple = 0
    count_orange = 0
    for x in range(len(apples)):
        if apples[x] + a >= s and apples[x] + a <= t:
            count_apple += 1
    for y in range(len(oranges)):
        if oranges[y] + b >= s and oranges[y] + b <= t:
            count_orange += 1

    print(count_apple)
    print(count_orange)
(data(7,11,5,15,[-2,2,1],[5,-5]))

# ----- mencari hitungan pertmuan angka dari posisi dan lompatan
def data(x1,v1,x2,v2):
    if x1 < x2 and v1 < v2:
        return('NO')
    elif x1 > x2 and v1 > v2:
        return('NO')
    else:
        if v1-v2 != 0:
            count = (x1-x2) % (v1-v2)
            if count == 0:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
print(data(0,2,5,3))