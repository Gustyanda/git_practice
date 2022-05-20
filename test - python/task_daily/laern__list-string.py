# --------------dictionary
def data(dct):
    return (dct)
print (data({'a':'1','b':'2','c':'3'}))

# -------------len (jumlah rentangan)
def data(dct):
    return len(dct)
print (data({'a':'1','b':'2','c':'3'}))

# -------------min (nilai terendah)
def data(dct):
    return min(dct)
print (data([-100,-20,0,500]))

# -------------max (nilai tertinggi)
def data(dct):
    return max(dct)
print (data([-100,-20,0,500]))

# -------------concat (menggabungkan dua list)
def data():
    a = [1,2,3,4]
    b = [5,6,7]
    for x in range(len(b)):
        a.append(b[x])
    return a
print (data())

def data(lst1, lst2):
    for x in range(len(lst1)):
        lst2.append(lst1[x])
    return lst2
print (data([1,2,3],[4,5,6]))

# -------------adding operation
def data():
    a = [1,2,3]
    b = [4,5,6]
    c = [(a[0])+(b[0]),(a[1])+(b[1]),(a[2])+(b[2])]
    return c
print (data())

def data():
    a = [1,2,3]
    b = [4,5,6]
    c = []
    c.append(a[0]+b[0])
    c.append(a[1]+b[1])
    c.append(a[2]+b[2])
    return c
print (data())

def data():
    a = [1,2,3]
    b = [4,5,6]
    c = []
    for x in range(len(b)):
        c.append(a[x]+b[x])
    return c
print (data())

def data(lst1, lst2):
    c = []
    for x in range(len(lst1)):
        c.append(lst1[x]+lst2[x])
    return c
print (data([1,2,3,4],[5,6,7,8]))

# -------------string
def data():
    a = 'menjemukan'
    b = a[:4]
    c = a[4:]
    return (b,c)
print (data())

def data ():
    a = 'menjemukan'
    # b = a[0],a[1],a[2],a[3],a[4]
    # c = a[5],a[6],a[7],a[8],a[9]
    d = len(a)//2
    e = []
    f = []
    for x in range(d):
        e.append(a[x])
    for x in range(5,(len(a))):
        f.append(a[x])
    return (e,f)
print (data())

# -------------get last item
def data(lst):
    return lst[-1]
print (data([1, 2, 3]))

def data():
    a = ['1','2','apel','zebra']
    return a[-2:]
print(data())

# -------------menggabungkan 
def data(pair1, pair2):
    for x in range(len(pair2)):
        pair1.append(pair2[x])
    return pair1
print(data([1],[2]))

def data(pair1, pair2):
    for x in range(len(pair2)):
        pair1.append(pair2[x])
    return pair1
print(data([2,3,4],[1,2,3]))

# -------------condition 
def data(num):
    x = str(num)
    if num == x:
        return 'True'
    else:
        return 'False'
print(data('phone'))

# -------------condition string
def data(word):
    if (word) == 'macan':
        return word + ' ' + 'suka macan'
    elif word > 'macan':
        return word + ' akan menggoreng ' + 'macan'
    elif word < 'macan':
        return 'apa itu macan?'

print(data('macan kumbang'))

from itertools import count

# -------------count / menghitung rentangan dengan increment/decrement
def data():
    a = 'macan'
    count = 0
    for x in a:
        count = count + 2
    return count
print (data())

# -------------mencari index ke [x] dari list
def data(mix):
    return mix[5]
print (data([1,2,3,'a','b','c']))

# -------------mencari value dari index yang ditentukan permasing-masing list
# PENDING!!
def data(lst1,lst2):
    odd_index_list = lst1[1::2]
    even_index_list = lst2[0::2]
    odd_index_list.append(even_index_list)
    return odd_index_list

print(data([3, 6, 9, 12, 15, 18, 21],[4, 8, 12, 16, 20, 24, 28]))

# -------------input nama
def name_string(name):
	b = "Edabit"
	result = name + b
	return result
print(name_string('matt'))

def data(name):
    return name + 'Eddabit'
print(data('matt'))

# -------------menghitung panjangan stirng
def comp(txt1,txt2):
    if len(txt1) == len(txt2):
        return 'True'
    else:
        return 'False'
print(comp('a','b'))

def comp(txt1,txt2):
    return len(txt1) == len(txt2)
print(comp('AB','CD'))

# -------------operator untuk string
def repetition(txt, n):
	return txt * (n)

print(repetition('ab',3))
print(repetition('kiwi',1))
print(repetition('cherry',2))

def data(txt,n):
    return txt + n
print(data('sat','set'))

# -------------perkalian string (slicing)
def data(num):
    a = 'Burp'
    b = a[:2]
    c = a[3]
    return (b + (a[2]*num) + c)
print(data(69))

def data(num):
    return 'Bu' + ('r'*(num)) + 'p'
print(data(10))

# -------------penggabungan nama string
def data(name):
    return 'hello' + ' ' + (name)
print(data('gerald'))

# -------------boolean berdasarkan karakter terakhir
def data(name):
    return (name.endswith('n'))
print(data('Andin'))

def data(name):
    a = name[-1]
    return a == 'n'
print(data('Gera'))

def data(name):
    a = name[-1]
    if a == 'n':
        return True
    else:
        return False
print(data('Mamen'))

# -------------find function (mencari index ke dalam string)
def find(kata, ch):
    index = 0
    while index < len(kata):
        if kata[index] == ch:
            return ch + ' adalah index ke ' + str(index)
        index = index + 1
    return False
print(find('memuaskan', 'm'))

def find(str, ch):
  index = 0
  while index < len(str):
    if str[index] == ch:
      return ch + ' adalah indeks ke' + " % s " % index
    index += 1
  return False
print(find("coba dulu aja kali ya","y"))

# -------------looping counting(mencari element tertentu dari index ke.. )
def data():
    a = 'menyegarkan'
    count = 0
    for x in range(0,len(a)):
        if a[x] == 'a':
            count += 1
    return count

print(data())

# -------------mengganti menggunakan .replace atau char classification
txt = 'fauzAN'
new_txt = txt.replace(txt[4],txt[4].lower())
print(new_txt)

txt = 'fauzAN'
new_txt = txt.lower()
print(new_txt)

# -------------looping menggunakan while (!harap hati-hati)
a = 0
b = []
while a < 10:
    b.append(a+1)
    a += 1
print (b)