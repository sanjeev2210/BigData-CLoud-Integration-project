#!/usr/bin/python2

import sys



for i in sys.stdin:
	val=i.split()
	if val[9]=='6' or val[9]=='4' :
		data='{} {}'.format(val[0],val[9])
		print data
