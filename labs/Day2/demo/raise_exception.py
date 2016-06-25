

#!/usr/bin/env
############################################
# raise_exception.py
# Author: Paul Yang
# Date: June, 2016
# Brief:
############################################


def password_check(passwd):
    if len(passwd) < 1:
        raise Exception("PasswordFormatError: length is {}".format(len(passwd)))
    if passwd.find('*') != -1:
        raise Exception("PasswordFormatError: contains *")

password = ""
try:
    password_check(password)
except Exception as e:
    print(e)


