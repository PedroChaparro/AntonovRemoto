carga = float(input("Ingrese la carga, en kg, que hay en el avión en este momento: "))

#Si la carga que hay en el avión antes de subir el paquete es mayor o igual a 237500, ya se superó el límite de carga

nuevo = "Si"

while nuevo == "Si": 

    if carga >= 237500:
        print("Ya se ha superado el límite de carga, NO SE RECIBEN MÁS PAQUETES")
        break
    else:
        peso = float(input("Ingrese el peso del paquete que se quiere enviar: "))
    
        if peso < 10:
            print("Lo sentimos, el peso del paquete no es aceptable: ")
        else:
            carga = carga + peso 
        
            if carga >= 237500:
                print("Al subir este paquete, se superaría el límite de carga, SE RECOMIENDA NO RECIBIRLO")
                break
            else:

                tipo = str(input("Ingrese el tipo de envío, puede ser Nacional o Intercontinental: "))
                #Se pone la primera letra en mayúscula por defecto, para evitar errores
                tipo = tipo.title()

                distancia = float(input("Ingrese la distancia, en Km que recorrerá el paquete: "))

                if tipo == "Nacional":
                    sin_descuento = (4500*peso) + (4000 * distancia)
                else:
                    sin_descuento = (4500*peso) + ((8000 * distancia)/1.60934)
            
                #CALCULAR DESCUENTOS:

                if peso > 100 and tipo == "Nacional":
                    descuento = sin_descuento * 0.15

                elif peso > 400 and tipo == "Intercontinental" and distancia > 8000:
                    descuento = sin_descuento * 0.1

                else:
                    descuento = 0

                pagar = sin_descuento - descuento
                pagar = int(pagar)

                print("El precio a pagar por un envío {}, de {} km con peso {} kg es: {}".format(tipo, distancia, peso, pagar))

                nuevo = str(input("¿Desea calcular otro envío, digite Si o No: "))
                nuevo = nuevo.title()

