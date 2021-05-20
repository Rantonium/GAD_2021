pythonList=[7,8,9,2,3,1,4,10,5,6]
lista1 = list(pythonList)
lista1.sort()
print("Sortare crescatoare: "+str(lista1))
lista2 = list(pythonList)
lista2.sort(reverse=1)
print("Sortare descrescatoare: "+str(lista2))
lista3 = lista1[0:len(lista1):2]
print("Numere impare: "+str(lista3))
print("Numere impare: "+str([pythonList[0],pythonList[2],pythonList[4],pythonList[5],pythonList[8]]))
lista4 = lista1[1:len(lista1):2]
print("Numere pare: "+str(lista4))
print("Numere pare: "+str([pythonList[1],pythonList[3],pythonList[6],pythonList[7],pythonList[9]]))
print("Multipli de 3: "+str([pythonList[2],pythonList[4],pythonList[9]]))

#bonus lambda
print("Sortare crescatoare: "+str(list(sorted(pythonList, key=lambda x: x))))
print("Sortare descrescatoare: "+str(list(sorted(pythonList, key=lambda x: x, reverse=True))))
print("Numere pare: "+str(list(filter(lambda x:x%2==0,pythonList))))
print("Numere impare: "+str(list(filter(lambda x:x%2==1,pythonList))))
print("Multipli de 3: "+str(list(filter(lambda x:x%3==0, pythonList))))
