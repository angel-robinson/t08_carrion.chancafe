# operaciones de cadena embebidas en python
# ejemplo 01
msg="se humilde PARA admitIr tus errORES"
print(msg.lower())
# retorna: se humilde para admitir tus errores

# ejemplo 02
tetx="si no luchas por lo que amas, no llores por lo que pierdes"
print(tetx.upper())
# retorna:SI NO LUCHAS POR LO QUE AMAS, NO LLORES POR LO QUE PIERDES

# ejemplo 03
msf="     ama la vida que tienes"
print(msf.strip())
# retorna:ama la vida que tienes

# ejemplo 04
con="somo polvo cosmico tratando de entender el tiempo              "
print(con.lstrip())
#retorna:somo polvo cosmico tratando de entender el tiempo

# ejemplo 05
hop="SOMOS/VICTIMA/DE/NUESTRA/CRUEL/IMAGINACION"
print(hop.split("/"))
#retorna:'SOMOS', 'VICTIMA', 'DE', 'NUESTRA', 'CRUEL', 'IMAGINACION'

# ejemplo 06
text="yo tengo 18 años"
print(text.split(","))
#retorna: 'yo tengo 18 años'

# ejemplo 07
ter="mi amigo tiene 23 años"
print(ter.isdigit())
# retorna:Falso

# ejemplo 08
numero="192022"
print(numero.isdigit())
# retorna: True

# ejemplo 09
per="PROGRAMACION, TECNICAS, MATEMATICA"
print(per.lower().split("."))
#retorna:'programacion, tecnicas, matematica'

# ejemplo 10
msg="CADA quie ES dueño DE su SIlenCio"
print(msg.lower().upper())
# retorna:CADA QUIE ES DUEÑO DE SU SILENCIO

# ejemplo 11
tex="eres dificil de encontrar"
print(tex.upper().split(" "))
#retorna:'ERES', 'DIFICIL', 'DE', 'ENCONTRAR'

# ejemplo 12
que="             es complicado verte          "
print(que.strip().upper())
#retorna:ES COMPLICADO VERTE

# ejemplo 13
dni="74286615"
print(dni.isdigit())
#retorna: True

# ejemplo 14
text=input("ingrese nombre:")
print(text.upper())
#retorna:ANGEL

# ejemplo 15
ape=input("ingrese primer apellio:") # si ingreso: carrion==> reotorna= Carrion
print(ape.upper()[0:1]+ape[1:])
