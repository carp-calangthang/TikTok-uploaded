import os

def load_proxies():
    script_path = os.path.abspath(__file__) 
    src_directory = os.path.dirname(script_path)
    proxy_path = os.path.join(src_directory, '..', 'data', 'proxies.txt')

    with open(proxy_path, 'r') as file:
        proxies_list = file.readlines()
        
        print(proxies_list)