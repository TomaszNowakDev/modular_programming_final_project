# Tomasz Nowak
# 13 APR 2021

# Creating main menu as a constant
MAIN_MENU = "Running Contest \n=========================== \n1. Show the results for a race" \
            + "\n2. Add results for a race \n3. Show all competitors by county \n4. Show the winner of each race" \
            + "\n5. Show all the race times for one competitor \n6. Show all competitors who have won a race" \
            + "\n7. Quit\n==>"


def display(items):
    for item in range(len(items)):
        print(f"{item+1}. {items[item]}")


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


def validation_for_choice(rac, prompt):
    display(rac)
    while True:
        try:
            cho = int(input(prompt))
            if 0 < cho <= len(rac):
                break
            else:
                print("Choose one of the options please.")
        except ValueError:
            print("Numbers only please!")
    return cho


def validation_for_menu(prompt):
    while True:
        try:
            cho = int(input(prompt))
            if 0 < cho <= 7:
                break
            else:
                print("Choose one of the options from 1 to 7.")
        except ValueError:
            print("Numbers only please!")
    return cho


def display_option1(codes, time1):
    for item in range(len(codes)):
        t = time_formatted(time1[item])
        print(f"{item + 1}. {codes[item]}{t}")


def time_formatted(t):
    minutes = t // 60
    seconds = t % 60
    tf = f"{minutes:>5} min {seconds:>2} sec"
    return tf


def main():
    choice_main = validation_for_menu(MAIN_MENU)
    while True:
        runner_name, runner_id = reading_runners()
        races = reading_races()

        if choice_main == 1:
            print("(1) Show the results for a race \n===============================")
            choice1 = validation_for_choice(races, "Choice ==> ")
            c, t = race_details(races[choice1 - 1])
            print(f"Results for {races[choice1 - 1]}\n=======================")
            display_option1(c, t)
            print()
            fastest = min(t)
            for index in range(len(t)):
                if t[index] == fastest:
                    print(f"{c[index]} won the race.")

        elif choice_main == 2:
            print("(2) Add results for a race \n===============================")
            new_race = input("Name of new race location ==> ").capitalize()
            while True:
                if new_race not in races:
                    with open("Races.txt", "a") as file_option2:
                        print(new_race, file=file_option2)
                    with open(new_race.lower() + ".txt", "w") as file_race:
                        for i in range(len(runner_id)):
                            time_from_race = int(input(f"What time {runner_id[i]} got? ==>"))
                            if time_from_race > 0:
                                print(f"{runner_id[i]},{time_from_race}", file=file_race)
                        break
                else:
                    print(f"data for {new_race} already exists, please enter a different name.")
                    new_race = input("Name of new race location ==> ").capitalize()

        elif choice_main == 3:
            print("(3) Show all competitors by county \n===============================")
            print("Cork runners \n---------------------")
            for i in range(len(runner_id)):
                if runner_id[i].startswith("CK"):
                    print(f"\t{runner_name[i]:15}{runner_id[i]}")
            print("Kerry runners \n---------------------")
            for i in range(len(runner_id)):
                if runner_id[i].startswith("KY"):
                    print(f"\t{runner_name[i]:15}{runner_id[i]}")

        elif choice_main == 4:
            print("(4) Show the winner of each race \n===============================")
            print(f"{'Venue':16}{'Winner'}\n======================")
            for i in range(len(races)):
                c, t = race_details(races[i])
                fastest = min(t)
                for index in range(len(t)):
                    if t[index] == fastest:
                        print(f"{races[i]:15} {c[index]}")

        elif choice_main == 5:
            print("(5) Show all the race times for one competitor \n===============================")
            which_runner = validation_for_choice(runner_name, "Which runner ==> ")
            runner_to_display = runner_id[which_runner - 1]
            print(f"{runner_name[which_runner - 1]:11}({runner_id[which_runner - 1]})")
            print("------------------------------")
            for i in range(len(races)):
                code, time_in = race_details(races[i])
                if runner_to_display in code:
                    y = code.index(runner_to_display)
                    copied_times = time_in.copy()
                    copied_times.sort()
                    place = copied_times.index(time_in[y])
                    print(f"{races[i]:12}{time_formatted(time_in[y])} ({place +1} of {len(code)})")

        elif choice_main == 6:
            print("(6) Show all competitors who have won a race \n===============================")
            print("The following runners have all won at least one race:")
            print('-----------------------------------------------------')
            winners_list = []
            for i in range(len(races)):
                c, t = race_details(races[i])
                fastest = min(t)
                for index in range(len(t)):
                    if t[index] == fastest and c[index] not in winners_list:
                        winners_index = runner_id.index(c[index])
                        print(f"\t{runner_name[winners_index]} ({c[index]})")
                        winners_list.append(f"{c[index]}")

        elif choice_main == 7:
            print("Thank you, Goodbye.")
            break
        choice_main = validation_for_menu(MAIN_MENU)


if __name__ == '__main__':
    main()
