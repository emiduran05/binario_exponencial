# binario_exponencial

El algoritmo binario exponencial es una manera de calcular el exponente de un determinado numero a través de operaciones más pequeñas pero equivalentes

Ejemplo (con pseudocódigo)

function bin_exp (input_base, input_exponente, input_resultado)
		base = input_base
		exponente = input_exponente
		resultado = input_resultado
	if exponente == 0
		return 1
	if exponente % 2 == 0 
		base *= base 
		exponente = exponente / 2
		bin_exp(base, exponente, resultado)
	if exponente % 2 == 1
		if exponente == 1
			resultado = resultado * base
			return resultado
		resultado = resultado * base 
		base *= base
		exponente = (exponente - 1) / 2
		bin_exp(base, exponente, resultado)

Suponiendo que tenemos a calcular 2^12, 2 = base, 12 = exponente, el resultado inicia siendo 1, entonces mandamos a llamar a nuestra función con estos parámetros

bin_exp(2,12,1)

Como el exponente es diferente de 0, y es par...
