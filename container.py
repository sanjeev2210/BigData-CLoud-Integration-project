#!/usr/bin/python2

print 'Content-Type: text/html'
print

import cgi
import commands

import mysql.connector as mariadb


db=mariadb.connect(user='root',password='1',database='lw')
cursor=db.cursor()


numData=cgi.FormContent()['numData'][0]
numTask=cgi.FormContent()['numTask'][0]
partSize=cgi.FormContent()['partSize'][0]



val=commands.getstatusoutput('sudo cat /var/www/cgi-bin/user_log')
user=val[1].split(':')[0]
ipServer='192.168.43.52'



ipDataList=[]
ipTaskList=[]
dataNodeList={}

#launching name node according to the input
#print '<h3> The Name Nodes launched are:<br/><br/>'

nameName='{}-master'.format(user)
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker run -dit --privileged=true --name {0}-master hadoop_copy:v1'.format(user,ipServer))
ip=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker inspect {0}-master | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(user,ipServer))
ipName=ip.split('"')[1]
commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/name.py root@{}:/mnt/'.format(ipServer))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/name.py {1}:/'.format(ipServer,nameName))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {2} python /name.py {1}'.format(ipServer,ipName,nameName))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/name.py'.format(ipServer))

cursor.execute("INSERT into resource VALUES (%s,%s,%s)",(user,nameName,ipName))
db.commit()

#print nameName+' : '+ipName
#print '<br/>'


#launching data nodes according to the input



i=1
#print '<h3> The Data Nodes launched are:<br/><br/>'
while i<=int(numData):
	Str="---\n- hosts: base\n  tasks:\n    - lvol:\n        vg: 'cloud'\n        lv: '{0}-d{1}'\n        size: {2}g\n    - command: 'mkfs.ext4 /dev/cloud/{0}-d{1}'\n    - file:\n        state: directory\n        path: '/media/{0}-{1}'\n        mode: 'u+rwx,g=rx,o+rwx'\n    - name: Mount up device by path\n      mount:\n        path: '/media/{0}-d{1}'\n        src: '/dev/cloud/{0}-d{1}'\n        fstype: ext4\n        state: mounted\n    - lineinfile:\n        path: '/etc/exports'\n        line: '/media/{0}-d{1} *(rw,sync,no_root_squash)'\n    - command: 'exportfs -v'".format(user,i,partSize)
	#commands.getstatusoutput('sudo chown apache /var/www/cgi-bin/yml-files/lvcreate.yml')
	fh=open('/var/www/cgi-bin/yml-files/lvcreate.yml','w')
	fh.write(Str+'\n')
	fh.close()
	commands.getoutput('sudo ansible-playbook /var/www/cgi-bin/yml-files/lvcreate.yml')
	dataName='{}-d{}'.format(user,i)
	commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{2} docker run -dit --privileged=true -v /media/{0}-d{1}:/data  --name {0}-d{1} hadoop_copy:v1'.format(user,i,ipServer))
	ip=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{2} docker inspect {0}-d{1} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(user,i,ipServer))
	ipData=ip.split('"')[1]
	ipDataList.append(ipData)
	commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/data.py root@{}:/mnt/'.format(ipServer))
	commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/data.py {1}:/'.format(ipServer,dataName))
	commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {2} python /data.py {1}'.format(ipServer,ipName,dataName))
	commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/data.py'.format(ipServer,dataName))
	dataNodeList.update({ipData:dataName})
	#print dataName+' : '+ipData
	cursor.execute("INSERT into data VALUES (%s,%s,%s)",(user,dataName,ipData))
	db.commit()
	#print '&nbsp;&nbsp;&nbsp;&nbsp;'
	i+=1
print '<br/>'

#launching job tracker according to the input


#print '<h3> The Job Tracker launched are:<br/><br/>'
jobName='{}-job'.format(user)
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker run -dit --privileged=true --name {0}-job hadoop_copy:v1'.format(user,ipServer))
ip=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker inspect {0}-job | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(user,ipServer))
ipJob=ip.split('"')[1]
commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/job.py root@{}:/mnt/'.format(ipServer))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/job.py {1}:/'.format(ipServer,jobName))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {1} python /job.py {2} {3}'.format(ipServer,jobName,ipJob,ipName))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/job.py'.format(ipServer))

#print jobName+' : '+ipJob

cursor.execute("INSERT into resource VALUES (%s,%s,%s)",(user,jobName,ipJob))
db.commit()

#print '<br/>'


#launching task trackers according to the input


if int(numTask)==int(numData):
	i=0
	#print '<h3> The Task Trackers launched are:<br/><br/>'
	while i<int(numTask):
		taskName=dataNodeList[ipDataList[i]]
		commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/task.py root@{}:/mnt/'.format(ipServer))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/task.py {1}:/'.format(ipServer,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {2} python /task.py {1}'.format(ipServer,ipJob,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/task.py'.format(ipServer,taskName))
		#print taskName+' : '+ipDataList[i]
		cursor.execute("INSERT into task VALUES (%s,%s,%s)",(user,taskName,ipDataList[i]))
		db.commit()
		ipTaskList.append(ipDataList[i])
		#print '&nbsp;&nbsp;&nbsp;&nbsp;'
		i+=1
	print '<br/>'
elif int(numTask)>int(numData):
	i=0
	#print '<h3> The Task Trackers launched are:<br/><br/>'
	while i<int(numData):
		taskName=dataNodeList[ipDataList[i]]
		commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/task.py root@{}:/mnt/'.format(ipServer))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/task.py {1}:/'.format(ipServer,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {2} python /task.py {1}'.format(ipServer,ipJob,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/task.py'.format(ipServer,taskName))
		#print taskName+' : '+ipDataList[i]
		cursor.execute("INSERT into task VALUES (%s,%s,%s)",(user,taskName,ipDataList[i]))
		db.commit()
		ipTaskList.append(ipDataList[i])
		#print '&nbsp;&nbsp;&nbsp;&nbsp;'
		i+=1
	diff=int(numTask)-int(numData)
	j=1
	while j<=diff:
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker run -dit --privileged=true --name {0}-t{2} hadoop_copy:v1'.format(user,ipServer,j))
		ip=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker inspect {0}-t{2} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(user,ipServer,j))
		taskName='{}-t{}'.format(user,j)
		commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/task.py root@{}:/mnt/'.format(ipServer))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/task.py {1}:/'.format(ipServer,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {2} python /task.py {1}'.format(ipServer,ipJob,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/task.py'.format(ipServer,taskName))
		ipTask=ip.split('"')[1]
		ipTaskList.append(ipTask)
		#print taskName+' : '+ipTask
		cursor.execute("INSERT into task VALUES (%s,%s,%s)",(user,taskName,ipTask))
		db.commit()
		#print '&nbsp;&nbsp;&nbsp;&nbsp;'
		j+=1
	print '<br/>'

elif int(numTask)<int(numData):
	i=0
	#print '<h3> The Task Trackers launched are:<br/><br/>'
	while i<int(numTask):
		taskName=dataNodeList[ipDataList[i]]
		commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/task.py root@{}:/mnt/'.format(ipServer))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/task.py {1}:/'.format(ipServer,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {2} python /task.py {1}'.format(ipServer,ipJob,taskName))
		commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/task.py'.format(ipServer,taskName))
		#print taskName+' : '+ipDataList[i]
		cursor.execute("INSERT into task VALUES (%s,%s,%s)",(user,taskName,ipDataList[i]))
		db.commit()
		ipTaskList.append(ipDataList[i])
		#print '<br/>'
		i+=1

#launching client system

#print '<h3> The Client IP is:<br/><br/>'
clientName='{}-client'.format(user)
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker run -dit --privileged=true --name {0}-client hadoop_copy:v1'.format(user,ipServer))
ip=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} docker inspect {0}-client | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(user,ipServer))
commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/bin/client.py root@{}:/mnt/'.format(ipServer))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker cp /mnt/client.py {1}:/'.format(ipServer,clientName))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker exec {1} python /client.py {2} {3}'.format(ipServer,clientName,ipJob,ipName))
commands.getstatusoutput('sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} rm /mnt/client.py'.format(ipServer))
ipClient=ip.split('"')[1]
cursor.execute("INSERT into resource VALUES (%s,%s,%s)",(user,clientName,ipClient))
db.commit()
#print clientName+' : '+ipClient

db.close()

commands.getstatusoutput('sshpass -p redhat  ssh -o stricthostkeychecking=no root@{}  docker exec {} hadoop fs -mkdir /user/{}'.format(ipServer,clientName,user))

print "Cluster Successfully Created....Check out the Dashboard...!!!"




