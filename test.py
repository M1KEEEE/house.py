import turtle as t

n = int(input("значение"))

t.shape("turtle")
t.speed(0)
for i in range(4):
        t.forward(n)
        t.right(90)
t.right(300)
t.forward(n)
t.left(240)
t.forward(n)

t.done()
t.done()
