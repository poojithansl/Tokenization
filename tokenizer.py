#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def mixtheregex(*items):
	return '(?:' + '|'.join(items) + ')'

word=r'(?:[\w_\‘\’\'\-\:\\)\(]+)'		#Regex to match words

number=(r'(?:[\+-]?\$?\d+(?:\.\d+)?(?:[eE]-?\d+)?%?)(?![A-Za-z])(?:\\s*/\s*(?:[\+-]?\$?\d+(?:\.\d+)?(?:[eE]-?\d+)?%?)(?![A-Za-z]))?')
											#Regex for numbers(decimals,...)
Punct=r"['\"“”‘’?.!…,:;@/\\]"		#Punctuation	
hashi = r'(?:\#+[\w]+[_\'\-]*[\w]+)'		#Hash regex

mention=r'(?:@[\w_]+)'			#Mention regex
ellipsis=r'(?:\.(?:\s*\.){1,})'		#Ellipsis regex
h_nu=r"""(?:(?:\+?[01][\-\s.]*)?(?:[\(]?\d{3}[\-\s.\)]*)?\d{3}[\-\s.]*\d{4})"""		#Phonenumberregex
brack=r'(?:[(][\w_\'\-\:\\)\(]+[)])'		#Brackets regex
time=(r'\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM|am|pm)?')	#Time regex
other=r'(?:\S)'
br=r'(?:[{][\w_\'\-\:\\)\(]+[}])'		#other kindof bracket regex
has=r'(?:[<][\w_\'\-\:\\)\(]+[>])'			#<> regex
sqb=r'(?:[[][\w_\'\-\:\\)\(]+[]])'			#square bracket regex
quotes=r'(?:["][\w_\'\-\:\\)\(]+["])'
url=r'(?:http[s]?:\//[\w]+.[\w]+(?:[\/])*[\w]+)'
email=r'(?:[a-zA-Z(0-9)]+@[a-z]+.[a-z]{3,3})'
t_re=re.compile((mixtheregex(email,url,word,quotes,number,hashi,mention,ellipsis,Punct,time,h_nu,brack,br,has,other,sqb)),re.VERBOSE|re.I|re.UNICODE)

def Tokenize(s):
	
	print s

	s=str(s).decode('utf-8')
	tokens=t_re.findall(s)
	
	for k in tokens:	
		print k.encode('utf-8')
		
	return tokens
	
	
if __name__=="__main__":
	
	for j in open('test9.txt', mode='r').readlines():
			
			l=Tokenize(j)
			
