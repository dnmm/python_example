#Control Statement & Description
#	break statement
'''Terminates the loop statement and transfers execution to the statement immediately following the loop'''
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break
    
#continue statement
'''Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.'''
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)


  # pass statement
'''The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute'''
for letter in 'Python': 
   if letter == 'h':
      pass
      print( 'This is pass block')
   print ('Current Letter :', letter)