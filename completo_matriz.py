print("que matriz quieres hallar? A continuacion esta el lista de las opciones, porfavor escrbir el numero  de la opcion ")
print("1.identidad "))
u = []
iu = []
uo = []

opciones = float(input("escribe el numero de la opcion "))
print(f"la opcion que que escojiste es {opciones}")

match opciones:
    case 1:
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
        u.append(0)
        u.append(0)

        iu.append(0)
        iu.append(g)
        iu.append(0)

        uo.append(0)
        uo.append(0)
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
