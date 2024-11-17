# #kolekcje i sterowanie przepływem 
# # Stwórzmy pustą listę
# my_list = []

# # Dodajmy wartości
# my_list.append("Python")
# my_list.append("is ok")
# my_list.append("sometimes")
# # Usuńmy'sometimes'
# my_list.remove("sometimes")
# # Zmieńmy drugi element listy
# my_list[1] = "is neat"
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == ["Python", "is neat"]

# #1.1.2
# original = ["I", "am", "learning", "hacking", "in"]
# # Twoja implementacja
# #sposób1
# modified = original[:]
# modified.append("Python")
# modified[3] = "lists"
# #sposób2
# modified = original.copy()
# #sposób3
# modified = [*original, 'Python']
# modified[3] = 'lists'
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert original == ["I", "am", "learning", "hacking", "in"]
# assert modified == ["I", "am", "learning", "lists", "in", "Python"]

#
# list1 = [6, 12, 5]
# list2 = [6.2, 0, 14, 1]
# list3 = [0.9]
# # implementacja
# combo = [list1, list2, list3]
# my_list = sorted(my_list, reverse=True)
# print(my_list)

# ##INNA 2
#  my_list = list1.copy()
# my_list.extend(list2)
# my_list.extend(list3)

# my_list = sorted(my_list, reverse=True)
# #v3
# my_list=sorted([*list, *list2, *list3], reverse=True)


# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]

# 1.2.1
# first_name = "John"
# last_name = "Doe"
# favorite_hobby = "Python"
# sports_hobby = "gym"
# age = 82
# # Twoja implementacja
# # Twoja implementacja
# my_dict = {
#     "name": f"{first_name} {last_name}", 
#     "age": age, 
#     "hobbies": [favorite_hobby,sports_hobby]}
# print(my_dict)
 
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}

# #Zadanie 1.2.2
# dict1 = dict(key1="This is not that hard", key2="Python is still cool")
# dict2 = {"key1": 123, "special_key": "secret"}
# # Można również zainicjalizować słownik przez wykorzystanie listy krotek
# dict3 = dict([("key2", 456), ("keyX", "X")])
# # Twoja implementacja
# my_dict = {**dict1, **dict2, **dict3}
# #operator '**' który tworzy nowy słownik 
# #key1 i 2 rónią się, bo nadpisano wartość, aktualna jest ta późniejsza
# special_value = my_dict.pop('special_key')

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
# assert special_value == "secret"
# # Sprawdźmy czy słowniki początkowe nie zostały zmienione
# assert dict1 == {"key1": "This is not that hard", "key2": "Python is still cool"}
# # assert dict2 == {"key1": 123, "special_key": "secret"}
# # assert dict3 == {"key2": 456, "keyX": "X"}

#1.3.1
# name = "John Doe"
# if len(name) > 20:
#     print(f'Name "{name}" is more than 20 chars long')
#     length_description = "long"
# elif len(name) > 15:
#     print(f'Name "{name}" is more than 15 chars long')
#     length_description = "semi long"
# elif len(name) > 10:
#     print(f'Name "{name}" is more than 10 chars long')
#     length_description = "semi long"
# elif len(name) in range (8,11):
#     print(f'Name "{name}" is 8, 9 or 10 chars long')
#     length_description = "semi short"
# else:
#     print(f'Name "{name}" is a short name')
#     length_description = "short"
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert length_description == "semi short"

#1.3.2
# words = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
# upper_case_words = []

# for word in words:
#     if word.isupper():
#        upper_case_words .append(word)
    
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert upper_case_words == ["PYTHON", "JOHN", "DOE"]

# #skrocona wersja to: 
#     upper_case_words = [word for word in words if word.isupper()]

# #rozbudowana wersja z if else, która zwraca 1, jesli nie ma duzych
#     upper_case_words = [i if i.isupper() else 1 for i in words]

#1.3.3
# magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)
# # Twoja implementacja

# sum_of_values = 0
# for key in magic_dict.keys():
#     if isinstance(magic_dict[key],(int, float)):
#         sum_of_values += magic_dict[key]
# v2 
# sum_of_values = sum([magic_dict[key] for key in magic_dict.keys() if isinstance(magic_dict[key],(int, float))])
# Sprawdźmy czy otrzymaliśmy 

# # 1.3.4
# numbers = [1, 3, 4, 6, 81, 80, 100, 95]
# # Twoja implementacja
# my_list = []

# for number in numbers: 
#     if numbers % 5 == 0 and numbers % 2 == 1:
#         my_list.append("five odd");
#     elif numbers % 5 == 0 and number % 2 == 0
#       my_list.append("five even")
#     elif number % 2 == 1:
#         my_list.append("odd")
#     elif number % 2 == 0:
#         my_list.append("even")

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == [
#     "odd",
#     "odd",
#     "even",
#     "even",
#     "odd",
#     "five even",
#     "five even",
#     "five odd",
#     ]

# FUNKCJE NA KOLJENYM SPOTKANIU 

# Zadania z 2
#2.1

# System oceniania
# 90-100, 5.0
# 75-89, 4.5
# 65-75, 4.0
# 60-65, 3.5
# 50-57, 3.0
# 0-49, 2.0
# # Przykładowy output
# Liczba punktów: 53
# Uzyskana ocena: 3.5
# Student zaliczył zadanie
#

# ##Czyjeś 
# #słownik z wartościami; w () jest krotka z wartościami punktów 
# score = {
#     (90, 100): 5.0,
#     (75, 89): 4.5,
#     (65, 74): 4.0,
#     (60, 64): 3.5,
#     (50, 59): 3.0,
#     (0, 49): 2.0
# }
 
# punkty = int(input("Podaj liczbę punktów: "))
 
# # skąd tu są te wartości w []? i czym jest dokładnie przedział?
# ocena = None
# for przedzial, ocena_wynik in score.items():
#     if przedzial[0] <= punkty <= przedzial[1]:
#         ocena = ocena_wynik
#         break
 
 
# print(f"Liczba punktów: {punkty}")
# if ocena >= 3.0:
#     print(f"Uzyskana ocena: {ocena}")
#     print("Student zaliczył zadanie")
# else:
#     print(f"Uzyskana ocena: {ocena}")
#     print("Student nie zaliczył zadania")
 
#2.2

    # miesiac = input("Wprowadz miesiąc: ")

    # poryroku = {
    #     "styczeń": "zima",
    #     "luty": "zima",
    #     "marzec": "wiosna",
    #     "kwiecień": "wiosna",
    #     "maj": "wiosna",
    #     "czerwiec": "lato",
    #     "lipiec": "lato",
    #     "sierpień": "lato",
    #     "wrzesień": "jesień",
    #     "październik": "jesień",
    #     "listopad": "jesień",
    #     "grudzień": "zima"
    # }

    # # Przykładowy input
    # # Wprowadź miesiąc: październik

    # print(poryroku[miesiac] if miesiac in poryroku.keys() else "Podano miesiąc poza zakresem")

#INNA WERSJA 
# month = input("Wprowadz miesiąc: ")

# seasons = {
#         ["1", "2", "3", "styczen", "luty", "marzec"]: "zima",
#         ["4", "5", "6", "styczen", "luty", "marzec"]: "wiosna",
#         ["7", "8", "9", "styczen", "luty", "marzec"]: "lato",
#         ["10", "11", "12", "styczen", "luty", "marzec"]: "jesien", 
# }
# seasons = None
# #value = pora roku, key = miesiace
# for key, value in seasons.items():
#     if month in key: 
#         seasons = value 
#         break 

            # print(f"Pora roku dla miesiąca {month}: {season}")


            #             month = input("Wprowadź miesiąc: ")
            # seasons = {
            #     ('1', '2', '3', 'styczeń', 'luty', 'marzec'): "zima",
            #     ('4', '5', '6', 'kwiecień', 'maj', 'czerwiec'): "wiosna",
            #     ('7', '8', '9', 'lipiec', 'sierpień', 'wrzesień'): "lato",
            #     ('10', '11', '12', 'październik', 'listopad', 'grudzień'): "jesień",
            # }
            # # season = None
            # # for key, value in seasons.items():
            # #     if month in key:
            # #         season = value
            # #         break
            
            # season = [value for key, value in seasons.items() if month in key][0]
            
            # print(f'Pora roku dla miesiąca {month}: {season}')
        

# # zadanie 3
# lista = ["tekst", 1, 1.5, True, [0]]

# print(len(lista))
# print(lista[0])
# #jeśli nie znamy długosci, a chcemy elemnt środkowy 
# print(lista[len(lista)//2])
# print(lista[len(lista)-1])
# #alternatywnie print(lista[-1])
# print(lista)
# lista.insert(0, "Pierwszy element")
# lista.append("ostatni element")
# print(lista)

# #2.4 
# list = list(range(1,11))
# print(list)
# list.sort(reverse = True)
# print(list)
# list2 = list[:5]
# print(list)
# list2.remove(list2[len(list2)//2])
# print(list)
# list2.sort()

# element = 8 

# if element in list:
#   print(f'W pierwszej liście występuje element {element}')
 
# if element in list2:
#   print(f'W nowej liście występuje element {element}')
 
# del list
# del list2

# #2.5
# dzialanieuzytkownika = (input("podaj operacje: "))
# informacje = dzialanieuzytkownika.split()

# liczba1 = float(informacje[0])
# liczba2 = float(informacje[2])
# dzialanie = informacje[1]

# wynik = None

# if dzialanie == '+':
#     wynik = liczba1 + liczba2
# elif dzialanie == '-':
#     wynik = liczba1 - liczba2
# elif dzialanie == '*':
#     wynik = liczba1 * liczba2
# elif dzialanie == '/':
#     wynik = liczba1 / liczba2

# #USRPAWNIENIE
# #dzialanienaliczbach = f"{liczba1} {operator} {liczba2}"

# if wynik is not None:
#     print(f" {liczba1} {dzialanie} {liczba2} = {wynik}")

#2.7 -  to jest z list comprehension 
# lista = [-4, -3, -2, -1, 0, 3, 6, 9, 12]
# print({value for value in lista if value > 0})


# lista_krotek = [(x, 1, x, x**2, x**3) for x in range(11)]
# print(lista_krotek)

# lista = [22, 19, 24, 25, 26, 24, 25, 24]
# zbior = set(lista)
# print(len(lista), len(zbior))
# print(lista if len(lista) > len(zbior) else zbior)

#2.10
# liczba = int(input("Podaj liczbę, dla której chcesz wyświetlić tabliczkę mnoenia (1-10): "))

# if 1 <= liczba <= 10: 
#     print(f"Tabliczka mnienia dla {liczba}")
#     for y in range(1,11):
#         wynik = liczba * y
#         print (f"{liczba} x {y} = {wynik}")


# suma_parzyste = 0
# suma_nieparzyste = 0

# for i in range(101):   
#     if i % 2 == 0: 
#         suma_parzyste += i 
#     else:
#         suma_nieparzyste += i 

#         #mona jeszcze tak
#         #suma_parzyste = sum(i for i in range(101) if i % 2 == 0)
#         #suma_nieparzyste = sum(i for i in range(101) if i % 2 == 1)
 

# print(f"suma wszystkich liczb parzystych to: {suma_parzyste}, a liczb to: {suma_nieparzyste}")

#zadani2 2.12
# tekst = "Uczę się Pythona, aby móc tworzyć aplikacje. Dużą zaletą Pythona jest to że jest bardzo zbliżony do języka angielskiego. Posiada prostą składnię, ale czasami potrafi być skomplikowany przez wysoki poziom abstracji. Jednak dobrze jest się nauczyć Pythona, aby dalej rozwijać się w stronę programowania."

# ekst = "Uczę się Pythona, aby móc tworzyć aplikacje. Dużą zaletą Pythona jest to że jest bardzo zbliżony do języka angielskiego. Posiada prostą składnię, ale czasami potrafi być skomplikowany przez wysoki poziom abstracji. Jednak dobrze jest się nauczyć Pythona, aby dalej rozwijać się w stronę programowania."
# zdania = tekst.split('. ')
 
# for zdanie in zdania:
#     print(zdanie)
#     slowa = zdanie.split(' ')
#     print(f'Liczba unikalnych słów: {len(set(slowa))}')
#     print(f'Liczba słów: {len(slowa)}')

# #2.13
# X = [
#     [12,9,3],
#     [4,5,6],
#     [7,8,3]
#     ]

# Y = [  
#     [9,8,1],
#     [6,7,3],
#     [4,5,9]
#     ]

# result = []
# i to indeks wiersza; j to index kolumny 
for i in range(len(X)):
    row = []
for j in range(len(X[i])):
        row.append(X[i][j] + Y[i][j])
    result.append(row)
 
# assert result == [[21, 17, 4], [10, 12, 9], [11, 13, 12]]

X = [[12,9],
    [7 ,3],
    [5 ,6]]

result = [[0, 0, 0],
            [0, 0, 0]]
#Macierz X, wartośc i to 0 dla pierwszego wiersza 

for i in range(len(result)):
    for j in range(len(result[i])):
        print(i,j)
        result[i][j] = X[j][i]


assert result == [[12, 7, 5], [9, 3, 6]]