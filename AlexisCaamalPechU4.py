import re

expre1="\d+\s?\+\s?\d+"
expre2="\d+\s?\-\s?\d+"
expre3="\d+\s?\*\s?\d+"
expre4="\d+\s?\/\s?\d+"
expre5="[i]+\+[\+]?"
expre6="\d+\.?\d+"
expre7="[\+\-\*\/\%]"
expre8="\=[\=]|\![\=]|\<\=?|\>\=?"
expre9="decimal|byte|explicit|extern|else|class|default|base|case|false|enum|delegate|const|catch|abstract|bool|as"

print("- - - - - - - - - - - - - - - - - - - - - -")
print("Variables validad: suma, i, cont7, etc.")
exp = 'Valores.txt'
analizar = open(exp, "r")
senuno = re.compile(expre1)
sendos = re.compile(expre2)
sentres = re.compile(expre3)
sencuatro = re.compile(expre4)
sencinco = re.compile(expre5)
for imp in analizar:
    resultado = senuno.findall(imp)
    print(resultado)
    resultado = sendos.findall(imp)
    print(resultado)
    resultado = sentres.findall(imp)
    print(resultado)
    resultado = sencuatro.findall(imp)
    print(resultado)
    resultado = sencinco.findall(imp)
    print(resultado)
analizar.close()

print("- - - - - - - - - - - - - - - - - - - - - -")
print("Enteros y decimales: 2.7, 3.1416, 0.2, etc.")
exp = 'Valores.txt'
analizar = open(exp, "r")
senseis = re.compile(expre6)
for imp in analizar:
    resultado = senseis.findall(imp)
    print(resultado)
analizar.close()

print("- - - - - - - - - - - - - - - - - - - - - -")
print("Operadores aritméticos: suma, resta, multiplicación, división, etc.)")
exp = 'Valores.txt'
analizar = open(exp, "r")
sensiete = re.compile(expre7)
for imp in analizar:
    resultado = sensiete.findall(imp)
    print(resultado)
analizar.close()

print("- - - - - - - - - - - - - - - - - - - - - -")
print("Operadores relacionales: mayor, menor, igual, diferente, etc")
exp = 'Valores.txt'
analizar = open(exp, "r")
senocho = re.compile(expre8)
for imp in analizar:
    resultado = senocho.findall(imp)
    print(resultado)
analizar.close()

print("- - - - - - - - - - - - - - - - - - - - - -")
print("Palabras reservadas")
exp = 'Valores.txt'
analizar = open(exp, "r")
sennueve = re.compile(expre9)
for imp in analizar:
    resultado = sennueve.findall(imp)
    print(resultado)
analizar.close()




