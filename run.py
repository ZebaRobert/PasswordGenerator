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
             print(f"User already exists under ({self.username}) username. Please try to login")
        except Exception as e:
            print(f"An errorr occured: {e}")
            
        
