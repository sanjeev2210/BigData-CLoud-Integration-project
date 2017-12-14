#!/usr/bin/python2

import cgi
import commands

print 'Content-Type: text/html'
print

ipServer='192.168.43.52'

val=commands.getstatusoutput('sudo cat /var/www/cgi-bin/user_log')
user=val[1].split(':')[0]

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
input.in{
	padding:10px;
	font-size:20px;
	border:2px ridge aqua;
	background:lightgrey;
	border-radius:3px;
}
input.in:focus{
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
<form enctype="multipart/form-data" method="POST" action="http://www.thor.com/cgi-bin/upload.py">
<h3>Upload file to your HDFS:</h3>
<table>
<tr style="bottom:10px;">
<td><input type="file" name="fname" style="font-size:20px;"/></td>
</tr>
<tr>
<td colspan="2">
<input class="n" type="submit" value="Upload File"/>
</td>
<td></td>
</tr>
</table>
</form>
</body>
</html>
'''

fdata=cgi.FormContent()['fname'][0]
fh=open('/var/www/cgi-bin/uploads/data.txt','w')
fh.write(fdata)
fh.close()

commands.getstatusoutput('sshpass -p redhat sudo scp /var/www/cgi-bin/uploads/data.txt root@{}:/home/{}/'.format(ipServer,user))

print '<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.thor.com/cgi-bin/result.py?\">\n'



