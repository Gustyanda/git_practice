# ----- 01. FIZZBUZZ
# (print output verticaly fizz buzz)
def data(n):
    for x in range(1,n+1):
        if x % 3 == 0:
            print ('Fizz')
        elif x % 5 == 0:
            print ('Buzz')
        else:
            print(x)
print(data(15))


# ----- 02. SIMPLE MAX DIFFERENCE
# ()
def data(px):
    a = []
    for x in range(len(px) - 1):
        for y in range(x + 1,len(px)):
            if px[x] > px[y]:
                pass
            elif px[x] < px[y]:
                b = px[y] - px[x]
                a.append(b)
    
    if not a:
        return -1
    else:
        return max(a)
print(data([7,1,2,5]))
print(data([7,5,3,1]))
print(data([7,2,3,10,2,4,8,1]))
print(data([1,5,6,8]))


def data(px):
    a = 0
    b =[]

    for x in range(0,len(px)-1):
            if px[x+1] > px[x]:
                a = px[x+1] - px[x]
                b.append(a)
            elif px[x+1] < px[x]:
                a = 0
                b.append(a)
                if b.count(0) == 2:
                    break
    if sum(b)==0:
        return -1
    return sum(b)
print(data([7,1,2,5]))


# ----- 03. STRING REDUCTION
# (menghilangkan value duplicate)
def data(s):
    sl =list(s)
    sl2 =list(s)
    count = 0
    for x in range(0,len(sl)):
        b = sl[x] 
        a = sl2.count(b)
        if a > 1:
            sl2.remove(sl[x])
            count += 1
        elif a == 1:
            pass
    return count

print(data('abaa'))
print(data('abccbabba'))


def data(txt):
    b = []
    count = 0
    for x in range(len(txt)):
        if txt[x] not in b:
            b.append(txt[x])
        else:
            b.remove(txt[x])
            count += 1
    return count
print(data('abcab'))
print(data('abcbca'))
print(data('aabcab'))
print(data('bcaaacabbca'))
print(data('abaa'))


def data(s):
    sl =list(s)
    sl2 =list(s)
    count = 0
    for x in range(0,len(sl)):
        b = sl[x] 
        a = sl2.count(b)
        if a > 1:
            sl2.remove(sl[x])
            count += 1
        elif a == 1:
            pass
    return count

print(data('abaa'))
print(data('abccbabba'))


def data(s):
    for x in range(0, len(s)):
            a = s[x]
            b = s.count(a)
            if b > 1 :
                s.remove(s[x])
                count += 1
            elif a == 1:
                pass
    return count

# ----- 04. CLOSED PATH
# (mencari jumlah lubang pada angka)
def data(n):
    a = list(str(n))
    count = 0
    for x in a:
        if x == '0' or x == '4' or x == '6' or x == '9':
            count += 1
        elif x == '8':
            count += 2
        else:
            count += 0
    return count
print(data(630))
print(data(880))
print(data(58902))


# ----- 05. REVERSED ARRAY QUERIES
# (membalikan posisi index sesuai parameter)
def data(arr, operations):
    for x in operations:
        arr[x[0]:x[1]+1] = reversed(arr[x[0]:[1]+1])
    return arr
print(data([5, 2, 5, 1], [[1, 2], [1, 1]]))
print(data([9,8,7,6,5,4,3,2,1,0],[[0,9],[4,5],[3,6],[2,7],[1,8],[0,9]]))