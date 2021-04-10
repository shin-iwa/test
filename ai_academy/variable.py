# a = 10
# print(a)

# h = 1.71
# w = 64
# bmi = w / (h * h)
# print(bmi)

# i = 100
# f = 12.3
# w = 'hello'
# b = True
# print(i,f,w,b)

# y = 'こんにちは' + "\n" + 'わたしはMr.レッドラム'
# print(y)
# print(y[0])
# print(y[7:12])
# print(y[-3:])
# print(
# '''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 11111111111111111111'''
# )

# a = '100'
# print(a+'23')
# print(int(a)+23)

a = '100'
b = 'こんにちは'
print(a.isdigit())
print(b.isdigit())

b = 'こんにちは'
if b.isdigit():
    print(int(b)+23)
else:
    print('数値じゃないよ')