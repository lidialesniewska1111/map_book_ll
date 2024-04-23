def read_friends(users: list)->None:
    print("Informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')

def add_user(lista: list) -> None:
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_postow = int(input("Podaj liczbę postów użytkownika: "))
    nazwa_miejscowości = input("Podaj nazwę miejscowości: ")
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow, 'location': nazwa_miejscowości }
    lista.append(new_user)

def search_user(users: list)->dict:
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            print(user)
            return user
def remove_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            users.remove(user)

def update_user(users: list):
    imie = input("Wprowadź imię użytkownika, którego dane chcesz zmienić: ")
    for user in users:
        if user["name"] == imie:
            user["name"] = input("Podaj nowe imię: ")
            user["surname"] = input("Podaj nowe nazwisko: ")
            user["posts"] = int(input("Podaj nową liczbę postów: "))