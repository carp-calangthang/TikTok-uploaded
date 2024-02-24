import os
import time
from colorama import Fore, Style
from multiprocessing import Process
from module.load_proxy_module import load_proxies
from module.check_data_module import check_cookies
from module.load_cookies_module import load_cookie
from module.upload_with_cookies import upload_videos

os.system("cls")
print("---------------------------------------------------------------------------- \n")
print("---------------------------------------------------------------------------- \n")
print("---------------------------------------------------------------------------- \n")

def get_c_user_from_cookie(cookies):
    start_index = cookies.find("csrf_session_id=")
    if start_index != -1:
        end_index = cookies.find(";", start_index)
        if end_index == -1:
            end_index = None
        c_user_value = cookies[start_index + len("csrf_session_id="):end_index]
        print(c_user_value)
        return c_user_value
    else:
        return None

def run_process(cookies, caption, wait_time, browser_name):
    process_action = upload_videos()
    c_user = get_c_user_from_cookie(cookies)
    browser_name_with_c_user = f"{browser_name}: {c_user} "
    process_action.run_upload_videos(cookies, caption, wait_time, browser_name_with_c_user)
    
if __name__ == "__main__":
    adminNoiti = Fore.CYAN + "Admin: "
    systemNoiti = Fore.GREEN + "System: "
    browserNoiti = Fore.MAGENTA + "Browser "
    warning = Fore.YELLOW + "Warn: "   
    error = Fore.RED + "Error: "
    browser_name = "ID "
    script_path = os.path.abspath(__file__) 
    src_directory = os.path.dirname(script_path)
    cookie_path = os.path.join(src_directory, '..', 'data', 'cookies.txt')
    
    print(adminNoiti + Fore.WHITE + "Nhập caption cho video: ")
    caption = input()
    print(adminNoiti + Fore.WHITE + "Thời gian chờ (phút): ")
    wait_time = float(input())
    print(adminNoiti + Fore.WHITE + "Số tài khoản chạy cùng lúc: ")
    len_count = int(input())
    print(Style.RESET_ALL)
    
    cookie_instance = load_cookie()
    cookie_values = cookie_instance.getCookie()
    processes = []
    
    check = check_cookies()    
    check_null = check.check_null_cookies()
    check_len = check.check_len_cookies(len_count)
    
    while True:
        
        if check_null and check_len:
            taken_cookies = cookie_values[:len_count]
            remaining_cookies = cookie_values[len_count:]
            
            cookies_list = taken_cookies

            with open(cookie_path, "w") as cks_file:
                cks_file.writelines(remaining_cookies)
                
        elif check_null and not check_len:
            cookies_list = cookie_values
            with open(cookie_path, "w") as cks_file:
                cks_file.writelines([])
                
        elif not check_null:
            print(adminNoiti + Fore.WHITE + "Đã sử dụng hết cookie, chương trình dừng hoạt động")
            break
        
        for cookie in cookies_list:
            login_cookies = cookie.strip()
            
            process = Process(target=run_process, args=(login_cookies, caption, wait_time, browser_name))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()