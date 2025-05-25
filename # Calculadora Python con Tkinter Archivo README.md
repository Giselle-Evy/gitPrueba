# Calculadora Python con Tkinter

Una calculadora moderna y versátil con interfaz gráfica desarrollada en Python usando Tkinter, que incluye modo oscuro y claro, además de funciones científicas básicas.

## Características

- Interfaz gráfica moderna y responsive
- Cambio entre modo oscuro y claro
- Operaciones básicas:
  - Suma (+)
  - Resta (-)
  - Multiplicación (*)
  - División (/)
- Operaciones avanzadas:
  - Potencia (^)
  - Raíz cuadrada (√)
  - Porcentaje (%)
  - Cambio de signo (+/-)
- Funcionalidades adicionales:
  - Botón de limpieza (C)
  - Borrar último dígito (⌫)
  - Memoria (M+, M-, MR, MC)
- Soporte para números decimales
- Diseño adaptable a diferentes tamaños de ventana
- Accesos rápidos de teclado
- Historial de operaciones

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)

## Instalación

1. Clona este repositorio o descarga el archivo `calculadora.py`
```bash
git clone https://your-repository-url.git
```

2. Navega al directorio del proyecto
```bash
cd calculadora-python
```

3. Ejecuta la aplicación
```bash
python calculadora.py
```

## Uso

1. La calculadora se inicia en modo oscuro por defecto
2. Usa los botones numéricos y operadores para realizar cálculos
3. Presiona '=' para obtener el resultado
4. Presiona 'C' para limpiar la pantalla
5. Usa el botón 'Cambiar Modo' para alternar entre tema oscuro y claro
6. Accesos rápidos de teclado:
   - Enter: Calcular resultado
   - Escape: Limpiar pantalla
   - Backspace: Borrar último dígito
   - M: Acceder a funciones de memoria

## Personalización

Puedes modificar los colores de la interfaz editando los valores hexadecimales en las funciones:
- `configurar_tema_oscuro()`
- `configurar_tema_claro()`

## Notas técnicas

- Desarrollado con Python 3.10+
- Implementación de patrón MVC
- Manejo de errores robusto
- Código documentado siguiendo PEP 257

## Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:
1. Haz fork del repositorio
2. Crea una nueva rama
3. Realiza tus cambios
4. Envía un pull request

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)