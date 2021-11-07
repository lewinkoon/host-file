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
            print(*list_sites(), sep="\n")
            break

        elif choice == "2":
            add_site()
            break

        elif choice == "3":
            remove_site()
            break

        elif choice == "0":
            print("\nQuitting the program...\n")
            quit()

        print("\nPlease enter a valid number.\n")


def read_file():
    with open("hosts", "r") as file:
        raw = file.readlines()
    return raw


def list_sites():
    sites = [x.rstrip('\n').split(" ")[1] for x in read_file()[::2]]
    return sites


def check_site(site):
    if re.match('[a-zA-Z0-9]{1,256}\.[a-z]{1,6}$', site):
        if site in list_sites():
            return True
        else:
            return False


def add_site():
    while True:
        inp = input("\nPlease, type the site addresss you want to block: ")
        if check_site(inp) == False:
            break
        elif check_site(inp) == True:
            print("\nSite is already in host file.")
            continue
        print("\nInvalid format.")

    with open("hosts", "a") as file:
        file.write("\n0.0.0.0 " + inp)
        file.write("\n0.0.0.0 www." + inp)
    print("\nAdded " + color.RED + inp +
          color.END + " to host file.\n")


def remove_site():
    while True:
        inp = input("\nPlease, type the site addresss you want to remove: ")
        if check_site(inp) == True:
            break
        elif check_site(inp) == False:
            print("\nSite is not in host file.")
            continue
        print("\nInvalid format.")

    raw = read_file()

    with open("hosts", "w") as file:
        for line in raw:
            if inp not in line:
                print(repr(line))
                file.write(line)
        file.truncate(file.tell()-2)
    print("\nRemoved " + color.RED + inp +
          color.END + " from host file.\n")


# print(read_file())
main()
