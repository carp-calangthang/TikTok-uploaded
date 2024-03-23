from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from colorama import Fore, Style
from seleniumwire import webdriver
from module.get_videos_module import get_video_files
from gologin import GoLogin
from gologin import getRandomPort
from sys import platform
import random
import time
import toml
import os

class upload_videos:
    def __init__(self):
        self.adminNoiti = Fore.CYAN + "Admin: "
        self.systemNoiti = Fore.GREEN + "System: "
        self.browserNoiti = Fore.MAGENTA + "Browser "
        self.warning = Fore.YELLOW + "Warn: "   
        self.error = Fore.RED + "Error: "
        
        self.gl = GoLogin({
            "token": "",
            "profile_id": "",
            # "port": random_port
        })
        
    def run_upload_videos(self, ssid, caption, wait_time, process_name):
        
        if platform == "linux" or platform == "linux2":
            chrome_driver_path = "./chromedriver"
        elif platform == "darwin":
            chrome_driver_path = "./mac/chromedriver"
        elif platform == "win32":
            chrome_driver_path = "chromedriver.exe"
            
        debugger_address = self.gl.start()
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
            
        video_files = get_video_files()
        print(video_files)
        
        while video_files:
            
            session_id = {'name': 'sessionid', 'value': ssid}
            
            url = "https://www.tiktok.com/login"
            driver.get(url)
            
            try:
                print(ssid)
                driver.add_cookie(session_id)
                driver.refresh()
                time.sleep(2)
                    
                print(self.systemNoiti + Fore.CYAN + f"{process_name}: " + Fore.WHITE + "Waiting for login...")
                print("--------------------------------------------------------------------------------")
                print(Style.RESET_ALL)
                
            except:
                print(self.error + Fore.YELLOW + "Session Id Error!")
                print(Style.RESET_ALL)
                
            video = video_files.pop(0)
            
            script_path = os.path.abspath(__file__) 
            src_directory = os.path.dirname(script_path)
            config_path = os.path.join(src_directory, '..', 'config', 'config.toml')
            videos_path = os.path.join(src_directory, '..', 'videos')
            
            with open(config_path, 'r') as config_file:
                config = toml.load(config_file)
                
            driver.get("https://www.tiktok.com/creator-center/upload?from=upload&lang=en")
            time.sleep(2)
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            print(self.systemNoiti + Fore.CYAN + f"{process_name}" + Fore.WHITE +  "Start Upload Video!")
            
            iframe_selector = EC.presence_of_element_located(
                (By.XPATH, config['selectors']['upload']['iframe'])
            )
            iframe = WebDriverWait(driver, config['explicit_wait']).until(iframe_selector)
            driver.switch_to.frame(iframe)
            
            wait = WebDriverWait(driver, 10)
            
            time.sleep(3)
            
            upload_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, config['selectors']['upload']['upload_video']))
            )
            upload_box.send_keys(videos_path + "\\" + video)
            print(f"{self.systemNoiti}" + Fore.CYAN + f"{process_name}: Upload: {video}")
            print("--------------------------------------------------------------------------------")
            print(Style.RESET_ALL)
            time.sleep(random.randint(3, 5))
            
            upload_progress = EC.presence_of_element_located(
                (By.XPATH, config['selectors']['upload']['upload_in_progress'])
            )
            upload_confirmation = EC.presence_of_element_located(
                (By.XPATH, config['selectors']['upload']['upload_confirmation'])
            )
            WebDriverWait(driver, config['explicit_wait']).until(upload_confirmation)
            
            process_confirmation = EC.presence_of_element_located((By.XPATH, config['selectors']['upload']['process_confirmation']))
            WebDriverWait(driver, config['explicit_wait']).until(process_confirmation)  
            
            try:
                desc = wait.until(EC.presence_of_element_located((By.XPATH, config['selectors']['upload']['description'])))
                desc.clear()
                desc.send_keys(caption)
                print(self.systemNoiti + Fore.CYAN + f"Description: {caption}")
                print("--------------------------------------------------------------------------------")
            except:
                continue
            
            time.sleep(random.randint(3, 5))       
                
            try:
                time.sleep(random.randint(3, 10))  
                post = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, config['selectors']['upload']['post'])))
                post.send_keys(Keys.END)
                post.click()
                print(self.systemNoiti + Fore.CYAN + f"{process_name}" + Fore.WHITE + "The video is being uploaded. Please wait!")
                print("--------------------------------------------------------------------------------")
                print(Style.RESET_ALL)
                post_confirmation = EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[4]/div/div/div[1]")
                    )
                WebDriverWait(driver, 60).until(post_confirmation)
            except:
                time.sleep(random.randint(3, 10))  
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.execute_script('document.querySelector(".btn-post > button").click()')
                print(self.systemNoiti + Fore.CYAN + f"{process_name}" + Fore.WHITE + "The video is currently being uploaded. Please wait!")
                print("--------------------------------------------------------------------------------")
                print(Style.RESET_ALL)
                post_confirmation = EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[4]/div/div/div[1]")
                    )
                WebDriverWait(driver, 60).until(post_confirmation)
                
            time.sleep(random.randint(3, 5))
            print(self.systemNoiti + Fore.CYAN + f"{process_name}" + Fore.WHITE + f"The video has been posted: {video}")
            print("--------------------------------------------------------------------------------")
            print(Style.RESET_ALL)
            
            try:
                minute_time = wait_time * 60
                print("--------------------------------------------------------------------------------")
                print(self.systemNoiti + Fore.CYAN + f"{process_name}" + Fore.WHITE + f"Please wait for {minute_time} seconds before continuing...")
                print(Style.RESET_ALL)
            except:
                wait_time_int = int(wait_time)
                minute_time = wait_time_int * 60
                print("--------------------------------------------------------------------------------")
                print(self.systemNoiti + Fore.CYAN + f"{process_name}" + Fore.WHITE + f"Please wait for {wait_time_int} seconds before continuing...")
                print(Style.RESET_ALL)
                
            print(Style.RESET_ALL)
            time.sleep(random.randint(3, 5))
            time.sleep(minute_time)
            
            if not video_files:
                print(self.systemNoiti + Fore.CYAN + f"{process_name}" + Fore.WHITE + "All videos have been uploaded!")
                print("--------------------------------------------------------------------------------")
                print(Style.RESET_ALL)
                break