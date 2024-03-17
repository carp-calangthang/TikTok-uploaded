import os

class check_ssid:
    
    def __init__(self):
        self.script_path = os.path.abspath(__file__) 
        self.src_directory = os.path.dirname(self.script_path)
        self.ssid_path = os.path.join(self.src_directory, '..', 'data', 'ssid.txt')
    
    def check_null_ssid(self):

        with open(self.ssid_path, "r") as cks:
            ssids = cks.readlines()

        return bool(ssids)

    def check_len_ssids(self, len_ssids):

        with open(self.ssid_path, "r") as cks:
            ssids = cks.readlines()

        if len(ssids) >= len_ssids:
            return True
        else:
            return False