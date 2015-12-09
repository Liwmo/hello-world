#!/usr/bin/env

def shiftEN():
    execfile("shiftEN.py")
    
def shiftDE():
    execfile("shiftDE.py")

def affineEN():
    execfile("affineEN.py");

def affineDE():
    execfile("affineDE.py");
    
def vigenereEN():
    execfile("vigenereEN.py");
    
def vigenereDE():
    execfile("vigenereDE.py");

options = {
    0: shiftEN,
    1: shiftDE,
    2: affineEN,
    3: affineDE,
    4: vigenereEN,
    5: vigenereDE,
}

for i in range(0, 5):
    stuff = "\t{} {}".format(i, options[i].__name__)
    print stuff

num = raw_input("Enter an option: ")
try:
    n = int(num)
except ValueError:
    print "Cannot parse int."
if num.isdigit() is False or n > 5:
    print "Invalid input."
else:
    options[n]()
