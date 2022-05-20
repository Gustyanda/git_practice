# ----- 01. SUBARRAY DIVISION 
# (menjumlahkan index pertama dan selanjutnya, 
# berdasarakan panjangan parameter yang ditentukan didalam list parameter)
def data(s,d,m):
    count = 0
    for x in range(len(s)):
        if sum(s[x:x+m]) == d: #(slicing dari index element 0 ke 0+m dalam array s)
            count += 1
    return count
print(data([1,2,1,3,2],3,2))
print(data([1,1,1,1,1,1],3,2))
print(data([4],4,1))
print(data([2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1],18,7))


# ----- 02.  DIVISIBLE SUM PAIR
# (menghitung jumlah perulangan element dua index yang mana menghasilkan 
# nilai parameter yang ditentukan)
def data(n,k,ar):
    count = 0
    for x in range(n - 1): #(dalam rentangan n-1 == rentangan ar)
        y = x + 1 #(variable kedua, sebagai index bantuan pertambahan setelah index x)
        while y < n:
            if (ar[x] + ar[y]) % k == 0:
                count += 1
            y += 1 #(bentuk perintah lanjutan untuk kondisi while, tanpa arahan tambahan looping akan terus berjalan sampai crash)
    return count
print(data(6,5,[1,2,3,4,5,6]))
print(data(6,3,[1,3,2,6,1,2]))


# ----- 03. MIGARTORY BIRD
# (mencari nilai index perulangan terbanyak, dari element index terkecil dari array)
def data(arr):
    lst = (max(arr)+1)*[0] #(membentuk rentangan array sepanjang parameter tertinggi didalam array parameter)
    for x in arr:
        lst[x] += 1
    return lst.index(max(lst)) #(memanggil data element terendah pada maksimal perulangan element index)
print(data([9,9,9,1,10,10,10,3,3,3,3]))

def data(arr):
    return max(set(arr), key = arr.count)
print(data([1,4,4,4,5,3,3,3,2,2,2]))


# ----- 04. DAY OF PROGRAMMER
# (membuat dan menghitung berdasarkan jumlah hari yang ditentukan, dengan memperhatikan
# tahun kabisat dan normal serta tahun jullien yang digunakna oleh russia)
def data(year):
    leap_date = [31,29,31,30,31,30,31,31]
    other_date = [31,28,31,30,31,30,31,31]
    russian_date = [31,15,31,30,31,30,31,31]
    if year >= 1919:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            date = 256 - (sum(leap_date))
            month = len(leap_date) + 1
        else:
            date = 256 - (sum(other_date))
            month = len(other_date) + 1
    elif year == 1918:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            date = 256 - (sum(russian_date))
            month = len(russian_date) + 1
        else:
            date = 256 - (sum(russian_date))
            month = len(russian_date) + 1
    elif year <= 1917:
        if year % 400 == 0 or year % 4 != 0 and year % 100 != 0: 
            date = 256 - (sum(other_date))
            month = len(other_date) + 1
        else:
            date = 256 - (sum(leap_date))
            month = len(leap_date) + 1            
    return (f'{date}.{month:02d}.{year}')
print(data(2200))
print(data(2016))
print(data(1700))
print(data(1800))
print(data(1915))
print(data(1917))
print(data(2000))
print(data(1918))


# ----- 05. BILL DIVISION
# (mencari hasil dengan output spesifik)
def data(bill,k,b):
    x = (sum(bill)-bill[k])/2
    if x < b:
        print(int(b - x))
    elif x == b:
        print('Bon Appetit')
(data([3,10,2,9],1,7))
(data([3,10,2,9],1,12))


# ----- 06. SALES BY MATCH
# (menghitung angka yang muncul sepasang)
def data(n,ar):
    ar_pair = []
    count = 0
    for x in range(len(ar)):
        if ar[x] not in ar_pair:
            ar_pair.append(ar[x]) #(memasukan angka muncul kedalam table array baru untuk dieleminasi, jika sepasang)
        else:
            ar_pair.remove(ar[x]) #(mengeleminasi angka sepasang, lalu menghitung yang sepasang)
            count += 1
    return count
print(data(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(data(7,[1,2,1,2,1,3,2]))


# ----- 07. DRAWING BOOK
# (menghitung jumlah halaman terdekat dengan target parameter dari halaman awal atau maksimum halaman)
def data(n,p):
    page = 2
    return min((p//page-0),(n//page - p//page))
print(data(6,2))
print(data(5,4))
print(data(5,3))

# ----- 08. COUNTING VALLEY
# (mengghitung jumlah turunan lembah ketika melewati sealevel dari valley)
def data(steps, path):
    sealevel = 0
    valley = 0
    for x in path:
        if x == 'U':
            sealevel += 1
            if sealevel == 0:
                valley += 1
        elif x == 'D':
            sealevel -= 1

    return valley
print(data(8,'UDDDUDUU'))


# ----- 09. ELECTRONIC SHOP PROBLEM
# (menjumlahkan antara rentangan keyboard dan drive, untuk mencari nilai memungkinkan pembelian maximum dari harga)
def data(keyboards,drive,b):
    possible_buy = []
    for x in range(len(keyboards)):
        for y in range(len(drive)):
            a = keyboards[x] + drive[y]
            if a <= b:
                possible_buy.append(a)

    if not possible_buy: #(kondisi yang menyatakan output dari kemungkinan dan ketidak mungkinan kondisi diatas)
        return -1                  
    else:
        return max(possible_buy)
print(data([3,1],[5,2,8],10))
print(data([3,2],[5,4],7))


# ----- 10. CAT AND MOUSE
# (mencari nilai terdekat dari, dan menggembalikan sebagai nilai return)
def data(a,b,c):
    near_value = 0
    if abs(a - c) < abs(b - c):
        near_value = 'Cat A'
    elif abs(a - c) > abs(b - c):
        near_value = 'Cat B'
    else:
        near_value = 'Mouse C'
    return near_value
print(data(2,5,4))
print(data(1,2,3))
print(data(1,3,2))


# ----- 11. MAGIC SQUARE FORMING
# (mencari kemungkinan pergantian angka dengan langkah terkecil, dengan membandingkan sample case yang di buat dengan parameter)
def data(s):
    a = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]], #(sample case, kemungkinan magic square dengan perhitunngan 15 permasing horizontal dan vertikal)
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    index = []
    for i in a:
        count = 0
        for x in range(len(s)):
            for y in range(len(s)):
                if i[x][y] != s[x][y]: #(menjelaskan kemungkinan tidak sama pada kemungkinan yang dibuat)
                    count += abs(i[x][y] - s[x][y]) #(mengembalikan perhitungan pertukaran anatara kemungkinan dengan parameter)
        index.append(count)
    return min(index) #(mengeluarkan hasil langkah terkecil dari perbandingan i dan s)
    
print(data([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))


# ----- 12. PICKING NUMBER
# (mencari nilai angka urutan paling banyak terdekat)
def data(a):
    b = []
    a.sort()
    rev = a[::-1]
    for i in range(len(a)):
        k = []
        for j in range(i,len(a)):
            if rev[i]-rev[j] <= 1:
                k.append(rev[j])
        b.append(k)

    g = []
    for i in b:
        g.append(len(i))
        
    return max(g)
print(data([4,6,5,3,3,1]))
print(data([1,2,2,3,1,2]))
print(data([1,2,3,4,4,5,5]))


def data(a):
    a.sort()
    b = []
    b.append(a[0])
    sementara = []
    num = 0
    for i in range(1,len(a)):
        if abs(b[0] - a[i]) <= 1:
            b.append(a[i])
        if a[i] - b[-1] >= 2:
            sementara.append(b)
            b = []
            b.append(a[i])
        if a[i] - b[0] == 2:
            num = (a[i] + b[0]) // 2
            sementara.append(b)
            b = b[b.index(num):]
            b.append(a[i])
    sementara.append(b)
    return len(max(sementara, key=len))
print(data([4,6,5,3,3,1]))
print(data([1,2,2,3,1,2]))
print(data([1,2,3,4,4,5,5]))


# ----- 13. THE HURDLE RACE
# (mencari selisih angka tertinggi dan lompatan maksimal)
def data(k, height):
    a = (max(height) - k)
    if a >= 0:
        return a
    if a <= 0:
        return 0
print(data(1,[1,2,3,3,2]))
print(data(4,[1,6,3,5,2]))
print(data(7,[2,5,4,5,2]))


# ----- 14. DESIGN PDF VIEWER
# (mencari nilai value dari elemen tertentu, lalu nilai tertinggi dikalikan dengan retnagan pramameter)
def data(h, word):
    lst1 = list('abcdefghijklmnopqrstuvwxyz')
    a = []
    for x in range(len(word)):
        for y in range(len(lst1)):
            if word[x] == lst1[y]:
                a.append(h[y])

    return max(a) * len(word)
print(data([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],'abc'))


# ----- 15. UTOPIAN TREE
# (mencari nilai ke parameter tertentu, dengan kondisi penjumlahan sesuai dengan pertanyaan)
def data(n):
    a = list(range(n+1))
    b = 0
    c = []
    for x in range(len(a)):
        if a[x] % 2 == 0 or a[x] == 1 and a[x] == 2:
            b += 1
            c.append(b)
        if a[x] % 2 != 0:
            b *= 2
            c.append(b)
    return c[n]
print(data(5))


# ----- 16. ANGRY PROFESOR
# (kondisi mencari data absesnsi dipengaruhi oleh kelas jadi atau tidak)
def data(k,a):
    count_min = 0
    count_pstf = 0
    for x in a:
        if x <= 0:
            count_min += 1
        elif x > 0:
            count_pstf += 1

    if count_min >= k:
        return 'NO'
    elif count_pstf <= k:
        return 'YES'
    elif count_min < k:
        return 'YES'
    elif count_pstf > k:
        return 'NO'
print(data(3,[-2,-1,0,1,2]))
print(data(3,[-1,-3,4,2]))
print(data(2,[0,-1,2,1]))
print(data(9,[-50,0,64,14,-56,-91,-65,-36,51,-28]))


# ----- 17. BEAUTIFUL DAYS AT THE MOVIE
# (menghitung dengan memalikan element rentangan parameter yang ditentukan kemudian di mod parameter)
def data(i,j,k):
    count = 0
    for x in range(i,j+1):
        a = str(x) #(kondisi a dirubah menjadi str untuk dibalikan)
        b = a[::-1] #(membalikan element str a)
        if abs(int(a) - int(b)) % k == 0:
            count += 1
    return count
print(data(20,23,6))