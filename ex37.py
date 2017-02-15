#Keywords

#with statement: two related operation that would like to execute as a pair 
with open("output.txt", 'w') as f:
	f.write('Hi there!')
	#no need to have a close as the with statment automatically closes the file.

#Assert: ensure something is true. Good for when looking for bug
#**! not super clear yet. https://wiki.python.org/moin/UsingAssertionsEffectively

#break
for letter in 'Python':     # First Example
   if letter == 'h':
      break #tells code to stop if this occurs
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"

#continue
for letter in 'Python':     # First Example
   if letter == 'h': #if this occurs continue for loop in code.
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
print "Good bye!"

#pass
for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"

#del: deletes from a list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a
 