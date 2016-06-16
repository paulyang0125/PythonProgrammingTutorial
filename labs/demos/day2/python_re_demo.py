#!/usr/bin/env
############################################
# python_re_demo.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################


import re

#detect the pattern
wordlist = ['hbasgoe', 'abhshgoe', 'hbatisgoe', 'tbgoe', 'tbortgoe','abaissed', 'abandoned', 'abased', 'abashed', 'abatised', 'abed', 'aborted','abaissgoe', 'abandongoe']
[w for w in wordlist if re.search('ed$',w)]
[w for w in wordlist if re.search('^..a..o..$',w)]


#range []
wordlist = ['abjectly', 'adjuster', 'gold','golder','dejected', 'golf', 'dejectly', 'injector', 'majestic','hold', 'hole']
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$',w)]
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]',w)]

#range + *
chat_words = ['miiinnee', 'mmmmmmmmiiiiiiiiinnnnnnnnneeeeeeee', 'mine','me','mingg','mi','ne' ]
[w for w in chat_words if re.search('^m+i+n+e+$', w)]
[w for w in chat_words if re.search('^m*i*n*e*$', w)]


#range \ {} () |
digitlist = ['123','331-points', '0.0085', 'C$','0.05','abv','2016' '0.1', 'JAP#','92.2','911-ppppppp''43643', '1978', 'US$','1.1253553','bread-and-butter','PO@','10-year','1.14', '1.1650', 'savings-and-loan','1.17', '1.0','10-day','331-bigpoints']
[w for w in digitlist if re.search('(ed|ing)$', w)]
[w for w in digitlist if re.search('^[0-9]+\.[0-9]+$', w)]
[w for w in digitlist if re.search('^[A-Z]+\$$', w)]
[w for w in digitlist if re.search('^[0-9]{4}$', w)]
[w for w in digitlist if re.search('^[0-9]+-[a-z]{3,5}$', w)]

#findall
word1 = 'smartdog smatdog ldoedog ddwwlaj'
re.findall('dog',word1)
word = 'supercalifragilisticexpialidocious'
re.findall('[aeiou]', word)

#option Flag
line = "Cats are smarter than dogs\n dfssss www";
bool(re.search( 'dogs$', line, re.I))
bool(re.search( 'dogs$', line, re.I|re.M))

#chinese

chinese_string = "恭喜發財"
pattern = "發財"
re.search(pattern,chinese_string)
new_pattern = "新喜"
new_c_string = re.sub(pattern,new_pattern,chinese_string)
print(new_c_string)


