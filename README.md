El presente proyecto se enfoca en el desarrollo de un sistema capaz de inspirar a los estudiantes de música. Para lograrlo, utilizamos una base de datos de sonidos de teclas de piano y dos canciones de ejemplo. Estos recursos preexistentes se emplean como base para entrenar el sistema, permitiéndole aprender y generar nuevas melodías de manera autónoma. Además, se realizó la instalación de las bibliotecas MIDO, PYGAME y se configuró el entorno en Visual Studio Code.

Instrucciones para Ejecutar el Proyecto
Abrir el archivo en Visual Studio Code Haz clic derecho en el archivo "melodia3.py" y selecciona la opción "Abrir con…" Visual Studio Code.

Verificar extensiones Antes de ejecutar el código, asegúrate de tener instaladas las siguientes extensiones en Visual Studio Code: Pylance, Python, Python Debugger. (Si no las tienes, descárgalas e instálalas desde la tienda de extensiones).

Instalar la biblioteca "mido" Abre la terminal en Visual Studio Code y ejecuta el siguiente comando: python3 -m pip install mido Esto instalará la biblioteca "mido" necesaria para que el programa funcione correctamente. Si encuentras errores durante la instalación, consulta la documentación en este enlace para obtener los pasos y requisitos de instalación.

Ejecutar el programa En la parte superior derecha de Visual Studio Code, encontrarás el botón de reproducción (play). Sin embargo, selecciona la flecha hacia abajo junto al botón de reproducción y elige la opción "Run Python file in Dedicated terminal". El código generará las melodías y las guardará en la carpeta del usuario. Si no sabes dónde se encuentra la carpeta, el programa indicará la ubicación donde se generaron las melodías.
