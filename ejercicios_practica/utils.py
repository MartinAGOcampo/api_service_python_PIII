'''
Archivo con utilidades para la app
---------------------------
Autor: Ing.Jesús Matías González
Version: 2.0

Descripcion:
En este programa se encuentran distitas herramientas
de ayuda para utilizar en la aplicación
'''

import io
import base64

import matplotlib
matplotlib.use('Agg')   # Para multi-thread, non-interactive backend (avoid run in main loop)
import matplotlib.pyplot as plt
# Para convertir matplotlib a imagen y luego a datos binarios
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg


def graficar(x, y):
    ''' 
        Crear el grafico que se desea mostrar en HTML
    '''
    x = list(x)
    y = list(y)

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(x, y)
    ax.set_xlabel('ID')
    ax.set_ylabel('Edad')
    ax.set_title('Comparativa de edades')

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return img
