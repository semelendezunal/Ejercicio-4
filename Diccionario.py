#Sergio Alexander Melendez Rodriguez
# Imprimir de forma ascendente mismo tipo valores
dcto1 = {"contraseña":"343454", "12345":"545454", "alfredo":"46557756", "perrro_brian":"57676"}

valor_dcto1 = list(dcto1.values())

def orden_dcto1 (valor_dcto1):
    n = len (valor_dcto1)

    for i in range (n-1):
        for m in range (n-1-i):
            if valor_dcto1 [m] > valor_dcto1 [m+1]:
                valor_dcto1 [m], valor_dcto1 [m+1] = valor_dcto1 [m+1], valor_dcto1[m]

print ("diccionario ascendente", valor_dcto1)

#-----------------------------
#verifica clave:valor estan en otro diccionario

dcto2 = {"contraseña":"343454", "12345":"545454", "alfredo":"46557756", "perrro_brian":"57676"}
dcto3 = {"contraseña":"554555", "54321":"54784", "juan":"466565", "ayudante_de_santa":"57676"}


comprobar = True
for clave, valor in dcto2.items ():
    if clave not in dcto3 or dcto3[clave] != valor:
        comprobar = False
        break
if comprobar:
    print("Par valor:clave es igual en dcto2 como en dcto3")
else: 
    print("Par valor:clave no es totalmente igual en dcto2 como en dcto3")

#------------------------------------------------------
#recibe 2 diccionarios, mezcla. hace un nuevo diccionario con ello.

dcto5 = {"contraseña":"343454", "12345":"545454", "alfredo":"46557756", "perrro_brian":"57676"}
dcto6 = {"contraseña12345":"554555", "54321":"54784", "pedro":"466565", "ayudante_de_santa":"57676"}

def mezcla ( dcto5, dcto6):
    mezcla_dcto = dcto6.copy()

    mezcla_dcto.update(dcto5)

    return mezcla_dcto

dcto_5_6 = mezcla(dcto5, dcto6)
print ("Diccionario mezclado", dcto_5_6)

#------------------------
#nombres y apellidos