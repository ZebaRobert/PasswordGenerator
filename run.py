import pickle
import hashlib
import os

FOLDER_PATH = 'users'

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
        except FileExistsError:
             print(f"User already exists under ({self.username}) username. Please try to login\n")
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
                if password == user_password:
                    return saved_data
                else:
                    retry_count = 3
                    while True:
                        retry = input(f"Incorrect password. Please try again:\n")
                        if retry == user_password:
                            return saved_data
                        else:
                            retry_count -= 1
                            if retry_count == 0:
                                print("If you are not able to log in to your account it can be deleted for safety purposes.\n")
                                print("Would you like to try again, delete your account or create a new account?\nagain/delete/new\n")
                                answer =  input("What will it be? :\n")
                                return answer
                            continue        
        except FileNotFoundError:
             print(f"User under the ({username}) username was not found. Please create an account.\n")
             return create_user()
        except Exception as e:
            print(f"An errorr occured: {e}\n")

def handle_input(input, username):
    """
    Function for handling all of the user inputs
    """
    if isinstance(input, User):
        return print("User found!\n")
    elif input == "again":
        password = input("Password:\n")
        user = User.load_from(username, password)
    elif input == "delete":
        file_path = os.path.join(FOLDER_PATH, username) + ".pkl"
        os.remove(file_path)
        print("Account has been successfully deleted.")
        main()
    elif input == "new":
        return create_user()

def create_user():
    """ 
    Creates a new instance of the User class 
    """
    print("Lets get you started!\n")
    username = input("How would you like to be called? \n").lower()
    password = input("Your password : \n").lower()
    print("Great!\nCreating an account....\n")
    new_user = User(username, password)
    new_user.save_to()
    print("Account created!\n")
    return new_user
    
def main():
    print("Hello, welcome to Password Generator\n\n")
    print("If you have an account, please login. Otherwise please create a new account.\n")
    print("create / login\n")
    answer = input("What would you like to do? \n")
    while True:
        if answer == "login":
            username = input("Username: \n").lower()
            password = input("Password: \n").lower()
            user = User.load_from(username, password)
            handle_input(user, username)
            print(f"Welcome {username}!")
            break     
        elif answer == "create":
            new_user = create_user()
            break 
        else:
            print(f"{answer.lower()} is not an option. Please try again.")
            continue
    return

main()


