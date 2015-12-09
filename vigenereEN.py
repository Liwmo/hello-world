#!/usr/bin/env

from math import *

phrase = raw_input("Enter a Phrase to be Encoded Here: ")

phrase1 = phrase.replace(" ", "")
phrase2 = phrase1.upper()

while phrase2.isalpha():
	keyword_raw = raw_input("Enter a Keyword: ")
	break
else: 
	phrase = raw_input("Enter a Phrase to be Decoded Here: ")
	phrase1 = phrase.replace(" ", "")
	phrase2 = phrase1.upper()
	
if keyword_raw.isalpha():
	print
else:
	print ">>>ERROR: Keyword contains incompatible characters"
	keyword_raw = raw_input("Enter a Keyword: ")
	
dict1 = { #Converts each letter to a number
"A": 0, 
"B": 1,
"C": 2, 
"D": 3,
"E": 4, 
"F": 5,
"G": 6, 
"H": 7,
"I": 8, 
"J": 9,
"K": 10, 
"L": 11,
"M": 12, 
"N": 13,
"O": 14, 
"P": 15,
"Q": 16, 
"R": 17,
"S": 18, 
"T": 19,
"U": 20, 
"V": 21,
"W": 22, 
"X": 23,
"Y": 24,
"Z": 25,
}

dict2 = { #Converts number back to letter - can possibly be combined with dict1??
0 : "A",
1 : "B",
2 : "C",
3 : "D",
4 : "E",
5 : "F",
6 : "G",
7 : "H",
8 : "I",
9 : "J",
10 : "K",
11 : "L",
12 : "M",
13 : "N",
14 : "O",
15 : "P",
16 : "Q",
17 : "R",
18 : "S",
19 : "T",
20 : "U",
21 : "V",
22 : "W",
23 : "X",
24 : "Y",
25 : "Z",
}

keyword = keyword_raw.replace(" ", "") #remove spaces from keyword_raw
keyword_upper = keyword.upper() #forces uppercase for keyword

L = []   #puts characters from input in a list 
for char in keyword_upper:
	L.append(char) 

shift = []   #defines shift functions for each letter
for i in range(0,len(keyword_upper)):
	shift.append(dict1[L[i]]) 
	
Plaintext = []   #turns letters to numbers and puts in a new list
for char in phrase2:
	Plaintext.append(dict1[char])

for i in range(0,len(phrase2)): #Finally shifts the numbers in previously defined list
	for a in range(0,len(keyword)):
		if i % len(keyword) == a:
			Plaintext[i] = (Plaintext[i] + shift[a]) % 26 

Ciphertext = "" #Finally spits out Ciphertext
for x in Plaintext:
	Ciphertext += dict2[x]

print Ciphertext

