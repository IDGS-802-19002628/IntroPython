num1 = 20
num2 = 4

print("La suma es: ", (num1 + num2))
print("La resta es: ", (num1 / num2))
print("La multiplicacion es: ", (num1 * num2))
print("La division es: ", (num1 / num2))
print("La division exacta es: ", (num1 // num2))
print("La potencia es: ", (num1 ** num2))

# Concatetacion en python
texto1 = "Hola"
texto2 = "mundo"
textoFinal = texto1, " ", texto2
print(textoFinal)
print("EL saludo es %s %s" % (texto1, texto2))
saludoFinal1 = "Saludo {}{}".format(texto1, texto2)
print(saludoFinal1)
saludoFinal2 = "Saludo {x}{y}".format(x=texto1, y=texto2)
print(saludoFinal2)
