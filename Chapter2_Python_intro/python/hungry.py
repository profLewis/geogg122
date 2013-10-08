#!/usr/bin/env python

"""Exercise in logical statements
  
   P. Lewis p.lewis@ucl.ac.uk

   Tue  8 Oct 2013 10:11:03 BST
"""

# hunger threshold in hours
hungerThreshold = 3.0
# sleep threshold in hours
sleepThreshold = 8.0

# time since fed, in hours
timeSinceFed = 4.0
# time since sleep, in hours
timeSinceSleep = 3.0

# Note use of \ as line continuation here
# It is poor style to have code lines > 79 characters
#
# see http://www.python.org/dev/peps/pep-0008/#maximum-line-length
#
print "Tired and hungry?",(timeSinceSleep >= sleepThreshold) and \
                            (timeSinceFed >= hungerThreshold)
print "Just tired?",(timeSinceSleep >= sleepThreshold) and \
                            (not (timeSinceFed >= hungerThreshold))
print "Just hungry?",(not (timeSinceSleep >= sleepThreshold)) and \
                            (timeSinceFed >= hungerThreshold)
