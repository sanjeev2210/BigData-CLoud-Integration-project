#!/usr/bin/python2

import cgi

import Cookie

c=Cookie.SimpleCookie()

c['user']=''
c['user']['expires']='Thu, 01 Jan 1970 00:00:00 GMT'

print c

print 'Content-Type: text/html'
print 


print '''

<!DOCTYPE>
<html>
<head>
<title>Redirecting....</title>
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
<div style="position:relative;float:left;bottom:10px;"><img src="http://www.thor.com/images/logo.png" width=90px height=100px/></div><div style="position:relative;float:left;"><font style="font-size:40px;"><b>THOR</b></font></div>
</div>
<div style="position:relative;top:115px;background:white;width:100%;height:500px;">
<div style="position:relative;float:left;text-align:center;width:100%;height:200px;">
<a href="http://www.thor.com/cgi-bin/signin.py" style="text-decoration:none;color:blue;font-size:20px;"><b>You are successfully logged out....Click here to login..!!</b></a>
</div>
</div>

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
