from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from seleniumwire import webdriver
from module.get_videos_module import get_video_files
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
        
    def run_upload_videos(self, cookies, caption, wait_time, proxy, browser_name):
        
        options = webdriver.FirefoxOptions()
        
        seleniumwire_options = {
            'proxy': {
                'http': f'http://{proxy}',
                'verify_ssl': False,
            }
        }
        
        options.add_argument('--headless')
        options.add_argument('--lang=en')
        driver = webdriver.Firefox(options=options) #seleniumwire_options=seleniumwire_options
            
        video_files = get_video_files()
        
        url = "https://www.tiktok.com/login"
        driver.get(url)
        driver.refresh()
        
        while video_files:
            
            url = "https://www.tiktok.com/login"
            driver.get(url)
            driver.refresh()
            
            try:
                cookie_pairs = cookies.split("; ")
                for cookie in cookie_pairs:
                    key, value = cookie.split("=", 1)
                    driver.add_cookie({"name": key, "value": value, "domain": "tiktok.com"})
                    
                print(self.systemNoiti + Fore.CYAN + f"{browser_name}: " + Fore.WHITE + "Đợi đăng nhập...")
                print("--------------------------------------------------------------------------------")
                print(Style.RESET_ALL)
                
            except:
                print(self.error + Fore.YELLOW + "Lỗi cookie!")
                print(Style.RESET_ALL)
                
            video = video_files.pop(0)
            
            script_path = os.path.abspath(__file__) 
            src_directory = os.path.dirname(script_path)
            config_path = os.path.join(src_directory, '..', 'config', 'config.toml')
            videos_path = os.path.join(src_directory, '..', 'videos')
            
            with open(config_path, 'r') as config_file:
                config = toml.load(config_file)
                
            driver.get("https://www.tiktok.com/creator-center/upload?from=upload&lang=en")
            driver.refresh()
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            print(self.systemNoiti + Fore.CYAN + f"{browser_name}" + Fore.WHITE +  "Bắt đầu đăng video!")
        
            time.sleep(5)
            
            iframe_selector = EC.presence_of_element_located(
                (By.XPATH, config['selectors']['upload']['iframe'])
            )
            iframe = WebDriverWait(driver, config['explicit_wait']).until(iframe_selector)
            driver.switch_to.frame(iframe)
                
            MAX_RETRY = 3

            for retry_count in range(MAX_RETRY):
                try:
                    CookieErrorPoint = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/h1')))
                    print("--------------------------------------------------------------------------------")
                    break
                except:
                    with open('./cookie_block.txt', "w") as ck:
                        ck.writelines(cookies)
                    print(self.error + Fore.YELLOW + f"{browser_name}" + Fore.WHITE + "Tài khoản bị khoá chức năng đăng bài!")
                    print("--------------------------------------------------------------------------------")
                    if retry_count == MAX_RETRY - 1:
                        print(f"Reached maximum retry count ({MAX_RETRY}). Exiting.")
                        return
                    print(f"Retrying... (Attempt {retry_count + 1})")
                    
            if not video_files:
                print(self.systemNoiti + Fore.CYAN + f"{browser_name}" + Fore.WHITE + "Đã hết video. Thoát chương trình!")
                print(Style.RESET_ALL)
                break
            
            wait = WebDriverWait(driver, 10)
            time.sleep(3)

            try:
                desc = wait.until(EC.presence_of_element_located((By.XPATH, config['selectors']['upload']['description'])))
                desc.send_keys(caption)
                print(self.systemNoiti + Fore.CYAN + f"Description: {caption}")
                print("--------------------------------------------------------------------------------")
            except:
                continue

            upload_box = driver.find_element(By.XPATH, config['selectors']['upload']['upload_video'])
            upload_box.send_keys(videos_path + "\\" + video)
            print(f"{self.systemNoiti}" + Fore.CYAN + f"{browser_name}: Đăng video: {video}")
            print("--------------------------------------------------------------------------------")
            print(Style.RESET_ALL)
            
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
                move_out_elm = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//span[text()="Chú thích"]'))
                )
                move_out_elm.click()
            except:
                move_out_elm_eng = WebDriverWait(driver, 10).until(   
                    EC.presence_of_element_located((By.XPATH, '//span[text()="Caption"]'))
                )
                move_out_elm_eng.click(move_out_elm_eng)
            
            success_flag = False
                
            try:
                post = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, config['selectors']['upload']['post'])))
                post.send_keys(Keys.END)
                post.click()
                print(self.systemNoiti + Fore.CYAN + f"{browser_name}" + Fore.WHITE + "Video đang được đăng, vui lòng đợi!")
                print("--------------------------------------------------------------------------------")
                print(Style.RESET_ALL)
                post_confirmation = EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[4]/div/div/div[1]")
                    )
                WebDriverWait(driver, 60).until(post_confirmation)
            except:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.execute_script('document.querySelector(".btn-post > button").click()')
                print(self.systemNoiti + Fore.CYAN + f"{browser_name}" + Fore.WHITE + "Video đang được đăng, vui lòng đợi!")
                print("--------------------------------------------------------------------------------")
                print(Style.RESET_ALL)
                post_confirmation = EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[4]/div/div/div[1]")
                    )
                WebDriverWait(driver, 60).until(post_confirmation)
                
            success_flag = True
            print(self.systemNoiti + Fore.CYAN + f"{browser_name}" + Fore.WHITE + f"Đã đăng video: {video}")
            print("--------------------------------------------------------------------------------")
            print(Style.RESET_ALL)
            
            try:
                minute_time = wait_time * 60
                print("--------------------------------------------------------------------------------")
                print(self.systemNoiti + Fore.CYAN + f"{browser_name}" + Fore.WHITE + f"Đợi {wait_time} giây trước khi tiếp tục...")
                print(Style.RESET_ALL)
            except:
                wait_time_int = int(wait_time)
                minute_time = wait_time_int * 60
                print("--------------------------------------------------------------------------------")
                print(self.systemNoiti + Fore.CYAN + f"{browser_name}" + Fore.WHITE + f"Đợi {wait_time_int} giây trước khi tiếp tục...")
                print(Style.RESET_ALL)
                
            print(Style.RESET_ALL)
            time.sleep(minute_time)