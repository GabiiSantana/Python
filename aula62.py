import copy

d1 = {1:'a', 2:'b', 3:'c', 'd':['Gabrielly', 'Santana']}
n = copy.deepcopy(d1)

n[1] = 'Nicholas'
n['d'][0] = 'Nicholas'

print(d1)
print(n)