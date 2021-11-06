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
    while choice == '0':
        print(color.PURPLE + "\nWelcome to HF manager!\n" + color.END)
        print("Please enter a number for what you want to do.\n")
        print("1. Read the hosts file")
        print("2. Remove blocked site")
        print("3. Add new blocked site")
        print("0. Exit\n")

        choice = input("What would you like to do?: ")

        # Declare variable lines
        sites = []
        with open("hosts", "r") as file:
            raw = file.readlines()

        if choice == "0":
            print("\nQuitting the program...\n")
            quit()
        elif choice == "3":
            print("\nType the site addresss you want to block.\n")
        elif choice == "2":
            print("\nType the blocked site address you want to remove\n")
        elif choice == "1":
            print("\nHere is the list of blocked sites\n")
            for i, str in enumerate(raw[::2]):
                web = re.split(r'\t+', str.rstrip('\n'))[1]
                sites.append(web)
                print(i, web)
        else:
            print("Please enter a valid number.")


# # Execution time measurement
# start_time = time.time()
main()
# print("--- %s seconds ---" % (time.time() - start_time))
