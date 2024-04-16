def read_friends(users: list)->None:
    print("Informacja o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')

