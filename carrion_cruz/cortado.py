# concatenacion
# ejemplo 01
#              1         2         3
#    012345678901234567890123456789012345678
msg="EL BUEN HOMBRE TIENE MUCHAS CUALIDADES"
print(msg[3:7]+msg[28:38])                          # se concatena: BUENCUALIDADADES

# ejemplo 02
#              1         2         3         4
#    012345678901234567890123456789012345678901234567
msg="NO PUEDO DEJAR DE PENSAR EN TI POR TODA LA NOCHE"
print(msg[3:8]+" "+msg[18:30])                         # se corta la cadena a: PUEDO PENSAR EN TI
print(msg[3:8]+" "+msg[35:])         # se corta la cadena a:PUEDO TODA LA NOCHE
print(msg[25:27]+" "+msg[40:]+" "+msg[:8])  # se corta la cadena a: EN LA NOCHE NO PUEDO

# ejemplo 03
#              1         2         3         4
#    012345678901234567890123456789012345678901234567
msg="SOY ROBINSON Y ESTUDIO INGENIERIA ELECTRONICA"
print(msg[:3]+" "+msg[34:])                 # se corta la cadena a: SOY ELECTRONICA
print(msg[15:22]+" "+msg[34:])              # se corta la cadena a: ESTUDIO ELECTRONICA
print(msg[23:26]+" "+msg[4:12])             ## se corta la cadena a: ING ROBINSON

# ejemplo 04
#              1         2
#     012345678901234567890123456 7
msg="\"LA PEDRO ME CAMBIO LA VIDA\""
print(msg[20:27]+", "+msg[1:9])               # se corta la cadena a: LA VIDA, LA PEDRO
print(msg[13:19]+" "+msg[1:9])              # se corta la cadena a: CAMBIO LA PEDRO
print(msg[::-1])                            # se corta la cadena a: "ADIV AL OIBMAC EM ORDEP AL"

# ejemplo 05
#              1         2         3         4         5         6
#    0123456789012345678901234567890123456789012345678901234567890123456789
msg="VIVE COMO SI FUERAS A MORIR MAÑANA, APREMDE COMO SI FUERA PARA SIEMPRE"
print(msg[:4]+" "+msg[28:34])               # se corta la cadena a: VIVE MAÑANA
print(msg[22:27]+" "+msg[58:])               # se corta la cadena a: MORIR PARA SIEMPRE
print(msg[36:43]+" "+msg[28:34]+"\n"+">> "+msg[63:])               # se corta la cadena a: APRENDE MAÑANA
#                                                                                          >> SIEMPRE


# ejemplo 06
#              1         2         3         4
#     0123456789012345678901234567890123 45678901234567
msg="\'NO HAY SUSTITUTO DEL TRABAJO DURO\'"
print(msg[30:34]+" "+msg[8:17])               # se corta la cadena a: DURO SUSTITUTO
print(msg[:7]+" "+msg[22:])               # se corta la cadena a: 'NO HAY TRABAJO DURO'
print(msg[4:7]+" "+msg[30:34]+" "+msg[8:17]) # se corta la cadena a: HAY DURO SUSTITUTO
# ejemplo 07
#              1         2         3         4
#    012345678901234567890123456789012345678901234567890123456789012345
msg="las matematicas son el alfabeto con el cual dios a creado al mundo"
print(msg[16:19]+" "+msg[4:15]+" "+msg[36:38]+" "+msg[61:])       # se corta la cadena a: son matematicas del mundo
print(msg[31:22:-1])               # se corta la cadena a: otefabla
print(msg[14:3:-1])                # se corta la cadena a: sacitametam
# ejemplo 08
#               1         2         3         4
#     012345678901234567890123456789012345678901234567 8
msg="\'LA MEJOR FORMA DE PREDECIR EL FUTURO ES CREARLO\'"
print(msg[38:40]+" "+msg[4:9]+" "+msg[28:37])# se corta la cadena a: ES MEJOR EL FUTURO
print(msg[37:18:-1])                        # se corta la cadena a: ORUTUF LE RICEDERP
print(msg[:1]+" "+msg[31:37]+" "+msg[48:])  # la cadena se corta a: ' FUTURO '
# ejemplo 09
#              1         2         3         4
#    012345678901234567890123456789012345678901234567
msg="las oportunidades no ocurren, las creas tú"
print(msg[27:20:-1]+" "+msg[16:3:-1])                     # la cadena se corta a: nerruco sedadinutropo
print(msg[18:20]+" "+msg[0:3]+" "+msg[34:42])                     # la cadena se corta a: no las creas tu
print(msg[16:3:-1])                     # la cadena se corta a: sedadinutropo

# ejemplo 10
#              1         2         3         4         5         6         7         8         9         1
#    0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901
msg="si no persigues lo que quieres nunca lo vas a lograr. si no vas hacia adelante siempre estaras en el mismo lugar"
print(msg[6:14]+msg[16:18]+" "+msg[54:56]+" "+msg[60:62]+" "+msg[64:78])# la cadena se corta a:persiguelo si va hacia adelante
print(msg[3:5]+" "+msg[23:30]+" "+msg[37:39])                     # la cadena se corta a:no quieres lo mismo
print(msg[79:94]+" "+msg[21]+msg[31]+" "+msg[101:103])                     # la cadena se corta a:simepre estaras en mi

# ejemplo 11
#               1         2         3         4
#     012345678901234567890123456789012345678901234567
msg="\"CADA LOGRO EMPIEZA CON LA INTENCION DE INTENTARLO\""
print(msg[12:19]+" "+msg[20:23]+" "+msg[1:5]+" "+msg[6:11])                     # la cadena se corta a:EMPIEZA CON CADA LOGRO
print(msg[-1:23:-1]+msg[0])                     # la cadena se corta a:"OLRATNETNI ED NOICNETNI AL"
print(msg[1:5]+" "+msg[14:19]+" "+msg[27:30]) # la cadena se corta a:CADA PIEZA INT

# ejemplo 12
#               1         2         3         4         5         6         7         8         9         1
#     01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890 1
msg="\"NO TE PREOCUPES POR LOS FRACASOS, PREOCUPATE POR LAS OPORTUNIDADES QUE PIERDES CUANDO NO LO INTENTAS\""
print(msg[0:3]+" "+msg[72:79]+"; "+msg[1:3]+" "+msg[4:16]+msg[101])# la cadena se corta a:"NO PIERDES; NO TE PREOCUPES"
print(msg[17:20]+" "+msg[25:33]+" "+msg[35:45])                     # la cadena se corta a:POR FRACASOS PREOCUPATE
print(msg[21:33]+" "+msg[87:99]+msg[77:79])                         # la cadena se corta a:LOS FRACASOS NO LO INTENTES

# ejemplo 13
#               1         2         3         4
#     01234567890123456789012345678901234567890123456789 0
msg="\'EL APRENDIZAJE NO ES UN DEPORTE PARA EXPECTADORES\'"
print(msg[0:3]+" "+msg[25:32]+" "+msg[19:21]+" "+msg[4:15]+" "+msg[50])       # la cadena se corta a:'EL DEPORTE ES APRENDIZAJE '
print(msg[33:50]+" "+msg[1:3]+" "+msg[25:32])  # la cadena se corta a:PARA EXPECTADORES EL DEPORTE

# ejemplo 14
#               1         2         3         4
#     012345678901234567890123456789012345678901234567890123456789
text="NO HAY ASCENSOR AL EXITO, TIENES QUE TOMAR LAS ESCALERAS"
print(text[31:25:-1]+" "+text[55:42:-1])  # la cadena se corta a:SENEIT SARELACSE SAL
print(text[0:6]+" "+text[19:24]+" "+text[16:18]+" "+text[37:42])  # la cadena se corta a:NO HAY EXITO AL TOMAR
print(text[37:42]+" "+text[52:50:-1]+" "+text[7:15]+" "+text[33:36]+" "+text[43:])  # la cadena se corta a:TOMAR EL ASCENSOR QUE LAS ESCALERAS

# ejemplo 15
#                1         2         3         4         5         6
#      0123456789012345678901234567890123456789012345678901234567890 1
text="\"ES IMPOSIBLE PARA UN HOMBRE APRENDER LO QUE CREE QUE YA SABE\""
print(text[50:53]+" "+text[22:28]+" "+text[4:13])  # la cadena se corta a:QUE HOMBRE IMPOSIBLE
print(text[0:1]+" "+text[38:40]+" "+text[4:13]+" "+text[29:36]+" "+text[19:28]+" "+text[61])  # la cadena se corta a:" LO IMPOSIBLE APRENDE UN HOMBRE "
print(text[54:56]+" "+text[45:49]+" "+text[4:13])  # la cadena se corta a:YA CREE IMPOSIBLE