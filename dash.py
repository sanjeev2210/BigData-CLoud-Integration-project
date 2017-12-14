#!/usr/bin/python2

import mysql.connector as mariadb
import commands

db=mariadb.connect(user='root',password='1',database='lw')

cursor=db.cursor()

print 'Content-Type: text/html'

print

print '<h2>Cluster Details:</h2>'

#user=commands.getstatusoutput('sudo cat /var/www/cgi-bin/user_log')

#user=val[1].split(':')[0]

val=commands.getstatusoutput('sudo cat /var/www/cgi-bin/user_log')
user=val[1].split(':')[0]

print '<div style="float:left;margin-right:20px;">'

print '<h3>Name Node:</h3>'

name='{}-master'.format(user)
cursor.execute('select ip from resource where container=%s',(name,))
n=cursor.fetchone();

n_ip=n[0]

print '<table style="border: 1px groove grey;padding :8px;color:maroon;font-size:20px;"><tr><td>{}</td><td>{}</td></tr></table>'.format(name,n_ip)

print '<h3>Data Nodes:</h3>'

cursor.execute('select ip,container from data where user=%s',(user,))
d=cursor.fetchall();

print '<table style="border: 1px groove grey;padding :8px;color:maroon;font-size:20px;">'
i=0
while i < len(d):
	#print i[1]
	#print i[0]
	print '<tr><td>{}</td><td>{}</td></tr>'.format(d[i][1],d[i][0])
	i+=1

print '</table>'

print '</div>'
print '<div style="float:left;margin-right:20px;">'
print '<h3>Job Tracker:</h3>'

name='{}-job'.format(user)
cursor.execute('select ip from resource where container=%s',(name,))
j=cursor.fetchone();

n_ip=j[0]

print '<table style="border: 1px groove grey;padding :8px;color:maroon;font-size:20px;"><tr><td>{}</td><td>{}</td></tr></table>'.format(name,n_ip)


print '<h3>Task Trackers:</h3>'

cursor.execute('select ip,container from task where user=%s',(user,))
t=cursor.fetchall();

print '<table style="border: 1px groove grey;padding :8px;color:maroon;font-size:20px;">'
i=0
while i<len(t):
	#cont=i[1]
	#val=i[0]
	print '<tr><td>{}</td><td>{}</td></tr>'.format(t[i][1],t[i][0])
	i+=1

print '</table>'
print '</div>'
print '<div style="float:left;">'
print '<h3>Client System:</h3>'

name='{}-client'.format(user)
cursor.execute('select ip from resource where container=%s',(name,))
c=cursor.fetchone();

n_ip=c[0]

print '<table style="border: 1px groove grey;padding :8px;color:maroon;font-size:20px;"><tr><td>{}</td><td>{}</td></tr></table>'.format(name,n_ip)

print '</div>'

db.close()


