import socket

class cordCart:
	x=0.0
	y=0.0
	z=0.0
	a=0.0
	e=0.0
	r=0.0

class cordJunta:
	j1=0.0
	j2=0.0
	j3=0.0
	j4=0.0
	j5=0.0
	j6=0.0


class libOpenClient:
	socketClient = 0
	
	def __init__(self, ipServidor='localhost', porta=54000):
		# Criando um socket TCP/IP
		global socketClient
		socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#, socket.SOCK_NONBLOCK)
		# Conectando ao servidor
		print('Tentando conectar a ' + ipServidor + ' através da porta ' + str(porta))
		socketClient.connect((ipServidor,porta))
		#socketClient.setblocking(0)
	
	def __del__(self):
		global socketClient
		print('Fechando socket')
		socketClient.close()
	
	def envia_msg(self, msg):
		global socketClient
		socketClient.sendall(str.encode(msg))
	
	def recebe_msg(self):
		global socketClient
		mensagemCompleta = b''
		while True:
			msg_byte = socketClient.recv(1)
			if (msg_byte==b'\x00'):
				return mensagemCompleta.decode('UTF-8')
			else:
				mensagemCompleta += msg_byte
			
	def le_cart(self):
		self.envia_msg('cl')
		msg = self.recebe_msg()
		msg = msg.split(" ")
		saida = cordCart()
		saida.x = float(int(msg[0]))/1000
		saida.y = float(int(msg[1]))/1000
		saida.z = float(int(msg[2]))/1000
		saida.a = float(int(msg[3]))/1000
		saida.e = float(int(msg[4]))/1000
		saida.r = float(int(msg[5]))/1000
		return saida
	
	def le_junta(self):
		self.envia_msg('jl')
		msg = self.recebe_msg()
		msg = msg.split(" ")
		saida = cordJunta()
		saida.j1 = float(int(msg[0]))/1000000
		saida.j2 = float(int(msg[1]))/1000000
		saida.j3 = float(int(msg[2]))/1000000
		saida.j4 = float(int(msg[3]))/1000000
		saida.j5 = float(int(msg[4]))/1000000
		saida.j6 = float(int(msg[5]))/1000000
		return saida

	def escreve_le_cart(self,x,y,z,a,e,r):
		self.envia_msg('c ' + str(int(x*1000)) + ' ' + str(int(y*1000)) + ' ' + str(int(z*1000)) + ' ' + str(int(a*1000)) + ' ' + str(int(e*1000)) + ' ' + str(int(r*1000)))
		msg = self.recebe_msg()
		msg = msg.split(" ")
		saida = cordCart()
		saida.x = float(int(msg[0]))/1000
		saida.y = float(int(msg[1]))/1000
		saida.z = float(int(msg[2]))/1000
		saida.a = float(int(msg[3]))/1000
		saida.e = float(int(msg[4]))/1000
		saida.r = float(int(msg[5]))/1000
		return saida

	def escreve_le_junta(self,j1,j2,j3,j4,j5,j6):
		self.envia_msg('j ' + str(int(j1*100000)) + ' ' + str(int(j2*100000)) + ' ' + str(int(j3*100000)) + ' ' + str(int(j4*100000)) + ' ' + str(int(j5*100000)) + ' ' + str(int(j6*100000)))
		msg = self.recebe_msg()
		msg = msg.split(" ")
		saida = cordJunta()
		saida.j1 = float(int(msg[0]))/100000
		saida.j2 = float(int(msg[1]))/100000
		saida.j3 = float(int(msg[2]))/100000
		saida.j4 = float(int(msg[3]))/100000
		saida.j5 = float(int(msg[4]))/100000
		saida.j6 = float(int(msg[5]))/100000
		return saida



##### EXEMPLO cartesiano

#import libOpenClient as loc
#oc = loc.libOpenClient()
#oc.escreve_le_cart( 797.07 , 0.0 , 1075.0 , 0.0 , 0.0 , 0.0 )
#coordenadas_Cartesianas = oc.le_cart()
#print("X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r) )


##### EXEMPLO junta

#oc = libOpenClient('localhost')
#oc.escreve_le_junta(0,0,-90,0,90,0)
#coordenadas_Juntas = oc.le_junta()
#print("J1: " + str(coordenadas_Juntas.j1) + "J2: " + str(coordenadas_Juntas.j2) + "J3: " + str(coordenadas_Juntas.j3) + "J4: " + str(coordenadas_Juntas.j4) + "\tJ5: " +  str(coordenadas_Juntas.j5) + "J6: " + str(coordenadas_Juntas.j6))

