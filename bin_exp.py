def bin_exp(input_base, input_exponente, input_resultado ):
    base = input_base
    exponente = input_exponente
    resultado = input_resultado
    
    if exponente == 0:
        return 1
    elif exponente % 2 == 0:
        base *= base
        exponente = exponente / 2
        return bin_exp(base, exponente, resultado)
    elif exponente % 2 != 0:
        if exponente == 1:
            resultado = resultado * base
            return resultado
        else:
            resultado = resultado * base
            base *= base
            exponente = (exponente -1 ) / 2
            return bin_exp(base, exponente, resultado)
    else: "si"
            
    
    
    
    
print(bin_exp(2,12,1))