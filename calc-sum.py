import os
import math

mul = 3600

with open('path-to-file-for-reading','r') as f, open('path-to-file-for-writing','w') as s:
    for line in f:
        ##  Multiply file values with 3600
        val = float(line) * int(mul)
        ##  Uncomment next line to see output of 3600 * variable
        #print val
        s.write( str(val)+ '\n' )

##  Adding all values
with open('path-to-file-for-reading','r') as o, open('path-to-file-for-writing','w') as t:
    z = (sum(float(line) for line in o))
    t.write(str(z))
