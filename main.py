import random


def main():
    # Defines
    firstname = "Hello"
    lastname = "World"
    nickname = ["test", "Crusher", "the Scientist", "Twinkle-toes", "the Coder", "the Jester", "the Sloth", "Quick-Silver"]

    # loop
    loop = True
    while loop:
        print(f"MAIN MENU {firstname, lastname}"
              "\n1. Change Name "
              "\n2. Display a Random Nickname "
              "\n3. Display All Nicknames "
              "\n4. Add a Nickname "
              "\n5. Remove a Nickname "
              "\n6. Exit")
        menu_choice = int(input("Select an option(1-6): "))

        # Change Name
        if menu_choice == 1:
            firstname = input("Please enter First name: ")
            lastname = input("Please enter Last name: ")

        # Display a Random Nickname
        elif menu_choice == 2:
            print(f"{firstname} \"{nickname[random.randrange(0,len(nickname))]}\" {lastname} ")

        # Display All Nicknames
        elif menu_choice == 3:
            for i in range(len(nickname)):
                print(f"{firstname} \"{nickname[i]}\" {lastname} ")

        # Add a Nickname
        elif menu_choice == 4:
            add_nickname = input("Please enter the new nickname you want to add:")
            if add_nickname not in nickname:
                nickname.append(add_nickname)
                print("Nickname added to list")
            else:
                print(f"{add_nickname} is already in the list")

        # Remove a Nickname
        elif menu_choice == 5:
            remove_nickname = input("Please enter the nickname you want to remove:")
            if remove_nickname in nickname:
                nickname.remove(remove_nickname)
                print("Nickname removed.")
            else:
                print(f"{remove_nickname} not found.")
        # Exit
        elif menu_choice == 6:
            loop = False


# Call Function
main()



