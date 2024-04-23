from models.data_source import users
from utils.crud import read_friends, add_user, search_user, remove_user, update_user

if __name__ == '__main__':
    while True:
        print("Welcome to the menu  ")
        print("0. Exit ")
        print("1. Read a list of friends ")
        print("2. Add new user")
        print("3. Search user")
        print("4. Remove user")
        print("5. Update user")
        menu_option = input("Choose an option:")
        if menu_option == "0":
            break
        if menu_option == "1":
            read_friends(users)
        if menu_option == "2":
            add_user(users)
        if menu_option == "3":
            search_user(users)
        if menu_option == "4":
            remove_user(users)
        if menu_option == "5":
            update_user(users)