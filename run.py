import pickle
import hashlib
import os

class User : 

    def __init__(self, username, password):
        """
        Creates an instance of user class
        """
        self.username = username
        self.password = password
        self.filename = f"{username}.pkl"
