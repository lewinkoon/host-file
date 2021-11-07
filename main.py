import re
# import time


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # Menu
    choice = '0'
    print(color.PURPLE + "\nWelcome to HF manager!\n" + color.END)
    print("Please enter a number for what you want to do.\n")
    print("1. Read the hosts file")
    print("2. Add new blocked site")
    print("3. Remove blocked site")
    print("0. Exit\n")

    while True:

        choice = input("What would you like to do?: ")

        # Declare variable lines
        sites = []

        if choice == "1":
            print("\nHere is the list of blocked sites\n")
            print(*read_file(), sep="\n")
            break

        elif choice == "2":
            add_site()
            break

        elif choice == "3":
            input("\nType the blocked site address you want to remove: ")

        elif choice == "0":
            print("\nQuitting the program...\n")
            quit()

        print("\nPlease enter a valid number.\n")


def add_site():
    while True:
        inp = input("\nPlease, type the site addresss you want to block: ")
        if re.match('[a-zA-Z0-9]{1,256}\.[a-z]{1,6}$', inp):
            if not check_site(inp):
                with open("hosts", "a") as file:
                    file.write("\n0.0.0.0 " + inp)
                    file.write("\n0.0.0.0 www." + inp)
                print("\nAdded " + color.RED + inp +
                      color.END + " to host file.\n")
                break
        print('\nError, please enter again: ')


def read_file():
    with open("hosts", "r") as file:
        raw = file.readlines()
    sites = [x.rstrip('\n').split(" ")[1] for x in raw[::2]]
    return sites


def check_site(site):
    if site in read_file():
        return True
    else:
        return False


main()
