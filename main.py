# Tomasz Nowak
# 13 APR 2021

# Creating main menu as a constant
MAIN_MENU = "Running Contest \n=========================== \n1. Show the results for a race" \
            + "\n2. Add results for a race \n3. Show all competitors by county \n4. Show the winner of each race" \
            + "\n5. Show all the race times for one competitor \n6. Show all competitors who have won a race" \
            + "\n7. Quit"


def reading_runners():
    with open("Runners.txt") as file_runners:
        lines_runners = file_runners.readlines()
        runners = []
        ids = []
        for line in lines_runners:
            split_line_runners = line.split(",")
            name = split_line_runners[0]
            id_runner = split_line_runners[1].strip()
            ids.append(id_runner)
            runners.append(name)
        return runners, ids


def display(items):
    for item in range(len(items)):
        print(f"{item+1}. {items[item]}")


def reading_races():
    with open("Races.txt") as file:
        lines = file.readlines()
        return [race.strip() for race in lines]


def race_details(race_name):
    with open(f"{race_name}.txt") as file_races:
        lines_race_details = file_races.readlines()
        ids_race = []
        time_race = []
        for lin in lines_race_details:
            split_line_race = lin.split(",")
            code = split_line_race[0]
            time = int(split_line_race[1])
            ids_race.append(code)
            time_race.append(time)
        return ids_race, time_race

8
def main():
    print(MAIN_MENU)
    try:
        choice_main = int(input("==>"))
        while True:
            runner_name, runner_id = reading_runners()
            races = reading_races()
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
