import time as t
import libOpenClient as loc

oc = loc.libOpenClient('200.128.140.12')
#oc.escreve_le_cart( 345.465 , -609.542 , 1074.0 , 0.0 , 180.0 , 0.0 )
print('OK')

def movelinear(posfin, velocity):
    pos = oc.le_cart()

    passo = 0.1
    
    while True:
        
        #print("X: " + str(pos.x) + "\tY: " +  str(pos.y) + "\tZ: " +  str(pos.z) + "\ta: " +  str(pos.a) + "\te: " +  str(pos.e) + "\tr: " +  str(pos.r) )
        coordenadas_Cartesianas = oc.le_cart()
        print("X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r) )

        pos.x = pos.x + passo
        pos.y = pos.y + passo
        pos.z = pos.z + passo

        oc.escreve_le_cart( pos.x , pos.y , pos.z , pos.a , pos.e , pos.r )

        t.sleep(0.01)

        if(pos.z > (posfin.z-5)):
            passo = 0.01

        if(pos.z > (posfin.z-0.2)):
            break

target = loc.cordCart()

target.x = 800.0
target.y = -1000.0
target.z = 1100.0
target.a = -30.0
target.e = 60.0
target.r = 90.0




#oc.escreve_le_cart( 345.465 , -609.542 , 823.960 , 0.0 , 180.0 , 0.0 )
#t.sleep(2)
# print("Posição Inicial: ")
# coordenadas_Cartesianas = oc.le_cart()
# print(f"\n\n X: {coordenadas_Cartesianas.x} \t Y: {coordenadas_Cartesianas.y} \t Z: {coordenadas_Cartesianas.z} \t a: {coordenadas_Cartesianas.a} \t e: {coordenadas_Cartesianas.e} \t r: {coordenadas_Cartesianas.r}\n\n")

# movelinear(target, 50)

# t.sleep(2)

print('FINAL:')
coordenadas_Cartesianas = oc.le_cart()
print(f"\n\n X: {coordenadas_Cartesianas.x} \t Y: {coordenadas_Cartesianas.y} \t Z: {coordenadas_Cartesianas.z} \t a: {coordenadas_Cartesianas.a} \t e: {coordenadas_Cartesianas.e} \t r: {coordenadas_Cartesianas.r}\n\n")

while(True):
    print('\n\n.')
    t.sleep(1)