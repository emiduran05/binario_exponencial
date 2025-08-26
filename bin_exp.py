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
    
    
    
    
print(bin_exp(2,12,1)) #base, exponente, y el resultado siempre se inicializa en 1
print(pow(2,12)) #Da el mismo resultado usando la funcion pow()