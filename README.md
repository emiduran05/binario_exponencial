# binario_exponencial

El algoritmo binario exponencial es una manera de calcular el exponente de un determinado numero a través de operaciones más pequeñas pero equivalentes

Ejemplo (con pseudocódigo)

function bin_exp (base, exponente, resultado)

	if exponente == 0
		return 1

	else if exponente % 2 == 0 
		bin_exp(base * base , exponente /2 , resultado) //Aqui está la recursividad

	else if exponente % 2 == 1
		if exponente == 1
			return resultado * base
		else
			bin_exp(base * base, (exponente -1) / 2, resultado * base) //Aqui esta la recursividad

	else
		return "input invalido"


El pseudocódigo representa la partición de un número con su exponente en multiplicaciones equivalentes, por ejemplo, es lo mismo 2^12 que 4^6 y es lo mismo 4^6 que 16^3 asi como 256 * 16 y finalmente obtienes el resultado con un par de operaciones en vez de multiplicar 2 doce veces consecutivas. 

Este principio se basa en operaciones equivalentes, si el exponente es un número par, se divide en dos y la base se multiplica por si misma, y se vuelve a llamar el ciclo, si el exponente es impar, y es diferente de 1 entonces la base se multiplica por si misma y el exponente se convierte en (exp -1)/2, y se multiplica la base por el resultado, que se inicia en 1.

Ejemplo:

el ciclo empieza aqui

2^12

el exponente es par, entonces se divide en dos y la base se multiplica por si misma

4^6

Aqui inica otr ciclo, donde vemos el mismo caso entonces hacemos lo mismo

16^3

Aqui se vuelve a ciclar pero el exponente es impar, por lo que se multiplica la base por el resultado (que por defecto es 1), la base se multiplica por la base y el exponente se convierte en (exp -1/2), por lo que quedaría algo asi

256^1 * 16

si la base, que en este caso es 256, su exponente llegó a 1, entonces ya llegamos al paso final, donde se multiplica el resultado (16) por la base (256) y nos da el resultado

4096

		


