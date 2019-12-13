# busqueda
# ejemplo 01
#              1         2
#    012345678901234567890123456789
mtr="EL MARAVILLOSO MUNDO DE MARVEL"
print(mtr.find("MARVEL"))                       # resulatado: 24
print(mtr.index("MARVEL"))                       # resulatado: 24
print(mtr.index("EL"))                       # resulatado: 0

# ejemplo 02
#    012345678901234567890123456789
msg="FIESTA CACHIMBOS"
print(msg.index("FIESTA"))                       # resulatado: 0
print(msg.find("S"))                       # resulatado: 3
print(msg.find("F"))                       # resulatado: 0

# ejemplo 03
#     01234567890123456789
text="los vengadores"
print(text.index("vengad"))                       # resulatado: 4
print(text.find("s"))                       # resulatado: 2

# ejemplo 04
#     01234567890123456789
text="batman regresa"
print(text.index("b"))                       # resulatado: 0
print(text.find("a"))                       # resulatado: 1

# ejemplo 05
#     01234567890123456789
text="el peru es maravilloso"
print(text.index("o"))                       # resulatado: 19
print(text.find("peru"))                       # resulatado: 3

# ejemplo 06
#     01234567890123456789
text="el rio mas grande es el amazonas"
print(text.index("amazonas"))                       # resulatado: 24
print(text.find("r"))                       # resulatado: 3

# ejemplo 07
#     01234567890123456789
text="las siete maravillas del mundo"
print(text.index("siete"))                       # resulatado: 4
print(text.find("mundo"))                       # resulatado: 25

# ejemplo 08
#     01234567890123456789
text="contaminaciom ambiental"
print(text.index("tal"))                       # resulatado: 20
print(text.find("no"))                       # resulatado: -1

# ejemplo 09
#     01234567890123456789
text="barcelona es el mejor equipo del mundo"
print(text.index("undo"))                       # resulatado: 34
print(text.find("ona"))                       # resulatado: 6

# ejemplo 10
#     01234567890123456789
text="mis mayores sueños son lograr mis metas"
print(text.index("tas"))                       # resulatado: 36
print(text.find("is"))                       # resulatado: 1

# ejemplo 12
#     01234567890123456789
text="la mejor comida es de peru"
print(text.index("ida"))                       # resulatado: 12
print(text.find("or"))                       # resulatado: 6

# ejemplo 04
#     01234567890123456789
text="mis mas sentido pesame"
print(text.index("esa"))                       # resulatado: 17
print(text.find("pe"))                       # resulatado: 16

# ejemplo 04
#     01234567890123456789
text="dios del trueno"
print(text.index("dios"))                       # resulatado: 0
print(text.find("el"))                       # resulatado: 6

# ejemplo 04
#     01234567890123456789
text="la distancia no importa"
print(text.index("orta"))                       # resulatado: 19
print(text.find("la"))                       # resulatado: 0

# ejemplo 11
#     01234567890123456789
text="\'chile, pais hermano\'"
print(text.index(","))                       # resulatado: 6
print(text.find("\'"))                       # resulatado: 0
