s = ("aaaaaaaaaaaaaaaaaaaaaaaaaa"
     "bbbbbbbbbbbbbbbbbbbbbbbbbb")
print(s)
print(r'C:\name\name')
print("hello.\"Idon't know\"")

world = 'python'
print(world[0])
print(world[1])
print(world[-1])
print(world[0:2])
print(world[2:5])
print(world[:2])
print(world[2:])

world = 'j' + world[1:]
print(world)
print(world[:])
n = len(world[:])
print(n)

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)

print('###################')

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.replace('Mike','Nancy'))