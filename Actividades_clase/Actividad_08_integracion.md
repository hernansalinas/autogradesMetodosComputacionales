# Actividad 
1. Elaborar un programa en python que permita calcular la integral de una función entre el intervalo a, b. para ello debera realizar lo siguiente:

## Realizar en notebook de collab
- Deducir la ecuación general del metodo del trapecio.
- Construir un funcion llamada integral_trapz que reciba como argumento una función y el intervalo a, b. El numero de intervalos N será un argumento opcional, 
  defina por defecto N=10. La función deberá retornar el valor de la integral.  
- Comparar la solución con la libreria de scipy https://docs.scipy.org/doc//scipy-1.4.1/reference/generated/scipy.integrate.trapz.html

## Construir un programa en python con la función anterior que realice lo siguiente:  

- Generalice el programa para que la funcion pueda ser pasada como parametro en terminal, junto con el parametro a, b. la ejecucion debera ser:
  python integral func a b, Ejemplo de ejcucion:
  python x**2+1 1 5  

Para pasar los parametros consulte la libreria sys de python.
