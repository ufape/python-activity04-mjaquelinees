def divisao():
    
    x = int(input("Digite o valor 1: "))
    y = int(input("Digite o valor 2: "))

    if x > y:
        x, y = y, x
    numeros = []
    for i in range(x+1, y):
        if i % 5 == 2 or i % 5 == 3:
            numeros.append(i)

    print("Os números são..: {}".format(" ".join(str(n) for n in numeros)))
