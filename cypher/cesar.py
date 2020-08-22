#!/usr/bin/python3

text = ''
indice = ''

while text == '':
    print("por favor ingrese un mensaje en letras mayusculas.\n\
    En caso contrario, se hara el cambio a mayusculas")
    text = input()        

while indice == '':
    print("por favor ingrese un numero entero\n\
    Este numero sera el desplazamiento segun el alfabeto")
    indice = input()    
    for i in indice:        
        if i == '.':
            indice = ''
print()

for i in text.upper():
    val = ord(i) + int(indice)    
    if val < 65:
        val = 91 - (65 - val)
    if val > 90:
        val = 64 + (val - 90)            
    print(chr(val), end="")

print()