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

    while choice == '0':

        choice = input("What would you like to do?: ")

        # Declare variable lines
        sites = []

        if choice == "1":
            with open("hosts", "r") as file:
                raw = file.readlines()
            print("\nHere is the list of blocked sites\n")
            for i, str in enumerate(raw[::2]):
                web = re.split(r'\t+', str.rstrip('\n'))[1]
                sites.append(web)
                print(i, '\t' + web)
        elif choice == "2":
            add_site()
        elif choice == "3":
            print("\nType the blocked site address you want to remove\n")
        elif choice == "0":
            print("\nQuitting the program...\n")
            quit()
        else:
            print("\nPlease enter a valid number.\n")
            choice = '0'


def add_site():
    while True:
        inp = input("\nPlease, type the site addresss you want to block: ")
        if re.match('[a-zA-Z0-9]{1,256}\.[a-z]{1,6}$', inp):
            return inp
        print('\nInvalid format, please enter again: ')


# # Execution time measurement
# start_time = time.time()
main()
# print("--- %s seconds ---" % (time.time() - start_time))
