#!/bin/python

#Das ist ein kleines terminal-Programm, das Ihr Alter in tagen auswirft.

name = input("Wie ist Ihr Name? \n")

print("\n \n Hallo " + name)

print("\n" +  name + ", bitte geben Sie Ihr Alter an: \n")

alter = int(input())  

days_calc = alter * 365

days = str(days_calc)

print("\n \n Sie sind " + days + " Tage alt.")


