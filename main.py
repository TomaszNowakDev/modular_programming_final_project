# Tomasz Nowak
# 13 APR 2021

# Creating main menu as a constant
MAIN_MENU = "Running Contest \n=========================== \n1. Show the results for a race" \
            + "\n2. Add results for a race \n3. Show all competitors by county \n4. Show the winner of each race" \
            + "\n5. Show all the race times for one competitor \n6. Show all competitors who have won a race" \
            + "\n7. Quit"


def main():
    print(MAIN_MENU)
    try:
        choice_main = int(input("==>"))
        while True:
            if choice_main == 1:
                print("(1) Show the results for a race \n===============================")
            elif choice_main == 2:
                print("(2) Add results for a race \n===============================")
            elif choice_main == 3:
                print("(3) Show all competitors by county \n===============================")
            elif choice_main == 4:
                print("(4) Show the winner of each race \n===============================")
            elif choice_main == 5:
                print("(5) Show all the race times for one competitor \n===============================")
            elif choice_main == 6:
                print("(6) Show all competitors who have won a race \n===============================")
            elif choice_main == 7:
                print("Thank you, Goodbye.")
                break
            else:
                print("Choose one of the options from 1 to 7.")
            print(MAIN_MENU)
            choice_main = int(input("==>"))
    except ValueError:
        print("Please choose one of the options from main menu.")


if __name__ == '__main__':
    main()
