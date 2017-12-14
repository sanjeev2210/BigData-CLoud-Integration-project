#!/usr/bin/python2

import cgi

import commands


print 'Content-Type: text/html'
print

ipServer='192.168.43.52'

val=commands.getstatusoutput('sudo cat /var/www/cgi-bin/user_log')
user=val[1].split(':')[0]

clientName='{}-client'.format(user)

print '''

<html>
<head>
<style>
div.logport{
	width:40%;
	text-align:center;
	position:relative;
	height:200px;
	margin-bottom:70px;
	border-radius:4px;
}
td.key{
	font-size:20px;
	line-height:8px;
	color:black;
	font-family:Georgia;
	padding:10px;
}
.in{
	padding:10px;
	font-size:20px;
	border:2px ridge aqua;
	background:lightgrey;
	border-radius:3px;
}
.in:focus{
	box-shadow:0px 0px 5px black;
}
input.n {
    display: block;
    color: white;
    text-align: center;
    font-size:20px;
    padding: 16px;
    text-decoration: none;
    width: 200px;
    overflow: hidden;
    background-color: blue;
}

input.n:hover {
    background-color: black;
}
</style>
</head>
<body>
<form enctype="multipart/form-data" method="POST" action="http://www.thor.com/cgi-bin/run_final.py">
<h3>Mapper Reducer Job Submission:</h3>
<table>
<tr style="bottom:10px;">
<td>Target File Name:</td>
<td><input class="in" type="text" name="fname" style="font-size:20px;"/></td>
</tr>
<tr>
<td colspan="2">
<input class="n" type="submit" value="Submit Job"/>
</td>
<td></td>
</tr>
</table>
</form>
</body>
</html>
'''



#print clientName


fname=cgi.FormContent()['fname'][0]



commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/uploads/map.py /var/www/cgi-bin/uploads/red.py root@{}:/home/{}/'.format(ipServer,user))

commands.getstatusoutput('sshpass -p redhat  ssh -o stricthostkeychecking=no root@{}   sudo docker cp  /home/{}/map.py  {}:/'.format(ipServer,user,clientName))

commands.getstatusoutput('sshpass -p redhat  ssh -o stricthostkeychecking=no root@{}   sudo docker cp  /home/{}/red.py  {}:/'.format(ipServer,user,clientName))

commands.getstatusoutput('sshpass -p redhat  ssh -o stricthostkeychecking=no root@{}   sudo docker cp  /home/{}/data.txt  {}:/'.format(ipServer,user,clientName))

commands.getstatusoutput('sshpass -p redhat  ssh -o stricthostkeychecking=no root@{} sudo docker exec {} hadoop fs -put /data.txt /user/{}'.format(ipServer,clientName,user))


commands.getoutput('sudo sshpass -p redhat ssh -o stricthostkeychecking=no root@{0}  docker exec {1}  hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar   -input /user/{2}/data.txt   -mapper  ./map.py  -file map.py  -reducer  ./red.py  -file  red.py  -output  /output/{2}'.format(ipServer,clientName,user))

print '<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.thor.com/output.py">\n'

