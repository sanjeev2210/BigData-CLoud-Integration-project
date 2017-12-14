#!/usr/bin/python2

import cgi

import mysql.connector as mariadb




print "Content-Type: text/html"
print

db=mariadb.connect(user='root',password='1',database='lw')




print'''
<!DOCTYPE>
<html>
<head>
<title>Login Here</title>
<style>
div.topleft{
	position:relative;
	float:left;
	width:50%;
	height:110px;
	font-family:Georgia;
	color:white;
	padding-top:20px;
	left:40px;
}
div.logport{
	width:40%;
	text-align:center;
	position:relative;
	height:200px;
	margin-bottom:70px;
	border-radius:4px;
}
td.key{
	font-size:25px;
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
div.foot{
	background:black;
	width:100%;
	position:relative;
	top:200px;
	height:200px;
}
div.part{
	float:left;
	position:relative;
	
}
</style>
</head>
<body style="background-color: black;">
<div class="topleft">
<div style="position:relative;float:left;bottom:10px;"><a href="http://www.thor.com" style="text-decoration:none;color:white;"><img src="http://www.thor.com/images/logo.png" width=90px height=100px/></div><div style="position:relative;float:left;"><font style="font-size:40px;"><b>THOR</b></font></a></div>
</div>
<div style="position:relative;top:115px;background:white;width:100%;height:500px;">
<center>
<div class="logport">
<center>
<form method="POST" action="http://www.thor.com/cgi-bin/signin.py">
<fieldset style="border-radius:4px;margin:10px;border:3px groove;padding : 10px;">
<legend><h2>Login Here :</h2></legend>
<table>
<tr>
<td class="key">Username</td> 
<td><input class="in" placeholder="enter username" name="name" size="30" type="text"></td>
</tr>
<tr>
<td class="key">Password</td>
<td><input class="in" placeholder="enter password" type="password" size="30" name="password"></td>
</tr>
<tr>
<td colspan="2"><center>
<input type="submit" value="Login" style="width:120px;height:40px;color:blue;font-size:25px;background:lightgrey;border-radius:4px;"><b></b></center>
</td>
<td></td>
</tr>
</table>
</fieldset>
</form>
</center>
</div>
</div>
</center>


<div class="foot">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<div class="part">
<ul style="list-style-type:none;font-family:Copperplate Gothic;color:white;">
<li style="font-size:20px;"><b>Contact Us :</b></li><br />
<li style="font-size:15px;">National Institute of Technology,Patna</li>
<li style="font-size:15px;">Ashok Rajpath,Mahendru</li>
<li style="font-size:15px;">Patna,Bihar-800005</li>
</ul>
</div>
<div class="part">
<ul style="list-style-type:none;font-family:Copperplate Gothic;color:white;">
<li style="font-size:22px;"><b>Our Policy :</b></li><br />
<li style="font-size:15px;">General Policy</li>
<li style="font-size:15px;">Refund Policy</li>
<li style="font-size:15px;">Pricing Policy</li>
</ul>
</div>
<div class="part">
<ul style="list-style-type:none;font-family:Copperplate Gothic;color:white;">
<li style="font-size:22px;"><b>Connect us :</b></li><br />
<li style="font-size:15px;">Facebook</li>
<li style="font-size:15px;">Twitter</li>
<li style="font-size:15px;">Youtube</li>
</ul>
</div>
</div>



</body>
</html>
'''


name=cgi.FormContent()['name'][0]
passwd=cgi.FormContent()['password'][0]

str_user='{}:{}'.format(name,passwd)
fh=open('/var/www/cgi-bin/user_log','w')
fh.write(str_user)
fh.close


try:
	cursor=db.cursor()
	cursor.execute("select password from user where name=%s",(name,))
	row=cursor.fetchone()
finally:
	cursor.close()

db.close()


if passwd==row[0]:
	
	print '<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.thor.com/cover.html\">\n'

else:
	print '<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.thor.com/cgi-bin/signin.py\">\n'


