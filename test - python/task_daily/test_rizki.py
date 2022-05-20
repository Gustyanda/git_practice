# -----------1 (menggabungkan 2 list menjadi 1 dictionary)
def data(a,b):
    output = dict(zip(a,b))
    return output
print(data(['Ten', 'Twenty', 'Thirty'], [10, 20, 30]))

def data(a,b):
    c = {}
    for x in range(len(a)):
        c.update({a[x]:b[x]})
    return c
print(data(['Ten', 'Twenty', 'Thirty'], [10, 20, 30]))

# -----------2 (menggabungkan 2 dictionary menjadi 1 dictionary)
def data():
    list1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    list2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    list3 = {**list1,**list2}
    return list3
print(data())

# -----------3 mencari key dari dictionary
def data():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                    }
                }
            }
        }
    return sampleDict['class']['student']['marks']['history']
print(data())

# -----------4 (membalikan list element pertama keselanjutnya, menjadi element terakhir ke selanjutnya)
def data():
    list1 = (10, 20, 30, 40, 50)
    list2 = list1[::-1]
    return list2
print(data())

# -----------5 (menacari element index tertentu didalam tuple didalam list)
def data():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    find1 = tuple1[1]
    find2 = find1[1]
    return find2
print(data())

def access_value(tuple2):
    return tuple2[1][1]
tuples = ("Orange", [10, 20, 30], (5, 15, 25))
print(access_value(tuples))

# ----------------------------------new case
# -----------6 (mencari perhitungan factorial menggunakan loop)
def data(a):
    b = 1
    while a >= 1:
        b = b*a
        a = a-1
    return b
print(data(5))

# -----------7 (mencari nilai ganjil/genap menggunakan loop)
def data():
    lst = [10,23,24,35,65,78,90]
    lst_even = []
    lst_odd = []
    for x in lst:
        if x%2==0:
            lst_even.append(x)
        else:
            lst_odd.append(x)
    return lst_odd
print(data())

# -----------8 mencari index flot dirubah ke string dikembalikan ke value yang ditentukan
def data(input):
    a = str(input)
    if a[3:] == '0':
        return 'INTEGER'
    elif a[3] == '0':
        return int(a[4:])
    else:
        return int(a[3:])  
print(data(99.09))
print(data(99.78))
print(data(99.00))

# -----------9 (mencari jumlah elemen string tertentu menggunakan loop)
def data():
    txt = 'aku adalah seorang pesepak bola'
    count = 0
    for x in range(0, len(txt)):
        if txt[x] == 'l':
            count = count + 1
    return count
print(data())

# -----------10 (mencari perhitungan factorial menggunakan rekrusif)
def data(a):
    if a == 1:
        return a
    else:
        return a*data(a-1)
print(data(4))