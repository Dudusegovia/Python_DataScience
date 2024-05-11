import numpy as np

andy = np.array([1,2,3,4])
edu=np.array([5,4,3,2])
nomes=['and', 'edu']
corred = [andy,edu]

def kart(tempos, nomes):
    temp_min= np.min(tempos)
    corredor, volta = np.where(tempos == temp_min)
    i = list([corredor])
    nome=nomes[int(i[0][0])]
    
    print(f"A melhor volta foi de {nome}, na volta {volta}")
    somas = [sum(lista) for lista in tempos]
    
    classificação=np.argsort(somas)
    print(f"A classificação é, respectivamente, :")
    for i in classificação:
        print(i+1)
        print(nomes[i])
        print('--')
    medias=np.mean(tempos, axis=1)
    volta_min=np.argmin(medias) + 1
    print(f" A volta mains rápida foi a {volta_min}, com tempo médio de {medias[volta_min-1]}")
    return 

kart(corred, nomes)