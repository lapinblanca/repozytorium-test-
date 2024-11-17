# x = 10 
# if x > 10: 
#     print("x jest większe od 10")
# elif x == 10:
#     print("x jest równe 10")
# else: 
#     print("x jest mniejsze od 10")

# lista_liczb = [9,6,8,2,5]
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

# lista_tekst = ["a", "b", "c", "d", "e"]

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

# age = input("podaj wiek: ")
# if not age.isdigit():
#     raise ValueError ("wiek nie jest podany jako liczba")

# age = int(age)

# if age < 10: 
#     raise ValueError ("wiek nie moze być ujemny!")
# print("wiek został podany poprawnie")

# #f = open ('file.txt', 'a', encoding ="utf-8")
# with open ('file.txt', 'r', encoding ="utf-8") as plik:
#     #operacje na pliku 
#     plik.write('nowy tekst')

# # import jason 

# # slownik_jason = {
# #     "a": "123",
# #     "b": [1,2,3], 
# }


# komentarze do materiałów // zadania
# 1. funkcja lower 2.TAM JEST BŁąd 3. te jest błąd, powinno być > original.lower()


# ugly = " title of my NeW Book\n\n"
# #implementacja pretty 
# pretty = ugly 
# pretty = ugly.strip().title()
# print(pretty)

# # #sprawdzamy 
# print(pretty)

# verb = 'is'
# language = "Python"
# puncatation = !"
# sentence = f"Learingn{language} {verb} fun{puncatation}"

# print(sentence)

# a = 2
# b = 3 
# c = 2

# result = 6*(a**3) - (8*(b**2))/(4*c) + 11
# assert result = 50

#implementacja 

# total = 45.123
# formatted_total = f"Twój całkowity wynik to {total:.2f}"
# print (formatted_total)

##### kolejny dzień 
#2.1
# Przykładowy input
# x = input("Wprowadź sowje imie: ")
# y = input("wprowadź swoje nazwisko: ")
# print(f'Cześć {y} {x}')

# #2.2
# filename = input("Wprowadź nazwę pliku: ")
# print(filename.split('.'))
# print(filename.split('.')[1])

#2.3
# dd = input('Podaj dzień: ')
# mm = input('Podaj miesiąc: ')
# yyyy = input('Podaj rok: ')
 
# print(f'{dd}/{mm}/{yyyy}')

#2.4 
# x = int(input("podaj liczbe1: "))
# y = int(input("podaj liczbe2: "))
# r = x + y
# print(f'Suma {x} oraz {y} to {r} ')

#2.5
#moje rozwiazanie
    # x1 = int(input("podaj liczbe całkowitą1: "))
    # x2 = int(input("podaj liczbe całkowitą2: "))
    # y = float(input("podaj liczbe zmienna1 : "))
    # y2 = float(input("podaj liczbe zmienna2 : "))
    # wynik1 = x1 + y1
    # wynik2 = y2 - x2
    # print(f"wynik pierwszej operacji{wynik1}"
    # print(type(wynik1))
    # print(f"wynik operacji 2 {wynik2}")
    # print(type(wynik2))
    # suma = wynik1 + wynik2
    # print(f"suma to [suma]")
    # print(type(suma))
##ALBO 
# a = int(input("Wprowadź pierwszą liczbę całkowitą: "))
# b = int(input("Wprowadź drugą liczbę całkowitą: "))
# c = float(input("Wprowadź pierwszą liczbę zmiennoprzecinkową: "))
# d = float(input("Wprowadź drugą liczbę zmiennoprzecinkową: "))
 
# wynik1 = a+c
# wynik2 = d-b
 
# print(f"Wynik operacji 1: {wynik1}")
# print(type(wynik1))
# print(f"Wynik operacji 2: {wynik2}")
# print(type(wynik2))
 
# suma = wynik1 + wynik2
 
# print(f"Suma to: {suma}")
# print(type(suma))

#2.6
# liczba = int(input("wprowadx liczbę "))
# pierwiastek = int(input("wprowadz pierwiastek "))
# wynik = liczba**pierwiastek
# print(f'wynik to {liczba**(1/pierwiastek)}')
# print(f'Pierwiastek stopnia {pierwiastek} z {liczba} to {liczba**(1/pierwiastek)}')

#2.7
# słowo1 = str(input("podaj słowo:"))
# słowo2 = str(input("podaj słowo:"))
 
# print(f'{słowo1} {słowo2}')
# print(słowo1, słowo2, sep=", ")
# print(słowo1, end=" ")
# print(słowo2)

#2.8
# bok1 = int(input("wprowadz bok 1: ")) 
# bok2 = int(input("wprowadz bok 2: ")) 
# bok3 = int(input("wprowadz bok 3: ")) 

# poletrojkata = 1/2*(bok1+bok2+bok3)
# wzorgerona = poletrojkata*(poletrojkata-bok1)*(poletrojkata-bok2)*(poletrojkata-bok3)

# print(f'Pole trojkata wynosi: {poletrojkata}')

# ##czyjeś 

#     a = float(input('Podaj pierwszy bok: '))
#     b = float(input('Podaj drugi bok: '))
#     c = float(input('Podaj trzeci bok: '))
    
#     p = (a + b + c) / 2
    
#     pole = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
#     print(f'Pole trójkąta wynosi: {pole:.2f}')

#2.9 
# km = float(input('Podaj wartość w kilometrach: '))
# mile = 0.621371192 * km
 
# print(f'{km:.2f} kilometra to {mile:.2f} mili')

2.10
Celsjusz = float(input('Podaj wartość w stopniach Celsjusza: '))
Fahrenheit = (Celsjusz*9/5)+ 32
 
print(f'{Celsjusz} Celsjusza to {Fahrenheit} stopni Fahrenheita')
