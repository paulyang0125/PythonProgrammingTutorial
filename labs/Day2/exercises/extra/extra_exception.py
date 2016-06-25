#!/usr/bin/env
############################################
# extra_exception.py
# Author: Paul Yang
# Date: June, 2016
# Brief:
############################################


import re
def codecheck(passwd):
    regex = r"[^1-9]+"
    assert type(passwd) is str, "�K�X���Ostring: %r" % passwd
    
    if len(passwd) != 8:
        raise Exception("�u����8��ƱK�X, �A��J�K�X���׬�{}".format(len(passwd)))
    elif re.findall(regex, passwd):
        raise Exception("�u����1-9�Ʀr, �A��J��{}".format(passwd))
        
        

codes = [1234,'33',"98341021","12345678"]
codecheck(codes[0])
codecheck(codes[1])
codecheck(codes[2])    

## comment the above three codecheck to see the result below
for code in codes:
    try:
        codecheck(code)
    except Exception as e:
        print(e)
    else:
        print("�K�X���T")
    finally:
         print("���ұK�X����")
         print("\n")