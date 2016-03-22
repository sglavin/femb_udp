#!/usr/bin/env python33

import sys 
import string
from femb_udp_cmdline import FEMB_UDP

if len(sys.argv) != 2 :
	print 'Invalid # of arguments, usage python read_reg <reg #>'
	sys.exit(0)

regVal = int( sys.argv[1] )
if (regVal < 0) or (regVal > 666):
	print 'Invalid register number'
        sys.exit(0)

femb = FEMB_UDP()
val = femb.read_reg(regVal)
print hex(val)