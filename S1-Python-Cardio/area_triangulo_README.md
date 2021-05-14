# Área de Triángulo
_Actividad parte de Python Cardio de la semana 1 del reto Datacademy_


## Reglas

El programa debe calcular el área de un triángulo con respecto a la base y la altura ingresadas por el usuario

*Bonus:* El programa debe determinar si el triángulo es isósceles, equilátero o escaleno.

## Descripción

El programa calcula el área del triángulo con respecto a la altura y la base ingresada. También determina el tipo de triangulo mediante el ingreso de un ángulo adyacente a la base menor a 60°

## Flujo de operación

**Ingreso de información Base Altura Angulo**

*Cálculo del área (b * h) / 2*

**Imprime el área**

Mediante el ángulo y la altura, calcula el cateto adyacente CO = Altura CA = CO / tan(ángulo)

##### Ahora, con el Cateto Adyacente calculado, se obtiene la hipotenusa hip = raíz (CA² + CO²)

Ya tenemos la primera hipotenusa, por lo tanto, tenemos también la dimensión del segundo lado, esto nos ayudará a determinar más adelante el tipo de triangulo

##### Continúa calculando la segunda hipotenusa Tenemos la siguiente información Altura Base Cateto adyacente

Para calcula la base del siguiente triangulo y poder calcular su hipotenusa necesitamos base de segundo triangulo
 ##### Base Ingresada por el usuario - Cateto Adyacente

Al calcular la base se tienen los siguientes datos para seguir calculando la hipotenusa de este triangulo auxiliar Base de triangulo auxiliar Altura = Altura ingresada por el usuario

##### Calcula la hipotenusa

Ahora sí, tenemos toda la información para determinar qué tipo de triangulo es: Mediante condicionales determina lo siguiente:

*Si los 3 lados son iguales entonces, es un triángulo equilátero 
Si al menos 2 lados son iguales entonces, es un triángulo Isosceles 
Si las dos condiciones anteriores no se cumplen entonces, es un triángulo Escaleno*

Al finalizar el cálculo lo muestra en pantalla y pregunta si se desea continuar con otro cálculo
