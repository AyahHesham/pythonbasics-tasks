#task1:modify printing hello python function code with a comment of function usages.
#def hellopython
#print(Hello'python!)

#solution:
#function for print sentance and not take any parameters
from calendar import prmonth
from lib2to3.pytree import convert


def hellopython():
    print("Hello'python!")
hellopython()
#__________________________________________________________________________

#task2:write acode to print the excpected output using sep and end paramiters.
#I'm__learning python
#thanks ITI:)

#solution:
#function takes two parameters sep and end and print them
def thankforiti(sep,end):
    print(f'{sep}\n{end}')
thankforiti("I'm__learning python",'thanks ITI:)')

#_______________________________________________________________________

#task3:calculate the mean value of 5 numbers.

#solution:
a,b,c,d,e=11,7,4,18,37
#mean=sumition of numbers divided by those counts
print((a+b+c+d+e)/5)
#______________________________________________________________________

#task4:write a python program to print the calendar of given month and year.
#year=2021 #month=4

#solution:
year=2021
month=4
#w=The width between two columns. Default value is 0.
#l=Blank line between two rows. Default value is 0.
prmonth(year,month,w=0,l=0)
#__________________________________________________________________________

#task5:write a python program that accepts an integre(n) and computes the value of n+nn+nnn

#solution:
n=5
print(n+n*n+n*n*n)
#_________________________________________________________________________
#task6:write a python program that accepts a words from the users and reverse it like :
#enter the word:ahmed
#reversed:demha

#solution:
word=input('enter the word:')
#this def for convert word from characters to list tfor reverse it
def Convert(word):
    list1 = []
    list1[:0] = word
    reverselist=list1[::-1]
    chartoword=""
    for x in reverselist:
        #chartoword=characters to word
        chartoword=chartoword+x
    return chartoword 
print(F'reversed:{Convert(word)}')
#___________________________________________________________________________


