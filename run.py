#!/usr/bin/python2

import cgi

import commands


print 'Content-Type: text/html'
print

ipServer='192.168.43.52'

val=commands.getstatusoutput('sudo cat /var/www/cgi-bin/user_log')
user=val[1].split(':')[0]

#clientName='{}-client'.format(user)

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
<form enctype="multipart/form-data" method="POST" action="http://www.thor.com/cgi-bin/run.py">
<h3>Mapper Reducer Job Submission:</h3>
<table>
<tr style="bottom:10px;">
<td>Mapper Program:</td>
<td><input type="file" name="fname" style="font-size:20px;"/></td>
</tr>
<tr>
<td colspan="2">
<input class="n" type="submit" value="Next..."/>
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





fh=open('/var/www/cgi-bin/uploads/map.py','w')
fh.write(fname)
fh.close()

print '<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.thor.com/cgi-bin/run_2.py\">\n'

