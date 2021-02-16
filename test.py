a = 3
print(a)
b = 10
print(b)
print(a + b)

price = 100
tax = 0.08
total_tax = price * tax
print(total_tax)

name = "氏名"
print(name)

print(1<3)
print(2 > 3)

print(3 == 3)
print(3 == 9/3)
print(2 != 3)
print("岩" == "岩")

print(type("name"))
print(type(name))

b = 4.5
print(type(b))

complex = 3j
print(type(complex)) 

flg = True
print(type(flg))

c = [10, 20, 30]
print(type(c))

d = {}
print(type(d))

e = ()
print(type(e))

names = ['田中','鈴木','佐藤']
print(names)
print(type(names))

print(names[0])

print(names[1])

scores = [50, 80, 60]
print(scores)
print(scores[0])
print(scores[-1])
print(scores[-2])
print(scores[0:2])
print(scores[0:])
print(scores[:-1])

scores.append(70)
print(scores)
scores.append(90)
print(scores)

scores.pop()
print(scores)

p = 5
if p < 6:
    print("great!")

money = 9000
if money >= 8000:
    print('ディズニーランドに行きます')
elif money >= 2000:
    print('映画館に行きます')    
else:
    print('映画館に行きません')