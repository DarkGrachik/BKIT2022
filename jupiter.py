import requests
import json
import matplotlib.pyplot as plt

url = 'http://127.0.0.1:5000/20'
r = requests.get(url)
data = r.json()

def make_url(n):
    base = 'http://127.0.0.1:5000/'
    res = base + str(n)
    return res

def get_data(n):
    url=make_url(n)
    r=requests.get(url)
    return r.json()

n_list = [0, 5, 10, 15, 20]
for n in n_list:
    print('{} первых чисел Фибоначи в виде списочка: {}'.format(n, get_data(n)))

y = get_data(15)
x = list(range(1, len(y)+1))
fig = plt.figure(figsize = (7, 5))
plt.bar(x, y)
plt.xlabel('X')
plt.ylabel('Y' )
plt.title('Первые {} чиселок Фибоначи'.format(len(y)))
plt.show()


fig = plt.figure(figsize = (7, 5))
plt.plot(x, y)
plt.show()