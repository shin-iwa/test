# from turtle import *
# shape('turtle')
# # col = ['orange']
# for i in range(4):
#     color('orange')
#     forward(220)
#     left(90)
# done()

# from turtle import *
# shape("turtle")
# col = ['orange', 'limegreen','gold', 'plum', 'tomato']
# for i in range(5):
#     color(col[i])
#     circle(100)
#     left(72)
# done()

# from turtle import *
# shape("turtle")
# col = ['orange']
# for i in range(1):
#     color(col[i])
#     forward(200)
#     left(72)
#     forward(200)
#     left(72)
#     forward(200)
#     left(72)
#     forward(200)
#     left(72)
#     forward(200)
#     left(72)
#     # forward(100)
#     for i in range(5):
#         circle(100)
#         left(72)
# done()

from turtle import *
shape("turtle")
col = ['orange']
for i in range(1):
    color(col[i])
    forward(200)
    left(72)
    forward(200)
    left(72)
    forward(200)
    left(72)
    forward(200)
    left(72)
    forward(200)
    left(72)
    # forward(100)
    left(72)
    forward(325)
    for i in range(4):
        left(360-144)
        forward(325)
done()