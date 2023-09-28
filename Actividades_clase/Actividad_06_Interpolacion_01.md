# Interpolación Lineal

1. Construir un programa que permita calcular una interpolación lineal, para ello debera realizar lo siguiente: 

a. Deducir el método de interpolación lineal y encontrar la ecuación general de recurrencia que permite interpolar.
b. Aplicar el método para dos puntos.
c. Generalizar el método para N de puntos.


2. Determinar la interpolacion lineal que pasa por los puntos(2, 4), y (5, 1). Escribir la solución en código markdown.

3. Disenar un programa general,  que realice la interpolación de lagrange según lo visto en clase.  


4.  Realizar interpolación lagrange

Consideremos la función: 
\begin{equation*}
     f(x) = \frac{1}{1+25x^2}
\end{equation*}
en el intervalo $[-1, 1]$, definamos un conjunto de puntos $n+1$  equiespaciados en $[-1,1]$.

 1. Representar gráficamente la función junto al polinomio de interpolación de Lagrange, $p_n(x)$, para $n=\{ 4, 8, 12, 16, 20 \}$. 
 2. Comprobar gráficamente cómo el error aumenta con $n$. Emplee la libreria, simbolica de sympy y encuente el error en la interpolación.
 
 Para este numeral, emplee que: 
 
 
La cota del  error , viene dado por: 
\begin{equation}
f(x) - P(x) = \epsilon = \frac{1}{(n+1)!} f^{(n+1)}(\xi)(x - x_0)(x - x_1) ... (x - x_n)
\end{equation}, emplee la libreria simbolica para realizar la estimación de dicha cuota, sólo para n = 4, en el punto 0.5

