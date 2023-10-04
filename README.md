# Shark_Attacks
## Proyecto de limpieza de datos sobre ataques de tiburones.

Este proyecto tiene como ***objetivo*** principal realizar una ***limpieza*** exhaustiva de un conjunto ***de datos*** sobre ataques de tiburones. Además, se realizará un análisis del ratio de mortalidad y se investigará si este varía dependiendo de la zona geográfica.

Los datos utilizados para este estudio han sido extraídos de [Kaggle](https://www.kaggle.com/datasets/teajay/global-shark-attacks?resource=download).

[![sharks.jpg](https://i.postimg.cc/rpWWfMqb/sharks.jpg)](https://postimg.cc/sBjvXFQ9)

## Reglas del proyecto

1. ***No se puede eliminar ninguna columna del Dataframe***, pero se pueden modificar los valores que contienen. 
  
2. El Dataframe final debe tener ***al menos 2500 filas***.

Una vez establecidos el objetivo y las restricciones del proyecto, se procederá con el análisis de los datos:

## Visión general

En una primera inspección, se observa que el Dataframe está bastante desordenado y que las columnas 'Unnamed: 22' y 'Unnamed: 23' están llenas de valores nulos. Estas columnas se llenarán con los valores correspondientes de los índices.

También se observa que las columnas 'Date', 'Year', 'Case Number', 'Case Number.1' y 'Case Number.2' están relacionadas, ya que todas ellas corresponden a la fecha. Podemos completar los valores faltantes en la columna 'Date' utilizando la información de las demás columnas.

## Eliminación de duplicados

En este paso, se eliminarán las filas duplicadas del Dataframe. Tras realizar esta operación, el tamaño del Dataframe se reduce significativamente, pasando de ser (25723x24) a (6312x24).

# Limpieza de columnas

## Columna Type

Se analizarán los casos en los que el tipo de ataque sea inválido o haya sido causado por un desastre natural para verificar si en realidad han sido provocados por un tiburón.

## Columnas Country, Location y Area

Para limpiar estas columnas, se utilizarán expresiones regulares para eliminar datos numéricos y símbolos no deseados, especialmente aquellos relacionados con puntos cardinales.

## Columna Activity

Se agruparán las actividades en 10 grandes grupos: surfing, swimming, fishing, wading, bathing, diving, body boarding, snorkeling, scuba diving y treading water.

## Columna Name

Se eliminarán los valores 'male' y 'female' de esta columna, ya que no tiene sentido que estén aquí. Además, se llenarán los valores nulos en la columna Sex con dichos valores.

## Columnas Sex y Age

Se unificarán los valores de la columna Sex, de manera que aparezca 'F' (Female) si la víctima es una mujer, y 'M' (Male) si es un hombre. Todos los valores no numéricos de la columna Age se eliminarán.

## Columna Fatal

El contenido de esta columna se convertirá a un formato booleano, es decir, mostrará True si la persona ha fallecido y False si ha sobrevivido.

## Columna Time

El tipo de dato de esta columna se cambiará a datetime y se eliminarán los strings.

## Columna Species

Se eliminarán todas las filas en las que no se tenga constancia de que el ataque haya sido causado por un tiburón.

# Visualización

En el gráfico mostrado, se puede observar que Georgia, Maryland y US Virgin Island son los estados con mayor porcentaje de mortalidad, con un ratio del 50%. Les siguen de cerca Mississippi y Virginia. Esta visualización se ha enfocado en los estados de Estados Unidos ya que la mayoría de los datos proceden de dicho país.

[![Captura.png](https://i.postimg.cc/CLWBFRM2/Captura.png)](https://postimg.cc/Whwb8bkm)