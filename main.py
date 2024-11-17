# x = 10 
# if x > 10: 
#     print("x jest większe od 10")
# elif x == 10:
#     print("x jest równe 10")
# else: 
#     print("x jest mniejsze od 10")

lista_liczb = [9,6,8,2,5]
# print(lista_liczb[-2])

#Przykład tworzenia listy za pomocą range 
# my_list = list(range(5))
# print(my_list)
# for i in range(len(lista_liczb)):
#     print(i, lista_liczb[i])

# for i in lista_liczb:
#     print(i)

# for iterator, value in enumerate(lista_liczb):
#     print(iterator, value)
#     #oba 21 i 24 są takie same, zwracają to samo
# for i in range (len (lista_liczb)):
#     print(i, lista_liczb[i])

lista_tekst = ["a", "b", "c", "d", "e"]

# for value1, value2 in zip(lista_liczb, lista_tekst):
#     print(value1, value2)

# for i in range(len(lista_liczb)):
#     print(lista_liczb[1], lista_tekst[i])

# for iterator, value in enumerate(lista_liczb):
#     print(iterator, value)

# print(lista_tekst)
# lista_tekst.append('f')
# print(lista_tekst)
# lista_tekst.extend(['g','h', 'i'])
# print(lista_tekst)

# lista_tekst.insert(1, "ą")
# print(lista_tekst)

# lista_tekst.remove('ą')
# print(lista_tekst)

# a = lista_tekst.pop()
# print(a)

# lista_liczb.sort
# print(lista_liczb)

# krotka_liczba = (5,4,6,7,0)
# print(krotka_liczba)

# slownik = {
#     '0': 'A',
#     1: 'B'
#     10: 'C'
# }

# print(slownik['A'])
# print(slownik.keys())

# # print(slownik['0'])
# # print(slownik.get('0'))
# a = slownik.pop('0')
# print(a)
# print(slownik)

# zbior = {1,2,3,}
# zbior.add(5)
# print(zbior)

# element = zbior.pop(element)
# print(element)

# zbior1 = [1,2,3,4,5]
# zbior2 = {4,5,6,7,8}

# wynik_union = zbior1.union(zbior2)
# print(wynik_union)

# try:    
#     number = (0)
#     result= 10 / number 
#     print(f"wynik:{result}")
# except ZeroDivisionError as e:
#     print("wystąpił błąd dzielenia przez 0")
#     print(e)
# except:
#     print("wystąpił bład")
# finally:
#     print('funkcja finally')

age = input("podaj wiek: ")
if not age.isdigit():
    raise ValueError ("wiek nie jest podany jako liczba")

age = int(age)

if age < 10: 
    raise ValueError ("wiek nie moze być ujemny!")
print("wiek został podany poprawnie")
