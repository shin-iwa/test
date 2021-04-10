lunch = ['おにぎり','パスタ','ハンバーガー','カレー']
print(lunch[2])

import random
kuji = ['大吉','中吉','小吉','凶']
print(random.choice(kuji))

from turtle import *
shape('turtle')
col = ['red','blue','green','brown','black']
for i in range(5):
    color(col[i])
    forward(200)
    left(144)
done()