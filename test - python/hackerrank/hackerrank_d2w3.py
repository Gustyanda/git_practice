# ----- memecah nilai berdasarkan kategori dan kemudian membagi berdasarkannya panjangan array
def data(arr):
    count_pst = 0
    count_ngt = 0
    count_zro = 0
    for x in range(0, len(arr)):
        if arr[x] > 0:
            count_pst = count_pst + 1
        elif arr[x] < 0:
            count_ngt = count_ngt + 1
        else:
            count_zro = count_zro + 1
    pst = (count_pst/len(arr))
    ngt = (count_ngt/len(arr))
    zro = (count_zro/len(arr))
    # print ('{:.6f}'.format(pst))
    # print ('{:.6f}'.format(ngt))
    # print ('{:.6f}'.format(zro))
    print(round(pst,6))
    print(round(ngt,6))
    print(round(zro,6))

(data([-4, 3, -9, 0, 4, 1]))

# ----- membuat staircase
def data(n):
    for x in range(1,n+1):
        print(' '*(n-x)+'#'*x)

(data(6))

# ----- mengurangi total nilai array dengan nilai max/min
def data(arr):
    sum1 = (sum(arr) - max(arr))
    sum2 = (sum(arr) - min(arr))
    print (sum1,sum2)
(data([1,2,3,4,5]))

def data(arr):
    sum=0
    for x in range(len(arr)):
        sum = sum + arr[x]
    print(sum-max(arr),(sum-min(arr)))
(data([1,2,3,4,5]))

# ----- mencari jumlah angka tertinggi dalam array
def data(candles):
    count = 0
    c = candles[0]
    for x in range(0, len(candles)):
        if candles[x] > c:
            c = candles[x]
    for x in range(0, len(candles)):
        if candles[x] == c:
            count = count + 1
    return count
print(data([3,2,1,3]))

def data(candles):
    count = 0
    c = max(candles)
    for x in range(len(candles)):
        if candles[x] == c:
            count = count + 1
    return count
print(data([3,2,1,3]))

# ----- merubah format jam AM ke PM 
def data(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]
    elif s[-2:] == 'AM':
        return s[:-2]
    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[-2:]
    else:
        return str(int(s[:2])+12)+s[2:-2]
print(data('07:05:45PM'))