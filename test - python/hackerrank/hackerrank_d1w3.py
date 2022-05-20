# ----- menjumlahkan
def simpleArraySum(ar):
    num = 0
    for x in ar:
        num = num + x
    return num
print(simpleArraySum([1,2,3,4,10,11]))

def simpleArraySum(ar):
    num = sum(ar)
    return num
print(simpleArraySum([1,2,3,4,10,11]))

# ----- membandingkan array per index yang lebih besar
def compareTriplets(a, b):
    a_count = 0
    b_count = 0
    for x in range(len(a)):
        if a[x] > b[x]:
            a_count = a_count + 1
        elif a[x] == b[x]:
            a_count = a_count + 0
            b_count = b_count + 0
        elif a[x] < b[x]:
            b_count = b_count + 1
    return a_count,b_count          
print(compareTriplets([17,28,30],[99,16,8]))

# ----- menjumlahkan menggunakan loop
def aVeryBigSum(ar):
    count = 0
    for x in ar:
        count += x
    return count
print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))

# ----- menjumlahkan diagonal kiri dan kanan lalu dikurangkan
def diagonalDifference(arr):
    dig1 = 0
    dig2 = 0
    for x in range(0,len(arr)):
        dig1 = dig1 + arr[x][x]
    for y in range(0,len(arr)):     
        dig2 = dig2 + arr[y][len(arr) - y - 1]
    return abs(dig1 - dig2)

print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))