#!/usr/bin/env
############################################
# unicode.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################

a = "王建文"
type(a)
ascii(a)
#"'\\u738b\\u5efa\\u6587'"
a.encode('utf-8')
type(a.encode('utf-8'))
#b'\xe7\x8e\x8b\xe5\xbb\xba\xe6\x96\x87'
a.encode('big5')
#b'\xa4\xfd\xab\xd8\xa4\xe5'
a.encode('utf-16')
#b'\xff\xfe\x8bs\xfa^\x87e'
ord('\u738b')
chr(29579)
#'王'

b'\xe7\x8e\x8b'.decode("utf-8")