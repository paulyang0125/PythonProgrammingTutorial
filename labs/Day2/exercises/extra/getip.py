#!/usr/bin/env
############################################
# getip.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################
from subprocess import check_output
import re
import platform

def get_ips_windows():
    pattern = '^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
    ip_data = check_output('ipconfig').decode('cp437').split()
    ip_list = []
    for item in ip_data:
        if re.findall(pattern,item):
            ip_list.append(item)
    return [i for i in ip_list if i]

def get_ips_rpi():
    ip_data = check_output('ifconfig').decode().split()
    ip_list = []
    for item in ip_data:
        if "addr:" in item:
            ip_list.append(item[5:])
    return [i for i in ip_list if i]


if platform.system() == "Windows":print(get_ips_windows())
elif platform.system() == 'Linux':print(get_ips_rpi())
else:print("not supportive OS")