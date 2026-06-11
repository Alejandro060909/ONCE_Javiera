print("escribiras una matriz 3x3")
u = []
iu = []
uo = []
a = float(input("ingresa el la posicion 1,1 "))
b = float(input("ingresa el la posicion 1,2 "))
c = float(input("ingresa el la posicion 1,3 "))

f = float(input("ingresa el la posicion 2,1 "))
g = float(input("ingresa el la posicion 2,2 "))
h = float(input("ingresa el la posicion 2,3 "))

k = float(input("ingresa el la posicion 3,1 "))
l = float(input("ingresa el la posicion 3,2 "))
m = float(input("ingresa el la posicion 3,3 "))

u.append(a)
u.append(b)
u.append(c)

iu.append(f)
iu.append(g)
iu.append(h)

uo.append(k)
uo.append(l)
uo.append(m)
print()
print("tu matriz")
print()
print(u)
print(iu)
print(uo)
print()
print("diagonales")
print()
print(a,g,m)