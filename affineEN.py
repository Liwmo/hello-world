#!/usr/bin/env

from math import *
acceptable_values = [1,3,5,7,9,11,15,17,19,21,23,25]

phrase = raw_input("Enter a Phrase to be Encoded Here: ")

phrase1 = phrase.replace(" ", "")
phrase2 = phrase1.upper()

if phrase2.isalpha():
	int_mult_shift = int(raw_input("Enter an integer relatively prime with 26: ")) 
	mult_shift = int_mult_shift % 26
	while mult_shift not in acceptable_values:
		print ">>>ERROR: Integer is not relatively prime with 26"
		mult_shift = int(raw_input("Enter an integer relatively prime with 26 (multiplicative shift): "))
	add_shift = int(raw_input("Enter any integer: "))
else:
	print ">>>ERROR: Plaintext contains incompatible characters"
	
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

dict2 = { #Dictionary to convert each number back to a letter
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

Plaintext = []

for char in phrase2:
	Plaintext.append(dict1[char])

Step1 = []	
for x in Plaintext:
	Step1.append((mult_shift * x + add_shift) % 26) #Computes ax + b mod 26

Ciphertext = ""
for x in Step1:
	Ciphertext += dict2[x]

print Ciphertext

