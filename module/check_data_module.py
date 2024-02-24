import os

class check_cookies:
    
    def __init__(self):
        self.script_path = os.path.abspath(__file__) 
        self.src_directory = os.path.dirname(self.script_path)
        self.cookie_path = os.path.join(self.src_directory, '..', 'data', 'cookies.txt')
    
    def check_null_cookies(self):

        with open(self.cookie_path, "r") as cks:
            cookies = cks.readlines()

        return bool(cookies)

    def check_len_cookies(self, len_cookies):

        with open(self.cookie_path, "r") as cks:
            cookies = cks.readlines()

        if len(cookies) >= len_cookies:
            return True
        else:
            return False