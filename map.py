#!/usr/bin/python2

import sys

for i in sys.stdin:
	i=i.strip()
	if i.split(':')[6]=='/bin/bash' :
		print i.split(':')[0]
