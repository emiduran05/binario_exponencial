def bin_exp(base, exponente, resultado ): 
       
    if exponente == 0:
        return 1
    elif exponente % 2 == 0:
        return bin_exp(base *base, exponente/2, resultado)
    
    elif exponente % 2 != 0:
        
        if exponente == 1:
            return resultado * base
        else:
            return bin_exp(base * base, (exponente -1)/2, resultado *base)
        
    else: 
        return "numero no valido"  
    
    
    
    
print("Funcion con recursividad: ", bin_exp(2,12,1), ", Función con Pow: ", pow(2,12)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(2,10,1), ", Función con Pow: ", pow(2,10)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(2,2,1), ", Función con Pow: ", pow(2,2)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(3,10,1), ", Función con Pow: ", pow(3,10)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(4,15,1), ", Función con Pow: ", pow(4,15)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(5,3,1), ", Función con Pow: ", pow(5,3)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(3,9,1), ", Función con Pow: ", pow(3,9)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(6,10,1), ", Función con Pow: ", pow(6,10)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(8,18,1), ", Función con Pow: ", pow(8,18)) #base, exponente, y el resultado siempre se inicializa en 1
print("Funcion con recursividad: ", bin_exp(4,6,1), ", Función con Pow: ", pow(4,6)) #base, exponente, y el resultado siempre se inicializa en 1




