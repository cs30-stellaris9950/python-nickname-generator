# global Variables
Firstname = ""
Lastname = ""
nickname = ["Crusher", "the Scientist", "Twinkle-toes", "the Coder", "the Jester", "the Sloth", "Quick-Silver"]


def main():
    loop = True
    while loop:
        print(f"MAIN MENU {Firstname, Lastname}"
              "\n1. Change Name "
              "\n2. Display a Random Nickname "
              "\n3. Display All Nicknames "
              "\n4. Add a Nickname "
              "\n5. Remove a Nickname "
              "\n6. Exit")
        menu_choice = int(input("Select an option(1-6): "))

        # Change Name
        if menu_choice == 1:
            Firstname = input("Please enter First name: ")
            Lastname = input("Please enter Last name: ")
        # Display a Random Nickname
        elif menu_choice == 2:
            print("Constructing")
        # Display All Nicknames
        elif menu_choice == 3:
            print("Constructing")
        # Add a Nickname
        elif menu_choice == 4:
            print("Constructing")
        # Remove a Nickname
        elif menu_choice == 5:
            print("Constructing")
        # Exit
        elif menu_choice == 6:
            loop = False


