#!/usr/bin/python2

import sys

kol_four=0
kol_six=0

ban_four=0
ban_six=0

ch_four=0
ch_six=0

pun_four=0
pun_six=0

del_four=0
del_six=0

raj_four=0
raj_six=0

mum_four=0
mum_six=0

dec_four=0
dec_six=0

kochi_four=0
kochi_six=0

pun_four=0
pun_six=0

hy_four=0
hy_six=0

pune_four=0
pune_six=0

guj_four=0
guj_six=0

for v in sys.stdin:
	i=v.split()
	if i[0]=='KolkataKnightRiders' :
		if i[1]=='4':
			kol_four+=1
		else:
			kol_six+=1
	elif i[0]=='RoyalChallengersBangalore' :
		if i[1]=='4':
			ban_four+=1
		else:
			ban_six+=1
	elif i[0]=='ChennaiSuperKings' :
		if i[1]=='4':
			ch_four+=1
		else:
			ch_six+=1
	elif i[0]=='KingsXIPunjab' :
		if i[1]=='4':
			pun_four+=1
		else:
			pun_six+=1
	elif i[0]=='DelhiDaredevils' :
		if i[1]=='4':
			del_four+=1
		else:
			del_six+=1
	elif i[0]=='RajasthanRoyals' :
		if i[1]=='4':
			raj_four+=1
		else:
			raj_six+=1

	elif i[0]=='MumbaiIndians' :
		if i[1]=='4':
			mum_four+=1
		else:
			mum_six+=1
	elif i[0]=='DeccanChargers' :
		if i[1]=='4':
			dec_four+=1
		else:
			dec_six+=1
	elif i[0]=='KochiTuskersKerala' :
		if i[1]=='4':
			kochi_four+=1
		else:
			kochi_six+=1
	elif i[0]=='PuneWarriors' :
		if i[1]=='4':
			pun_four+=1
		else:
			pun_six+=1
	elif i[0]=='SunrisersHyderabad' :
		if i[1]=='4':
			hy_four+=1
		else:
			hy_six+=1
	elif i[0]=='RisingPuneSupergiants' :
		if i[1]=='4':
			pune_four+=1
		else:
			pune_six+=1
	elif i[0]=='GujaratLions' :
		if i[1]=='4':
			guj_four+=1
		else:
			guj_six+=1


print "Statistics of 4's and 6's hit by IPL Teams :"

print 'KolkataKnightRiders:'
print "4's : "+str(kol_four)
print "6's : "+str(kol_six)

print 'RoyalChallengersBangalore:'
print "4's : "+str(ban_four)
print "6's : "+str(ban_six)

print 'ChennaiSuperKings:'
print "4's : "+str(ch_four)
print "6's : "+str(ch_six)

print 'KingsXIPunjab:'
print "4's : "+str(pun_four)
print "6's : "+str(pun_six)

print 'DelhiDaredevils:'
print "4's : "+str(del_four)
print "6's : "+str(del_six)

print 'RajasthanRoyals:'
print "4's : "+str(raj_four)
print "6's : "+str(raj_six)

print 'MumbaiIndians:'
print "4's : "+str(mum_four)
print "6's : "+str(mum_six)

print 'DeccanChargers:'
print "4's : "+str(dec_four)
print "6's : "+str(dec_six)

print 'KochiTuskersKerala:'
print "4's : "+str(kochi_four)
print "6's : "+str(kochi_six)

print 'PuneWarriors:'
print "4's : "+str(pun_four)
print "6's : "+str(pun_six)

print 'SunrisersHyderabad:'
print "4's : "+str(hy_four)
print "6's : "+str(hy_six)

print 'RisingPuneSupergiants:'
print "4's : "+str(pune_four)
print "6's : "+str(pune_six)

print 'GujaratLions:'
print "4's : "+str(guj_four)
print "6's : "+str(guj_six)
