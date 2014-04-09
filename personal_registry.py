#!/usr/bin/env/python
# -*- coding: UTF-8 -*-

import cgi
import cgitb
import sys, os
import MySQLdb
cgitb.enable()

print "Content-Type: text/html;charset=utf-8"

form = cgi.FieldStorage()


print """
<html>
	<title>J&N | Music Requests</title>
	<link href='http://fonts.googleapis.com/css?family=Fredericka+the+Great' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=Alex+Brush' rel='stylesheet' type='text/css'>
	<style>
		body {background-image:url('images/Nicole&Jeff_59.jpg'); background-attachment:fixed; background-repeat:no-repeat;background-position:center; background-size: cover;}
		div.main {margin-left: auto; margin-right: auto; width:50%; margin-top:0px;}
		div.show {/*background-color: #F0F8FF*/; margin-left: auto; margin-right: auto; width:55%; margin-top:50px; background-color: rgba(94, 94, 94, 0.6); border-radius:15px; <!--position: relative; top:-30px;-->}
		.text {font-family: Gill Sans, sans-serif; color: white;}
		.nav{
			border:1px solid #ccc;
			border-width:1px 0;
			list-style:none;
			margin:0;
			padding:0;
			text-align:center;
			<!--position:relative;
			top:-40px;-->
			clear:both;
			background-color: rgba(192, 192, 192, 0.6);/*gray*/
		}
		.nav li{
			display:inline;
		}
		.nav a{
			display:inline-block;
			padding:20px;
			font-family: Gill Sans, sans-serif;
			font-weight: bold; 
			color: black;
			opacity:1.0;
		}
		
		.nav a:link {text-decoration:none;}
		.nav a:visited {text-decoration:none;}
		.nav a:hover {text-decoration:underline;}
		.nav a:active {text-decoration:overline; }
		div.banner {
			position:absolute;
			top:50%;
			left:50%;
		}
		.names {
			width:100%;
			font-family: 'Fredericka the Great', cursive;
			color: white;
			font-size: 100px;
			vertical-align: text-bottom;
		}
		.dottedline {
			border-bottom: 2px dashed white;
		}
		.shadow {
			-moz-box-shadow:    1px 1px 2px 3px #ccc;
			-webkit-box-shadow: 1px 1px 2px 3px #ccc;
			box-shadow:         1px 1px 2px 3px #ccc;
		}
	</style>
	
	<body class="dottedline" style="padding:0;">
			<!--<img src="images/centralpark_text2.jpg" alt="We've messed up :(" style="width: 100%; height: 300px; float:bottom; border-radius:15px;" />-->
		<ul class="nav">
			<li><a href="ourstory.html">Our Story</a></li>
			<li>|</li>
			<li><a href="ceremony_and_reception.html">Ceremony & Reception</a></li>
			<li>|</li>
			<li><a href="photos.html">Our Photos</a></li>
			<li><a href="index.html" style="padding: 0%;"><img src="images/jandn_small.png" style="vertical-align: middle; opacity:0.6;"/></a></li>
			<li><a href="registry.html">Our Registry</a></li>
			<li>|</li>
			<li><a href="accommodations.html">Accommodations</a></li>
			<li>|</li>
			<li><a href="music.py">Music Requests</a></li>
		</ul>
		<div class="dottedline">&nbsp;</div>
		<div class="show">
			<div style="padding:10px;">
			<span class="text" style="font-size:40px; font-family: 'Alex Brush', cursive;"><strong>Music Requests</strong></span>
				<div style="padding-left:20px; padding-right:20px;">
				<br/>
"""

try:
	conn = MySQLdb.connect (
	host = "jeffbrunsek.netfirmsmysql.com",
	user = "brunzer",
	passwd = "123456",
	db = "wedding")
			
	mysql = conn.cursor()
	mysql.execute("""SELECT * FROM registry""")
	fields=mysql.fetchall()

	print "<table border='1' width='100%' class='text' cellpadding='3' cellspacing='3'><tr><th>Item</th><th>Store</th><th>Quantity</th><th>Recieved</th><th>Link</th></tr>"
	print "<tbody>"
	for field in fields:
		item = field[1]
		store = field[2]
		link = field[3]
		image = field[4]
		bought = field[5]
		quantity = field[6]
		print """
		<tr><td>
			<img src=%s height='100px'/><span class='text'>   %s</span>
		</td><td >
			<span class='text'>%s</span>
		</td><td >
			<span class='text'>%d</span>
		</td><td >
			<span class='text'>%d</span>
		</td><td >
			<span class='text'><a href=%s class='text' target=_blank >View</a></span>
		</td></tr>
"""	% (image, item, store, quantity, bought, link)
	
	print "</tbody>"
	print "</table>"
	
	mysql.close()
	conn.close()
	
except MySQLdb.Error, e:
	print "ERROR!! ERROR!!"
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit (1)

print """
				</table>
				</div>
			</div>
		</div>
	</body>
</html>
"""