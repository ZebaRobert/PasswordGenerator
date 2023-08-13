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

    def save_to(self, filename, folder_path):
        """
        Saves an instance of the class inside users folder
        """
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "wb") as file:
                pickle.dump(self, file)
        except FileExistsError:
             print(f"User already exists under ({self.username}) username. Please try to login\n")
        except Exception as e:
            print(f"An errorr occured: {e}\n")
    
    @classmethod
    def load_from(cls, folder_path, username, password):
        """
        Loads an instance of the class user from the users folder
        """
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_path = os.path.join(folder_path, username) + ".pkl"
            with open(file_path, "rb") as file:
                saved_data = pickle.load(file)
                user_password = saved_data.get("password")
                if password == user_password:
                    return saved_data
                else:
                    retry_count = 3
                    while retry_count > 0:
                        retry = input(f"Incorrect password. {retry_count} attempts remaining. Please try again:\n")
                        saved_data = User.load_from(FOLDER_PATH, username, retry)
                        if saved_data is not None:
                            return saved_data
                        retry_count -= 1
                    print("Maximum password attempts made. Please create a new account\n")
                    
        except FileNotFoundError:
             print(f"User under the ({username}) username was not found. Please create an account.\n")
        except Exception as e:
            print(f"An errorr occured: {e}\n")

            
        
