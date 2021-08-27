# Prueba_Alaya
Respuestas a la prueba de clustering

## Introducción
A continuación, pongo a disposición mi respuesta al **desafío de clustering** correspondiente al análisis de motores y sensores.

## Entregables

```sh
├─── Prueba_clustering_motores.py | Script de resolución de desafío.
├─── funciones.py | Funciones auxiliares empleadas en el ejercicio.
└─── cluster_detection.csv | CSV con el id de cada fila y el estado predicho por el modelo
 ```

## Preguntas desafío

**1. De los 4 estados mencionados anteriormente, cuales crees que se encuentran presente en la data**

R: A partir de la data analizada, considero que los 4 estados pueden estar presentes. Resulta interesante que al momento de efectuar la estadística descriptiva de los 21 sensores implicados, observé una tendencia normal en 13 de los 21 sensores. Ellos me hicieron presuponer la existencia de motores nuevos (cola izquierda), motores con algún grado de uso (sector transicional), motores con desgaste promedio (sector central) y motores con un alto desgaste (cola derecha). Ello sumado a lo observado en el gráfico de los conglomerados generados, me hacen suponer la presencia de los 4 estados.

Si bien lo anterior, es necesario aclarar que esta es una inferencia basada en los datos la cual requiere un contraste con las características reales de cada motor, las cuales estuvieron ausentes en el dataframe y requieren necesaria confirmación.

**2. Como encontrarías estos estados sin conocer la data, todos los sensores aportan información? con cuales trabajarías?**

R: Dado a que la función de todo sensor es medir, naturalmente asumí que el parámetro involucrado per-sé puede cambiar. Sin embargo, es necesario indicar que el "no cambio" también es un parámetro de control importante para validar que los componentes internos que deben funcionar de una determinada forma, lo siga haciendo siempre. Esta es una variable control, la que es requerida para asegurar la validez de las condiciones deñ estudio y medición.

En este sentido, para encontrar estos estados haría una inspección del datasheet del motor y vería la composición de sensores para conocer sus rangos estándar. Luego, mediante software de control de calidad, vería el flujo potenciométrico de dichos sensores y, a partir del grado de lejanía del estándar, me aproximaría a un estado. Finalmente, **contrastaría mis apreciaciones con las de una persona entendida en motores**, que evalúe empíricamente su estado y vería el nivel de coincidencias.

Considero importante agregar que todos los sensores aportan información, tanto los que empíricamente cambian (como los sensores de oxígeno de los gases de escape) y los que debiesen ser constantes (como los sensores de rpm). En ambos casos trabajaría con ellos como criterio para clasificar.

**3. Que tipo de algoritmos no supervisados se adaptan a este problema**

R: Considero que tres algoritmos aportarían a estender esto: K-means, DBSCAN y las Gaussian Mixtures. Si bien todas las mencionadas establecen una distancia geométrica del centroide con cada uno de los datos, la manera geométrica es diferencial: las dos primeras lo hacen de manera circular, mientras que la tercera lo hace de forma no circular. Esto puede ser clave para datos cuyo posicionamiento no siga una distribución circular. En este desafío se realizó un ensayo preliminar con K-means y, a través del gráfico de inercia, se pudo determinar que la minimización de este parámetro se alcanzó con un número de conglomerados similar al número de estados descritos por el ejercicio, lo cual me hace suponer un posible correcto modelamiento. Si pudiera continuar con este desafío, contrastaría los conglomerados obtenidos con Gaussian Mixture para establecer si existe una mejor adecuación.

**4. Es factible el deep learning para descubrir estos estados**

R: Sí es factible, a través de redes neuronales. Una posible ventaja que tendría el utilizar deep learning en el contexto del desafío, es que cada dato de motor tendría un peso específico según sus atributos, los cuales pueden sumarse y darle una mirada no lineal al problema. Esto es importante porque los métodos de clasificación no supervisada como los basados en centroide, si bien pueden regularizar dicho aspecto a través del posicionamiento del dato, la reducción de la dimensionalidad hace que haya más convergencia aunque los atributos sean naturalmente distintos. Ello quiere decir que, para dos motores con set de datos totalmente diferentes para cada sensor, puede ocurrir que la reducción de la dimensionalidad genere un peso similar que haga que se vean como cercanos aún no siéndolo. Esto naturalmente genera limitantes, sobre todo en conglomerados muy cercanos unos de los otros.

**5. Es escalable la solución para todos los motores? o debes hacer el análisis por motor?**

R: El presente modelo y todos los que se pueden elaborar, naturalmente consideran las características de cada unidad para establecer patrones. Por lo mismo, naturalmente cada modelo supervisado o no supervisado revisa dato por dato para tratar de establecer aspectos comunes que permitan realizar una regresión o clasificación. Para el caso actual, hay una escalabilidad natural basada en los 20631 motores clasificados (por cada motor, 3 calibraciones y 21 sensores). Sin embargo, también existen factores a considerar como los modelos y las marcas: cada uno posee una cierta tecnología que perfectamente puede cambiar entre cada tipo de auto y manufacturador. En el presente set de datos, no es posible establecer si todos los motores testeados pertenecen a diferentes modelos y marcas, pudiendo existir algún tipo de sesgo natural: 20361 motores y autos es algo que una sola marca puede producir en un periodo de tiempo. Por lo mismo, para evaluar concretamente la escalibilidad, es necesario conocer las condiciones del muestreo (representatividad de marcas y modelos), la evaluación del mecánico (el tipo de estado). De no haber un cierto balance, se requiere un remuestreo o un oversampling para poder mejorar el desempeño de los modelos.

**6. Escribe el código**

R: Lo podrán encontrar en detalle en el archivo Prueba_clustering_motores.py. Para una mejor experiencia, invito a Uds a utilizar Jupyter Lab o Notebook para poder apreciar de forma más interactiva los gráficos generados y el flujo de trabajo realizado.

**7. Es escalable tu solución ¿Que dificultades tuvo el modelamiento? ¿Como harías escalable tu solución?**

R: Gran parte de la respuesta a esta pregunta la podrán encontrar en la pregunta n°5. Brevemente, considero que los resultados son parcialmente escalables debido al tamaño de la muestra de motores. Sin embargo, dado a que no existe información respecto a los modelos muestreados y si todos sus motores se comportan de la misma forma (aún cuando tengan los mismos sensores), es necesario considerar ello. Así, propongo dos formas para aumentar la escalabilidad:

a) Evaluar el número de datos por marca y modelo, de forma de balancear el número de ser necesario.

b) Aumentar el número de datos considerando marca y modelo, utilizando data histórica (si está disponible) o continuar evaluando motores, para aumentar aún más los atributos y con ello optimizar el modelo.

Por otro lado, uno de los desafíos fue contrastar los cluster generados con la data reportada por un mecánico en cuanto al estado del motor: la forma de saber el desempeño y correcta clasificación es sabiendo dicho dato, por lo cual el presente modelo es especulativo.
