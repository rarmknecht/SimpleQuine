#!/usr/bin/python

file = open('prog.txt','r')

s = ""
for b in file.read():
	s+="%d," % ord(b)

print(s[:-1])
