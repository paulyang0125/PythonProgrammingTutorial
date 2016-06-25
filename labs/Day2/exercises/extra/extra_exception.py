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
    assert type(passwd) is str, "密碼不是string: %r" % passwd
    
    if len(passwd) != 8:
        raise Exception("只接受8位數密碼, 你輸入密碼長度為{}".format(len(passwd)))
    elif re.findall(regex, passwd):
        raise Exception("只接受1-9數字, 你輸入為{}".format(passwd))
        
        

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
        print("密碼正確")
    finally:
         print("驗證密碼完成")
         print("\n")