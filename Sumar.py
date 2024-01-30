import time
g = """
Instrucciones : 
El argumento A es el primer argumento
Y el Argumento B es el segundo argumento
Ejemplo
Argumento a 5
Argumento b 2
Ejemplo Argumento a + Argumento b       5+2
Respuesta = 7
"""
y = '''*IMPORTANTE SOLO USAR NUMEROS*
'''
print(g)
time.sleep(3)
print(y)
time.sleep(1)

a = int(input("Argumento a "))
b = int(input("Argumento b "))
c = a + b
print(f"El resultado es: {c}")
time.sleep(3)
print("By Irdomeriko")

time.sleep(3)
exit()