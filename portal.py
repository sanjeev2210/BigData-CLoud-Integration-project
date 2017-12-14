#!/usr/bin/python2

import cgi
import commands


import mysql.connector as mariadb


print "Content-Type: text/html"
print 

db=mariadb.connect(user='root',password='1',database='lw')

val=commands.getstatusoutput('sudo cat /var/www/cgi-bin/user_log')
user=val[1].split(':')[0]
passwd=val[1].split(':')[1]

print'''
<!DOCTYPE>
<html>
<head>
<title>THOR Portal</title>
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
ul#nav {
    list-style-type: none;
    margin-top: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333333;
}

li.n {
    float: left;
}

li.n a {
    display: block;
    color: white;
    text-align: center;
    padding: 16px;
    text-decoration: none;
}

li.n a:hover {
    background-color: #111111;
}

.dropbtn {
    background-color: #333333;
    color: white;
    padding: 16px;
    font-size: 20px;
    border: none;
    cursor: pointer;
}

.dropbtn:hover, .dropbtn:focus {
    background-color: #3e8e41;
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    overflow: auto;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown a:hover {background-color: #111111;}

.show {display:block;}
div.dash{
	width:80%;
	height:500px;
	
	margin-left:50px;
}
</style>
<script>
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
</script>
</head>
<body style="background-color: black;">
<div class="topleft">
<div style="position:relative;float:left;bottom:10px;"><a href="http://www.thor.com" style="text-decoration:none;color:white;"><img src="http://www.thor.com/images/logo.png" width=90px height=100px/></div><div style="position:relative;float:left;"><font style="font-size:40px;"><b>THOR</b></font></a></div>
</div>
<div style="position:relative;top:115px;background:white;width:100%;height:700px;">
<div style="width:100%; height:200px;float:left;">
<div style="position:relative;float:left;">
<ul id="nav">
  <li class="n"><a href='http://www.thor.com/hadoop.html' target='main'>Create a Cluster</a></li>
  <li class="n"><a href='http://www.thor.com/cgi-bin/upload.py' target='main'>Put a File</a></li>
  <li class="n"><a href='http://www.thor.com/cgi-bin/run.py' target='main'>Run Mapper-Reducer</a></li>
  <li class="n"><a href='http://www.thor.com/cgi-bin/dash.py' target='main'>Dashboard</a></li>
</ul>
</div>
<div class="dropdown" style="float:right;right:80px;">
<button onclick="myFunction()" class="dropbtn"><b>Hii, 
'''
print user 
print '''
</b></button>
  <div id="myDropdown" class="dropdown-content">
    <a href='http://www.thor.com/cgi-bin/logout.py'>Logout</a>
  </div>
</div>
</div>

<div class="dash">

<iframe width="100%" height="600px" style="border:0px;" name="main">

</iframe>

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

