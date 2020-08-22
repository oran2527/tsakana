#!/usr/bin/python3

text = ''
indice = ''

while text == '':
    print("por favor ingrese un mensaje en letras mayusculas.\n\
    En caso contrario, se hara el cambio a mayusculas")
    text = input()        

while indice == '':
    print("Por favor ingrese un numero entero entre -27 y 27.\n\
    Este numero sera el desplazamiento segun el alfabeto")
    indice = input()    
    for i in indice:                
        if i == '.':            
            indice = ''            
    if indice != '':
        if abs(int(indice)) > 27:
            indice = ''        

print()

for i in text.upper():
    if ord(i) >= 65 and ord(i) <= 90:
        val = ord(i) + int(indice)    
        if val < 65:
            val = 91 - (65 - val)
        if val > 90:
            val = 64 + (val - 90)
    else:
        val = ord(i)                    
    print(chr(val), end="")

print()