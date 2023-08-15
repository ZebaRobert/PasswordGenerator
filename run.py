import pickle
import hashlib
import os

FOLDER_PATH = 'users'
user = None

class User : 

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
            print(f"An errorr occured: {e}\n")
    
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
                            print("If you are not able to log in to your account it can be deleted for safety purposes.\n")
                            print("Would you like to try again, delete your account or create a new account?\nagain/delete/new\n")
                            answer =  input("What will it be? :\n").lower()
                            if answer == "delete":
                                file.close()
                                return handle_input(answer)
                            return handle_input(answer)      
                    else:
                        password = input("Incorrect password! Please try again:\n")
                        retry_count -= 1
                return saved_data
        except FileNotFoundError:
             print(f"User under the ({username}) username was not found. Would you like to create a new account or try to login again?.\n")
             response = input("login/new : \n").lower()
             handle_input(response)
        except Exception as e:
            print(f"An errorr occured: {e}\n")

    gen_passwords = {
        "test1" : "test 1-1",
        "test2" : "test 2-2",
        "test3" : "test 3-3"
    }

def handle_input(answer, username = None):
    """
    Function for handling all of the user inputs
    """
    global user
    retry = answer
    while retry != "stop":
        if answer == "login" or answer == "again":
            username = input("Username: \n").lower()
            password = input("Password: \n").lower() 
            user = User.load_from(username, password)
            return user
        elif answer == "create" or answer == "new":
            user = create_user()
            return user
        elif answer == "delete":
            while True:
                try:
                    print("Please confirme the user you want to delete.\n")
                    username = input("Username: \n")
                    if username == "stop":
                        main()
                    file_path = os.path.join(FOLDER_PATH, username) + ".pkl"
                    os.remove(file_path)
                    print("Account has been successfully deleted.\n")
                    main()
                except FileNotFoundError:
                    print("This user doesnt exist. Please try again.\nIf you cant remeber your username, type in 'stop' to go back to the Main Menu.")
                except Exception as e:
                    print(f"An error occured: {e}")
        elif answer == "saved":
            print("Which password would you like to retreve? For which platform?\n")
            print("These are the platforms you have generated a password for : \n")
            for key in user.gen_passwords.keys():
                print(f"{key}")
            platform = input("Your choise: \n")
            print(f"Your password for {platform} is:\n{user.gen_passwords.get(platform)}")
            return
        else:
            print(f"{answer} is not a valid option.\n")           
            print("If you would like to go back to the Main Menu. Type in 'stop'.\n")
            retry = input("Please try again: \n").lower()
    if retry == "stop":
        user = None
        retry = None
        main()


def create_user():
    """ 
    Creates a new instance of the User class 
    """
    global user
    print("Lets get you started!\n")
    while True:
        username = input("How would you like to be called? \n").lower()
        path = os.path.join(FOLDER_PATH, username) + ".pkl"
        if os.path.exists(path):
            print("Sorry username is already taken. Try another one!\n")
            continue
        elif username.strip() == "" or username == None:
            print("Invalid input, please try again.\n")
            continue
        else:
            print("Username accepted.\n")
            break
    while True:
        password = input("Your password: ").lower()
        if password == None or password.strip() == "":
            print("Password cannot be empty or only spaces. Please try again.\n")
        else:
            print("Password accepted.\n")
            break 
    print("Great!\nCreating an account....\n")
    user = User(username, password)
    user.save_to()
    print("Account created!\n")
    return user
    
def main():
    print("\nHello, welcome to Password Generator\n")
    print("If you have an account, please login. Otherwise please create a new account.\n")
    print("create / login\n")
    answer = input("What would you like to do? \n").lower()
    user = handle_input(answer)
    while True:
        print(f"Hello {user.username}.\nWhat would you like to do next?\n")
        print("Avable options: \n1. Display saved password: saved\n2. Generate new password: generate\n3. Exit the program: exit\n4. Return to main menu: main: stop\n")
        answer = input("Keyword : \n")
        if answer == "exit":
            print(f"Goodbye, {user.username}")
            break
        handle_input(answer)
    return

main()

