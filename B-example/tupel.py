'''A tuple is a collection of objects which ordered and immutable.
 Tuples are sequences, just like lists. The differences between
  tuples and lists are, the tuples cannot be changed unlike lists and
   tuples use parentheses, whereas lists use square brackets.'''
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print ("First tuple length : ", len(tuple1))
print ("Second tuple length : ", len(tuple2))


tuple1, tuple2 = ( 'xyz', 'zara', 'abc'), (456, 700, 200)
print("Max value element : ", max(tuple1))
print ("Max value element : ", max(tuple2))
print ("min value element : ", min(tuple1))


#seq − This is a sequence to be converted into tuple
aList = [123, 'xyz', 'zara', 'abc']
aTuple = tuple(aList)
print ("Tuple elements : ", aTuple)



