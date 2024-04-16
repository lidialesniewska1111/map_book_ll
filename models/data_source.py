users: list = [

    {"name": "Julia", "surname": "Gotowiec", "posts": 1500, },
    {"name": "Hubert", "surname": "Sybilski", "posts": 123456, },
    {"name": "Adrian", "surname": "Dobrzański", "posts": 3, },
    {"name": "Bartek", "surname": "Wyrzykowski", "posts": 666, }
]
def search_user(users: list):
    imie = input("Podaj imie: ")
    for user in users:
        if user["name"] == imie:
            print(user)
