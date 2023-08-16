import pickle
import hashlib
import os
import string
import random
import sys

FOLDER_PATH = "users"
user = None


class User:
    def __init__(self, username, password):
        """
        Creates an instance of user class
        """
        self.username = username
        self.password = password
        self.filename = f"{username}.pkl"

    def save_to(self):
        """
        Saves an instance of the class inside users folder
        """
        try:
            if not os.path.exists(FOLDER_PATH):
                os.makedirs(FOLDER_PATH)
            file_path = os.path.join(FOLDER_PATH, self.filename)
            with open(file_path, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"\nAn errorr occured: {e}\n")

    @classmethod
    def load_from(cls, username, password):
        """
        Loads an instance of the class user from the users folder
        """
        try:
            if not os.path.exists(FOLDER_PATH):
                os.makedirs(FOLDER_PATH)
            file_path = os.path.join(FOLDER_PATH, username) + ".pkl"
            with open(file_path, "rb") as file:
                saved_data = pickle.load(file)
                user_password = saved_data.password
                retry_count = 2
                while password != user_password:
                    if retry_count == 0:
                        print(
                            "\nIf you are not able to log in to your account it can be deleted for safety purposes.\n"
                        )
                        print(
                            "Would you like to try again, delete your account or create a new account?\nagain/delete/new\n"
                        )
                        answer = input("What will it be? :\n").lower()
                        if answer == "delete":
                            file.close()
                        return handle_input(answer)
                    else:
                        password = input("Incorrect password! Please try again:\n")
                        retry_count -= 1
                file.close()
            return saved_data
        except FileNotFoundError:
            print(
                f"\nUser under the ({username}) username was not found. Would you like to create a new account or try to login again?.\n"
            )
            response = input("login/new : \n").lower()
            handle_input(response)
        except Exception as e:
            print(f"\nAn errorr occured: {e}\n")

    gen_passwords = {}


def handle_input(answer,stage = 0 , username=None):
    """
    Function for handling all of the user inputs
    """
    global user
    retry = answer
    if stage == 0:
        while retry != "exit":
            if answer == "login":
                username = input("Username: \n").lower()
                password = input("Password: \n").lower()
                user = User.load_from(username, password)
                return user
            elif answer == "create":
                user = create_user()
                return user 
            else:  
                print(f"\n{answer} is not a valid option.\n")
                retry = input("Please try again: \n").lower()
        raise SystemExit        
    elif stage == 1:
        if answer == "delete":
            while True:
                try:
                    print("\nPlease confirme the user you want to delete.\n")
                    username = input("Username: \n")
                    retry = username
                    if retry == "exit":
                        break
                    file_path = os.path.join(FOLDER_PATH, username) + ".pkl"
                    os.remove(file_path)                        
                    print("Account has been successfully deleted.\n")
                except FileNotFoundError:
                    print(
                        "\nThis user doesnt exist.\nIf you cant remeber your username, type in 'stop' to go back to the Main Menu or 'exit' to close the program."
                    )
                except Exception as e:
                    print(f"\nAn error occured: {e}")
                    return
            if username == "exit":
                raise SystemExit
            display_main_menu()
        elif answer == "new":
            user = create_user()
            return user
        else:  
            print(f"\n{answer} is not a valid option.\n")
            print("If you would like to go back to the Main Menu. Type in 'stop'.\n")
            retry = input("Please try again: \n").lower()   
    elif stage == 2:
        if answer == "saved":
            if len(user.gen_passwords) == 0:
                print("\nNo saved passwords found. Lets change that!\n")
                new_entry = generate_password()
                print("\nUpdating data base...\n")
                user.gen_passwords.update(new_entry)
                print("Data base updated successfully!\n")
                return
            else:
                print(
                    "\nWhich password would you like to retreve? For which platform?\n"
                )
                print("These are the platforms you have generated a password for : \n")
                for key in user.gen_passwords.keys():
                    print(f"{key}")
                platform = input("Your choise: \n")
                print(
                    f"\nYour password for {platform} is:\n{user.gen_passwords.get(platform)}\n"
                )
                return
        elif answer == "generate":
            new_entry = generate_password()
            print("\nUpdating data base...\n")
            user.gen_passwords.update(new_entry)
            print("Data base updated successfully!\n")
            return
        elif answer == "exit":
            raise SystemExit
        elif answer == "stop":
            display_main_menu()


def display_main_menu():
    print("\nHello, welcome to Password Generator\n")
    print(
        "If you have an account, please login. Otherwise please create a new account.\n"
    )
    print("create / login\n")
    answer = input("What would you like to do? \n").lower()
    user = handle_input(answer)
    return user

def create_user():
    """
    Creates a new instance of the User class
    """
    global user
    print("\nLets get you started!\n")
    while True:
        username = input("How would you like to be called? \n").lower()
        path = os.path.join(FOLDER_PATH, username) + ".pkl"
        if os.path.exists(path):
            print("Sorry username is already taken. Try another one!\n")
            continue
        elif username.strip() == "" or username is None:
            print("Invalid input, please try again.\n")
            continue
        else:
            print("Username accepted.\n")
            break
    while True:
        password = input("Your password:\n ").lower()
        if password is None or password.strip() == "":
            print("Password cannot be empty or only spaces. Please try again.\n")
        else:
            print("Password accepted.\n")
            break
    print("Great!\nCreating an account....\n")
    user = User(username, password)
    user.save_to()
    print("Account created!\n")
    return user


def generate_password():
    """
    Requesting instructions for configuring a password, generate a new password and store it within a class instance.
    """
    print("\nFor which platform would you like to generate a new password?\n")
    while True:
        new_platform = input("Platform: \n").lower()

        if new_platform.isalpha():
            break
        elif not new_platform.strip():
            print("Input cannot be empty. Please enter some text.")
        else:
            print("Invalid input. Please enter alphabetic characters.")

    print("How strong do you want your password to be?\n")
    print("weak/mediocre/strong\n")
    while True:
        pass_strength = input("Strength: \n").lower()

        if (
            pass_strength == "weak"
            or pass_strength == "mediocre"
            or pass_strength == "strong"
        ):
            break
        else:
            print("Invalid input. Please try again.")

    print("How long would you like your new password to be?\n")
    print("0 - 30\n")

    while True:
        pass_length = input("Lenght: \n")

        if pass_length.isdigit() and int(pass_length) >= 0 and int(pass_length) <= 30:
            number = int(pass_length)
            break
        else:
            print("Invalid input. Please enter a valid number.\n")

    print("Generating password..\n")

    if pass_strength == "weak":
        characters = string.ascii_letters
    elif pass_strength == "mediocre":
        characters = string.ascii_letters + string.digits
    elif pass_strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation

    new_password = "".join(random.choice(characters) for _ in range(number))

    print("Password generated successfully!\n")

    new_entry = {new_platform: new_password}

    return new_entry


def main():
    """
    Runs the main loop of the program
    """
    user = display_main_menu()
    while True:
        print(f"Hello {user.username}.\nWhat would you like to do next?\n")
        print(
            """Avaiable options:
            1. Display saved password: saved
            2. Generate new password: generate
            3. Exit the program: exit
            4. Return to main menu: main: stop\n"""
        )
        answer = input("Keyword : \n")
        if answer == "exit":
            print(f"Goodbye, {user.username}")
            break
        handle_input(answer)
    return


main()
