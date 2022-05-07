# 1. mutable Data type = can change its state or contant
"""list
 dictionary
 byte array """
# 2. im mutable data type= can't change the state and contant 
"""
int
float
complex
string
tuple
set """
# three type of number
from sre_parse import State


a=5
print(a,type(a))
a=5.5
print(a,type(a))
a=5+5j
print(a,type(a))
#String
s="I am Babita"
print(s,type(s)) 
 # muliline string 
s='''Hi   
my name is babita maurya
i am from mumbai'''
print(s)
# list
l=[4,"b",8]
# we can update the value in list
l[2]=10
print(l,type (l))
#tuple
'''we can not update the value in tuple
in tuple type data we need to
put the value
more than one'''
t=(1,3,"a")
print(t ,type(t))
#Dictionary
'''Dictionary is unorder collection of key - value pair.
in python, dictionry are defined with in {} with each
item being a pair in the form key:vlue'''
# key is unic and value can be repet
d={
    'Name':'Babita',
    'state': 'Maharashtra'
}
print(d)
#set
'''every set element is unique
and can not be changed(im mutable)'''
s={
    10,20,20, 10
}
print(s)