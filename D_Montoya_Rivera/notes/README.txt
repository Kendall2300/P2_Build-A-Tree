Módulos importados:

from tkinter import *
import os
import pygame
from threading import Thread
from tkinter import messagebox
import random

Autodocumentacion de modulos principales:


*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Principal

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Fecha de modificación: 17/7/2020

        Descripcion de la Funcion: 
        La funcion se encarga de la creacion de toda la interfaz gráfica,
        ajusta su tamaño, evita que su tamaño sea editable y le añade un
        ícono a esta. Luego de establecer estos parámetros llama a la
        funcion

        Entradas: Ninguna

        Salidas: Llamada a la funcion Menu

*************************************************************************

*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Menu

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Fecha de modificación: 17/7/2020

        Descripcion de la Funcion: 
        La funcion crea un canvas que contiene al menu principal del juego
        y dentro de ese mismo canvas añade seis botones que realizan llamadas
        a seis funciones diferentes cuando son presionados, estas funciones
        tienen un botón que les permite regresar al menu principal.

        Entradas: Ninguna

        Salidas: Llamada a la funcion:
        -CargarImg2
        -Musica
        -Play
        -Score
        -Help
        -Credits
        -Callback
        
        

*************************************************************************

*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: InterfazJuego

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Fecha de modificación: 17/7/2020

        Descripcion de la Funcion: 
        La funcion crea un canvas que contiene al escenario del juego, crea labels
        que contienen la vida, puntuacion y tiempo, ademas crea las imágenes de
        todos los personajes del Juego y escenario. Esta no contiene botones,
        sin embargo realiza llamadas a funciones por medio de un thread excepto
        la llamada a la funcion de movimiento del personaje que uno controla.

        Entradas: Name, Lvl

        Salidas: Llamada a la funcion:

        -Timer
        -TimerVidaYPuntuacion
        -GeneraEnemigos
        -GeneraMisiles
        -GeneraAplasta
        -MovDoom
        -cargarImg2


*************************************************************************

*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Enemigo

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Fecha de modificación: 17/7/2020

        Descripcion de la Funcion: 
        La funcion crea al enemigo y llama a las funciones que
        hacen que este se mueva y dispare

        Entradas: Img, shot

        Salidas: Llamada a la funcion:

        -RecursiveShotDemonDown
        -RecursiveMovDer


*************************************************************************

*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Enemigo2

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Fecha de modificación: 17/7/2020

        Descripcion de la Funcion: 
        La funcion crea el misil y realiza la llamada a
        las funciones que hacen que se mueva el misil

        Entradas: Img

        Salidas: Llamada a la funcion:

        -RecursionMovMisil


*************************************************************************

*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Enemigo3

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Fecha de modificación: 17/7/2020

        Descripcion de la Funcion: 
        Funcion encargada de la creacion del enemigo aplastador y
        llama a las funciones encargadas de su movilidad

        Entradas: Img,posicion,bala

        Salidas: Llamada a la funcion:

        -RecursionMovAplastaAbajo


*************************************************************************

*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: MovDoom

        Lenguaje y version: Pthon 3.8.2

        Autor: Daniel Montoya Rivera

        Version 1.0

        Fecha de modificación: 17/7/2020

        Descripcion de la Funcion: 
        La funcion recibe las teclas presionadas las cuales
        realizan el movimiento del personaje

        Entradas: event

        Salidas: Llamada a la funcion:

        -MovDoomUp
        -DisparoDoom


*************************************************************************