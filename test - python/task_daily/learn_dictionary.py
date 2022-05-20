# --------------menggabungkan 2 list kedalam dictionary
def data(keys, value):
    output = dict(zip(keys,value))
    return output
print(data(['ten','twenty','thirty'],[10,20,30]))

# --------------menggabungkan 2 dictionary kedalam 1 dictionary
def data():
    list1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    list2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    list3 = {**list1,**list2}
    return list3
print(data())

def data():
    a = {'a': 'ayam', 'b': 'babi', 'c': 'cacing'}
    b = {'d': 'domba', 'e': 'elang', 'f': 'flamingo'}
    c = dict(a, **b)
    return c
print(data())

