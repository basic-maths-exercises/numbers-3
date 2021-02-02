import numpy as np

def getNumberArray( N ) :
  # Your code goes here
  val = np.zeros(4)
  for i in range(4) :
     pp = 10**(3-i)
     val[i] = np.floor( N / pp )
     N = N - val[i]*pp
  return val

# This calls the function you have written to check if it works
print( getNumberArray(5623) )
