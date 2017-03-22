def LerLista(num_elementos):
    Lista = []
    for i in range(num_elementos):
        item = int(input("Elemento %d:" % (i+1)))
        Lista.append(item)
    return Lista

def JuntaListas(La, Lb, num_elementos):
    Resultado = []
    for i in range(num_elementos):
        Resultado.append(La[i])
        Resultado.append(Lb[i])
    return Resultado

L1 = LerLista(3)
L2 = LerLista(3)

print(JuntaListas(L1, L2, 3))




    
