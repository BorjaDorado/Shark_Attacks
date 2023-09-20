# Shark_Attacks
## Proyecto de limpieza de datos sobre ataques de tiburones.

### El objetivo de este proyecto hacer un análisis sobre el ratio de mortalidad y ver si este es diferente dependiendo de la zona geográfica en la que nos encontremos.

Los datos que se manipularán para la realización de este estudio han sido extraidos de https://www.kaggle.com/datasets/teajay/global-shark-attacks?resource=download.

[![sharks.jpg](https://i.postimg.cc/rpWWfMqb/sharks.jpg)](https://postimg.cc/sBjvXFQ9)

## Reglas del proyecto:
 ### 1. No se puede borrar nunguna columna del Dataframe, pero si puedes modificar los datos que hay dentro de ellas.
### 2. El Dataframe final  tiene que tener al menos 2500 filas.

### Una vez fijados el objeivo y las restricciones correspondientes se procederá con el análisis de los datos:

# 1ª Vision general
 En una primera instancia se observar que el Dataframe está muy sucio y hay dos columnas ('Unnamed: 22' y 'Unnamed: 23') llenas de valores nulos, las cuales se rellenaran con los valores del indice.

 También se observa que las columnas 'Date', 'Year', 'Case Number', 'Case Number.1' y 'Case Number.2' están correlacionadas puesto que los valores nulos de la columna 'Date' pueden ser rellenados con los de las columnas mencionadas anteriormente.

 # 2º Quitar duplicados
 En este caso al quitar las filas duplicadas el Dataframe se reduce considerablemente las dimensiones del Dataframe pasa de (25723x24) a (6312x24)

 # 3º Limpieza de las columnas (Case Number, Date, Year, Case Number.1, Case Number.2, original order, Unnamed: 22, Unnamed: 23)
 ## Se busca la posición de los valores nulos en 'Date', que es la columna que se quiere rellenar y se compueba si hay alguna coincidencia en el resto de las columnas. Al revisarlas se observa 
 ## 