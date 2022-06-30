import libOpenClient as loc
import time as t

oc = loc.libOpenClient('200.128.140.12')

def movelinear(posfin, steps):

    #Le a posição atual do robô (inicio):
    pos = oc.le_cart()

    #Calcula os steps em cada eixo:
    step_x = float((posfin.x - pos.x)/float(steps))
    step_y = float((posfin.y - pos.y)/float(steps))
    step_z = float((posfin.z - pos.z)/float(steps))

    #Declara como nao alcancadas as posicoes nos tres eixos:
    reach_x = False
    reach_y = False
    reach_z = False

    #Booleana de suavizacao final do movimento:
    smooth = True

    while(True):

        #Delay para compensar atrasos em cada passo:
        t.sleep(0.1)

        #Le e imprime a posicao atual do robo, a cada iteracao:
        coordenadas_Cartesianas = oc.le_cart()
        print("X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r) )

        #Verifica se a posicao em cada eixo foi atingida: caso não, haverá incremento na direcao, se nao, o incremento para e a direcao e declarada como alcancada:
        if(abs(posfin.x-pos.x) >= 0.005):
            pos.x = pos.x + step_x
        else:
            reach_x = True
        if(abs(posfin.y-pos.y) >= 0.005):
            pos.y = pos.y + step_y
        else:
            reach_y = True
        if(abs(posfin.z-pos.z) >= 0.005):
            pos.z = pos.z + step_z
        else:
            reach_z = True    

        #Escreve o novo vetor posicao com os devidos incrementos em cada eixo:
        oc.escreve_le_cart( pos.x , pos.y , pos.z , 0.0 , 90.0 , 0.0 )

        #Suaviza o movimento, reduzindo a velocidade em 10 vezes, nos ultimos 10mm:
        if(((abs(posfin.x-pos.x) < 10) or (abs(posfin.y-pos.y) < 10) or (abs(posfin.z-pos.z) < 10)) and smooth):
            step_x = float(step_x/10.0)
            step_y = float(step_y/10.0)
            step_z = float(step_z/10.0)
            smooth = False

        #Encerra o looping, quando o robo atinge sua posicao final, nos tres eixos:
        if(reach_x and reach_y and reach_z):
            break



##################################################################################################################


#Parametros externos:
x1 = 998.528
y1 = -198.214
x2 = 986.234
y2 = 209.599
zmesa = 223.317
hcopo = 97.0

#Definicoes:
z1n = (zmesa + (hcopo/2.0))
z1p = (zmesa + hcopo)
z2n = (zmesa + (hcopo*(3.0/2.0)))
z2p = (zmesa + (2.0*hcopo))
zseg = (zmesa + (2.5*hcopo))




#Vetor de posicao home do robo:
homepos = loc.cordCart()
homepos.x = 895.875
homepos.y = 3.448
homepos.z = 1170.490
homepos.a = 0.178
homepos.e = 88.779
homepos.r = 3.683

#Prestes a pegar o copo:
p1 = loc.cordCart()
p1.x = (x1-100)
p1.y = y1
p1.z = z1n

#Encaixa no copo em x1,y1:
p2 = loc.cordCart()
p2.x = x1
p2.y = y1
p2.z = z1n

#Pega o copo:
p3 = loc.cordCart()
p3.x = x1
p3.y = y1
p3.z = z1p

#Subir 3hcopo:
p4 = loc.cordCart()
p4.x = x1
p4.y = y1
p4.z = zseg

#Deslocar para x2,y2:
p5 = loc.cordCart()
p5.x = x2
p5.y = y2
p5.z = zseg

#Descer para 2hcopo:
p6 = loc.cordCart()
p6.x = x2
p6.y = y2
p6.z = z2p

#Soltar o copo:
p7 = loc.cordCart()
p7.x = x2
p7.y = y2
p7.z = z2n

#Afastar do copo:
p8 = loc.cordCart()
p8.x = (x2 - 100)
p8.y = y2
p8.z = z2n



#Movimentacao:
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
movelinear(homepos, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p1, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p2, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p3, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p4, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p5, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p6, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p7, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(p8, 10)
coordenadas_Cartesianas = oc.le_cart()
print("=> X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r))
t.sleep(3)
movelinear(homepos, 10)