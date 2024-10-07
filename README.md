# Ingresantes UNFV Admision 2024 - Puntaje Minimo y Maximo
Webscraping UNFV Admision 2024. Codigo preliminar.

Se hizo webscraping a los resultados de Admision a la UNFV 2024. 
Esto es con proposito educativo, no hay intenciones de por medio.

En la carpeta RESULTADOS, se puede encontrar archivos XLSX con los ingresantes por Facultad. 
Recordar que debes FILTRAR por Escuela Profesional y seleccionar la que te interese

# COMO USAR

1. Debes editar el archivo texttest.py con tu editor favorito.
2. Cerciorate que tengas todas las librerias necesarias:  Selenium y WebDriver
3. Modifica la variable **codigo_ini** y **codigo_fin** con los codigos a evaluar.
4. Si el programa muestra un error al final, no significa que esté mal. Significa que ya no encontró mas postulantes con el codigo.

# PROBLEMAS

1. El programa muere con error?. Calma. **Solo que ya no encontró un postulante con el codigo**. Lo que significa que ahi termina.
2. CSV? Como lo abro?. Calma. Lo que debes  hacer es abrir con Excel y guardarlo como archivo de Excel. Luego procedes a filtrar.
3. No puedo filtrar los puntajes?. Calma. Solo necesitas usar la opcion de Excel llamada ***BUSCAR Y REEMPLAZAR"**. Reemplaza la coma ( , ) por el punto ( . ). Y listo

# TODOLIST
1. Intentar mejorar el codigo con try y except para evitar los errores.
2. Usar una busqueda GLOBAL desde el codigo 00001 hasta el codigo final posible segun la cantidad de postulantes

Esta aplicación está basada en la idea de [Scraping Admission UNFV](https://github.com/jhonverde/scraping-admission-unfv) . El autor se encuentra en el mismo link.
