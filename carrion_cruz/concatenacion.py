# concatenacion
# ejemplo 01
nombre="angel carrion"
print("hola"+" "+nombre)            # seconcatena: hola angel carrion

# ejemplo 02
text="==>"+"estas hermosa"           # se concatena: hey, tu
print("hey, tu"+"\n"+text)           #               ==> estas hermosa

# ejemplo 03
mes1="me gusta ir a jugar futbol"
msg2="\n"+"a mi tambien me gusta lo mismo"      # se concatena: me gusta ir a jugar futbol
print(mes1+msg2)                                #             a mi tamnbien me gusta lo mismo

# ejemplo 04
text="quieres ser mi amiga:"                    # se concatena: ¿quieres ser mi amiga?
text1=" si"                                     #               >> si si si
print(text+"\n"+" >>" +text1*3)

# ejemplo 05
t="deseas tequila"                              # se concatena: deseas tequila
print(t+" "+"\n"+"si, gracias")                 #               si, gracias

# ejemplo 06
m="# hola"                                      # se concatena: # hola
n="# hola, como estas"                          #               # hola, como estas
m1="# bien, y tu"                               #               # bien, y tu
print(m+"\n"+n+"\n"+m1)

# ejemplo 07
print("desde mucho tiempo se practica la"+" "+"programacion")# se concatena :desde mucho tiempo se practica la programacion

# ejemplo 08
mis="="*3+"princesa"
print("hola"+"\n"+mis)                           # se concatena: hola
                                                 #              ===princesa

# ejemplo 09
met="bienvenido"                                # se concatena: bienvenido
sis=" gracias"                                   #              >> gracias
print(met+"\n"+">>"+sis)

# ejemplo 10
tet="¿puedes salir?"
lo="\n" +"lo siento no puedo"                   #se concatena: ¿puedes salir?
print(tet+lo)                                   #              lo siento no puedo

# ejemplo 11
print("me gusta "+ "tu carita bebe")            # se concatena: me gusta tu carita bebe

# ejemplo 12
ejm=":3"
tes=":("
print(ejm+"\r"+tes*4)                             # se concatena: :(:(:(:(

# ejemplo 13
pes="te toca jugar"                              # se conatena: te toca jugar, o ya no quieres jugar
pos=", o ya no quieres jugar"
print(pes+pos)

# ejemplo 14
pr="soy de peru"                                 # se concatena: soy de peru ¿y tu?
pt="¿y tu?"                                      #               yo soy de argentina
ch="yo soy de \'argentina\'"
print(pr+" "+pt+"\n"+ch)

# ejemplo 15
msg=input("ingrese nombre:")                    # se convatena: YO SOY, (NOMBRE)
tem="YO SOY, "
print(tem+msg.upper())