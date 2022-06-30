import libOpenClient as loc
import time as t

oc = loc.libOpenClient('200.128.140.15')

oc.escreve_le_cart( 100.0 , 100.0 , 100.0 , 0.0 , 90.0 , 0.0 )

t.sleep(2)

coordenadas_Cartesianas = oc.le_cart()
print("X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r) )
