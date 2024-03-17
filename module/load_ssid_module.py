from colorama import Fore, Style
import os

class load_ssid:
    def __init__(self):
        self.adminNoiti = Fore.CYAN + "Admin: "
        self.systemNoiti = Fore.GREEN + "System: "
        self.browserNoiti = Fore.MAGENTA + "Browser "
        self.warning = Fore.YELLOW + "Warn: "
        self.error = Fore.RED + "Error: "
    
    def getSSid(self):
        
        script_path = os.path.abspath(__file__) 
        src_directory = os.path.dirname(script_path)
        cookiePath = os.path.join(src_directory, '..', 'data', 'ssid.txt')

        with open(cookiePath, "r") as cks:
            cookies = cks.readlines()

        with open(cookiePath, "w") as ck:
            ck.writelines(cookies)

        return cookies