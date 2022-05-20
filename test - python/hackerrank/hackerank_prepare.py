# ----- 01. VIRAL ADVERTISING
# (mencari jumlah liked dengan rentangan panjang parameter, dan ditotalkan)
def data(n):
    shared = 5
    cumulative = []
    for x in range(0,n):
        liked = shared//2
        shared = liked*3
        cumulative.append(liked)
    return sum(cumulative)
print(data(3))


# ----- 02. SAVE THE PRISONER
# (mencari angka penyebaran menggunakan matematika)
def data(n,m,s):
    if (m + s - 1) % n == 0:
        return n
    else:
        return (m + s - 1) % n
print(data(4,6,2))
print(data(5,2,1))
print(data(5,2,2))


# ----- 03. CIRCULAR ARRAY ROTATION
# (membalikan angka array sesuai rotasi parameter)
def data(a,k,queries):
    for x in range(len(queries)):
        queries[x] = a[(queries[x]-k)%len(a)]
    return queries            
                
print(data([3,4,5],2,[1,2]))
