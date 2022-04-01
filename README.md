# Descargar-cursos-aprenderaprogramar.com
Programa para descargar de forma automatizada cursos completos de la página aprenderaprogramar.com.

Se piden dos datos de entrada: 
1. La url de inicio de la descarga. Será la url a partir de la cual se descargarán todos y cada uno de los módulos del curso. Normalmente se corresponde con el segundo módulo del curso, a saber: el Índice. Lo relevante de cara al funcionamiento correcto del programa es que dicha url incial incluya un enlace "Siguiente" al próximo módulo (al final de la página), de forma que la descarga pueda proseguir adecuadamente hasta descargar el curso entero.
2. La carpeta de destino. Se creará en el directorio actual de trabajo (pwd)

Dos ejemplos de url de inicio para los cursos "Bases de la Programación I" y "Java desde cero" respectivamente serían:
- https://www.aprenderaprogramar.com/index.php?option=com_content&view=article&id=90:indice-del-curso-qbases-de-la-programacion-nivel-iq-cu00102a&catid=28&Itemid=59
- https://www.aprenderaprogramar.com/index.php?option=com_content&view=article&id=362:indice-del-curso-qaprender-programacion-java-desde-ceroq-cu00601b&catid=68&Itemid=188
