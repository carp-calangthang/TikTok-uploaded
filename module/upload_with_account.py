from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from colorama import Fore, Style
import threading
import pyautogui
import shutil
import queue
import time
import toml
import sys
import os

class run_with_cookie:
    def __init__(self):
        self.all_cookies_used = False
        self.adminNoiti = Fore.CYAN + "Admin: "
        self.systemNoiti = Fore.GREEN + "System: "
        self.browserNoiti = Fore.MAGENTA + "Browser "
        self.warning = Fore.YELLOW + "Warn: "   
        self.error = Fore.RED + "Error: "
        print(self.adminNoiti + Fore.WHITE + "Enter Video Caption: ")
        self.caption = input()
        
    def check_cookie(self):
        return not self.all_cookies_used