
from tkinter import *
import os
import pygame
from threading import Thread
from tkinter import messagebox
import random


class General: #La clase contiene todas las interfaces presentes en el menu, con sus respectivos botones.

    global CoordBullet, CoordSlayer, CoordEnemy,coordMisil, coordAplasta, Misil, Aplasta, Vivo, AplastaBullet, SCORE, Tiempo,  PlayOrNot, Hp, Salto, Derecha, Izquierda, Disparo   #Variables globales correspondientes a las coordenadas de los objetos del juego


    Hp = 3
    
    
    def Principal(): #Funcion generadora de la interfaz
        """
*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Principal

        Lenguaje y version: Pthon 3.8.2

        Autores:
        Daniel Montoya Rivera
        Kendall Adolfo Martinez Carvajal
        

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
        """
        global WindGame, Salto, Derecha, Izquierda, Disparo

        Salto = "W"
        Derecha = "D"
        Izquierda = "A"
        Disparo = " "
        PlayOrNot = "Play"
        
        WindGame = Tk()

        WindGame.title("Smash")
        WindGame.minsize(1500,800)
        WindGame.resizable(width = False , height = False)

        WindGame.iconphoto(False, PhotoImage(file = 'img\icon.png'))

        
        #General.InterfazJuego("hola", 1)
        General.Menu()
        WindGame.mainloop()
        
    #End Principal


    def Musica(cancion): #Funcion encargada de reproducir la música
        global PlayOrNot

        

        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pygame.mixer.init()

        ruta = os.path.join('music', cancion)
        
        sound = pygame.mixer.Sound(ruta)
        sound.set_volume(0.05)

        sound.play()


    def cargarImg2(archivo):#Funcion encargada de la creación de imágenes
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file=ruta)
        return imagen
    
    #End CargarImg
    
    def playSmash():

        C_Play = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Play.place(x=0, y=0)

        C_Play.image1 = General.cargarImg2('InterfazMenu.png') #Background
        imgCanvas = C_Play.create_image(0,0, anchor = NW , image =C_Play.image1)
        
        Lb_Nombre = Label(C_Play, text= 'Nickname', bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13), height = 2, width = 10 )
        Lb_Nombre.place(x=700, y = 100)
        
        En_Nombre = Entry(C_Play)
        En_Nombre.place(x = 745, y = 150)

        En_IP = Entry(C_Play, width = 25)
        En_IP.place_forget()
        
        btn_Go1 = Button(C_Play, text = 'Create Server', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:Play_aux_host(C_Play, (En_Nombre.get()).strip()), font =("Goudy Stout", 13))
        btn_Go1.place(x = 400, y = 400)

        btn_Go2 = Button(C_Play, text = 'Join Server', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:Play_aux_join(C_Play, (En_Nombre.get()).strip()), font =("Goudy Stout", 13))
        btn_Go2.place(x = 950, y = 400)
        
        btn_Return = Button(C_Play, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 1200, y = 700 )
        
        btn_Play = Button(C_Play, text = 'Lets go dude!', bg = 'black', fg = 'Yellow', height = 1, width = 13,font =("Goudy Stout", 13))

        lb_Error = Label(C_Play, text= 'El nombre no puede estar vacío', bg ='Black', fg = 'Red', font ="Arial 13")

        lb_Error2 = Label(C_Play, text= 'El nombre no debe exeder la cantidad de caracteres máximos (11)', bg ='Black', fg = 'Red', font ="Arial 13")
        
        lb_Error3 = Label(C_Play, text= 'IP del servidor no válida', bg ='Black', fg = 'Red', font ="Arial 13")
        lb_Error3.place_forget()

        lb_IP =  Label(C_Play, text= 'Ingrese la dirección IP', bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13), height = 2, width = 20)
        lb_IP.place_forget()
        
        def Play_aux_host(C_Play, Texto): #La función se encarga de la creación del servidor
            if not Texto:
                lb_Error2.place_forget()
                lb_Error.place(x=745, y = 180)
            elif len(Texto) > 11:
                lb_Error.place_forget()
                lb_Error2.place(x=550, y = 180)
            else:
                lb_Error2.place_forget()
                lb_Error.place_forget()
                General.InterfazJuego(Texto, 0.5)
        
        def Play_aux_join(C_Play, Texto): #La funcion evalúa que no se ingrese un nombre en blanco, eso incluye espacios vacíos
            if not Texto:
                lb_Error2.place_forget()
                lb_Error.place(x=745, y = 180)
            elif len(Texto) > 11:
                lb_Error.place_forget()
                lb_Error2.place(x=550, y = 180)
            else:
                lb_Error2.place_forget()
                lb_Error.place_forget()
                btn_Go2.place_forget()
                btn_Go1.place_forget()
                En_Nombre.place_forget()
                Lb_Nombre.place_forget()
                lb_IP.place(x = 100, y = 150)
                En_IP.place(x = 530, y = 165)
                btn_Play = Button(C_Play, text = 'Lets go dude!', bg = 'black', fg = 'Yellow', height = 1,command = lambda: ValidaIP(En_IP.get().strip()), width = 13,font =("Goudy Stout", 13))
                btn_Play.place(x = 550, y = 600)

                def ValidaIP(Texto):
                    if not En_IP.get().strip():
                        lb_Error3.place(x = 530, y = 100)
                    else:
                        print("FUNCA")
                        #General.InterfazJuego(Texto, 0.5)

                
        
        #End Play

            




        
    def Score():
        C_Score = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Score.place(x=0, y=0)

        
        C_Score.image1 = General.cargarImg2('InterfazMenu.png')#Creacion del fondo de la interfaz
        imgCanvas = C_Score.create_image(0,0, anchor = NW , image =C_Score.image1)


        Puntuaciones = open("notes\D_Montoya_Rivera_Scores.txt", "r", encoding="UTF8").read()

        lb_Ayuda = Label(C_Score, text = Puntuaciones, bg='Black', fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_Ayuda.place(x = 25, y = 100 )





        btn_Return = Button(C_Score, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 1200, y = 700 )
        
        #End Score



        
    def Help(): #La funcion muestra los controles y el objetivo del juego

        global Salto, Derecha, Izquierda, Disparo
        
        C_Help = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Help.place(x=0,y=0)
        
        C_Help.image1 = General.cargarImg2('InterfazMenu.png')#Background 
        imgCanvas = C_Help.create_image(0,0, anchor = NW , image =C_Help.image1)


        

        #Muestreo de las instrucciones del juego (Completo)
        
        HelpFile = open("notes\D_Montoya_Rivera_Help.txt", "r", encoding="UTF8").read() #Llamada a un archivo .txt que contiene las instrucciones del juego
        
        lb_Ayuda = Label(C_Help, text = HelpFile, bg='Black', fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_Ayuda.place_forget()
        
        
        
        #Controles del juego (Completo)
        
        #Salto
        lb_Salto = Label(C_Help, text = 'SALTO:' , bg = 'White', fg = 'black', font = "Arial 12")
        lb_Salto.place_forget()
        
        lb_TeclaSalto = Label(C_Help, text = Salto , bg = 'White', fg = 'black', font = "Arial 12")
        lb_TeclaSalto.place_forget()

        en_Salto = Entry(C_Help)
        en_Salto.place_forget()

        #Disparo
        lb_Disparo = Label(C_Help, text = 'DISPARO:' , bg = 'White', fg = 'black', font = "Arial 12")
        lb_Disparo.place_forget()
        
        lb_TeclaDisparo = Label(C_Help, text = Disparo , bg = 'White', fg = 'black', font = "Arial 12")
        lb_TeclaDisparo.place_forget()

        en_Disparo = Entry(C_Help)
        en_Disparo.place_forget()

        #Mover izquierda
        lb_MoverIzq = Label(C_Help, text = 'MOVIMIENTO IZQUIERDA:' , bg = 'White', fg = 'black', font = "Arial 12")
        lb_MoverIzq.place_forget()
        
        lb_TeclaMoverIzq = Label(C_Help, text = Izquierda , bg = 'White', fg = 'black', font = "Arial 12")
        lb_TeclaMoverIzq.place_forget()

        en_MoverIzq = Entry(C_Help)
        en_MoverIzq.place_forget()
        
        #Mover Derecha
        lb_MoverDer = Label(C_Help, text = 'MOVIMIENTO DERECHA:' , bg = 'White', fg = 'black', font = "Arial 12")
        lb_MoverDer.place_forget()
        
        lb_TeclaMoverDer = Label(C_Help, text = Derecha , bg = 'White', fg = 'black', font = "Arial 12")
        lb_TeclaMoverDer.place_forget()

        en_MoverDer = Entry(C_Help)
        en_MoverDer.place_forget()

        lB_ErrorInput =  Label(C_Help, text= 'La entrada no puede estar vacía | Las teclas NO pueden ser las mismas | Solo puede ser 1 caracter', bg ='Black', fg = 'Red', font ="Arial 16")
        
        
        #Botones de la interfaz de ayuda
        
        btn_Change = Button(C_Help, text = 'Save Changes', bg = 'black', fg = 'Yellow', height = 1, width = 13, font =("Goudy Stout", 13),command = lambda: CambioControles((en_Disparo.get()).upper(), (en_MoverIzq.get()).upper(), (en_Salto.get()).upper(), (en_MoverDer.get().upper()))) #Se encarga de cambiar los contrles 
        btn_Change.place_forget()

        
        btn_Controles = Button(C_Help, text = 'Controles', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:(lb_Salto.place(x = 10, y = 100),
                                                                                                                                  lb_TeclaSalto.place(x = 300, y = 100),
                                                                                                                                  en_Salto.place(x=400, y = 100),
                                                                                                                                  lb_Disparo.place(x = 10, y = 200),
                                                                                                                                  lb_TeclaDisparo.place(x = 300, y = 200),
                                                                                                                                  en_Disparo.place(x=400, y = 200),
                                                                                                                                  lb_MoverIzq.place(x = 10, y = 300),
                                                                                                                                  lb_TeclaMoverIzq.place(x = 300, y = 300),
                                                                                                                                  en_MoverIzq.place(x=400, y = 300),
                                                                                                                                  lb_MoverDer.place(x = 10, y = 400),
                                                                                                                                  lb_TeclaMoverDer.place(x = 300, y = 400),
                                                                                                                                  en_MoverDer.place(x=400, y = 400),
                                                                                                                                  lb_Ayuda.place_forget(),
                                                                                                                                  btn_Change.place(x = 1200 , y = 300)) ,  font =("Goudy Stout", 13))# Se encarga de mostrar los controles
        btn_Controles.place(x = 1200 , y = 100)
        
        btn_Objetivo = Button(C_Help, text = 'Objectivo', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda: (lb_Ayuda.place(x=25, y = 100),
                                                                                                                                  lb_Salto.place_forget(),
                                                                                                                                  lb_TeclaSalto.place_forget(),
                                                                                                                                  en_Salto.place_forget(),
                                                                                                                                  lb_Disparo.place_forget(),
                                                                                                                                  lb_TeclaDisparo.place_forget(),
                                                                                                                                  en_Disparo.place_forget(),
                                                                                                                                  lb_MoverIzq.place_forget(),
                                                                                                                                  lb_TeclaMoverIzq.place_forget(),
                                                                                                                                  en_MoverIzq.place_forget(),
                                                                                                                                  lb_MoverDer.place_forget(),
                                                                                                                                  lb_TeclaMoverDer.place_forget(),
                                                                                                                                  en_MoverDer.place_forget(),
                                                                                                                                  btn_Change.place_forget(),
                                                                                                                                  lB_ErrorInput.place_forget()), font =("Goudy Stout", 13))# Se encarga de mostrar el objetivo del juego 
        btn_Objetivo.place(x = 1200, y = 500 )


        
        
        btn_Return = Button(C_Help, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 1200, y = 700 )

        
        

        def CambioControles(Dis, Izq, Sal, Der): #Evalúa que la edición de teclas sea correcta

            global Salto, Derecha, Izquierda, Disparo

            if len(Dis) > 1 or len(Izq) > 1 or len(Sal) > 1 or len(Der) > 1:
                lB_ErrorInput.config(text= 'SOLO puede ser 1 caracter', bg ='Black', fg = 'Red', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
            elif Dis == Izq or Dis == Sal or Dis == Der or Izq == Sal or Izq == Der or Sal == Der:
                lB_ErrorInput.config(text= 'Las teclas NO pueden ser las mismas', bg ='Black', fg = 'Red', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
            elif len(Dis) == 0 or len(Izq)  == 0 or len(Sal)  == 0 or len(Der)  == 0 :
                lB_ErrorInput.config(text= 'La entrada NO puede estar vacía', bg ='Black', fg = 'Red', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
            else:
                Salto=Sal
                Derecha=Der
                Disparo=Dis
                Izquierda=Izq

                print (Salto, Derecha, Disparo, Izquierda)
                                
                lb_TeclaSalto.config(text = Salto , bg = 'White', fg = 'black', font = "Arial 12")
                
                lb_TeclaDisparo.config(text = Disparo , bg = 'White', fg = 'black', font = "Arial 12")

                lb_TeclaMoverIzq.config(text = Izquierda , bg = 'White', fg = 'black', font = "Arial 12")

                lb_TeclaMoverDer.config(text = Derecha , bg = 'White', fg = 'black', font = "Arial 12")

                
                lB_ErrorInput.config(text= 'Cambios realizados exitósamente', bg ='Black', fg = 'Green', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)


        #End Help


        






        
    def Credits():
        C_Credits = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Credits.place(x=0, y=0)
        
        C_Credits.image1 = General.cargarImg2('InterfazMenu.png')#Background 
        imgCanvas = C_Credits.create_image(0,0, anchor = NW , image =C_Credits.image1)


        Autor = open("notes\D_Montoya_Rivera_Credits.txt", "r", encoding="UTF8").read() #Llamada a un archivo .txt que contiene al autor del programa.
        
        Modulo = open("notes\D_Montoya_Rivera_Modulos.txt", "r", encoding="UTF8").read() #Llamada a un archivo .txt que contiene los modulos implementados.
        
        lb_Autor = Label(C_Credits, text = Autor, bg='Black', fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_Autor.place(x=25, y = 100)

        lb_Modulo = Label(C_Credits, text = Modulo, bg='Black', fg= 'Green', font = "Arial 14") #Label que muestra el archivo
        lb_Modulo.place(x=500, y = 100)


        
        btn_Return = Button(C_Credits, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 1200, y = 700)


        
        #End Credits








    
    def Menu(): #Interfaz del menu
        """
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
        """

        C_Game = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Game.place(x=0, y=0)
        
        
        C_Game.image1 = General.cargarImg2('InterfazMenu.png')#Background 
        imgCanvas = C_Game.create_image(0,0, anchor = NW , image =C_Game.image1)

        #Botones
    
        btn_Play = Button(C_Game, text = 'PLAY', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.playSmash(), font =("Goudy Stout", 13)) 
        btn_Play.place(x = 700, y = 100 )
        
        btn_Scores = Button(C_Game, text = 'HISTORY', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Score(), font =("Goudy Stout", 13)) 
        btn_Scores.place(x = 700, y = 250 )

        btn_Help = Button(C_Game, text = 'HELP', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Help(), font =("Goudy Stout", 13)) 
        btn_Help.place(x = 700, y = 400 )

        btn_Credits = Button(C_Game, text = 'CREDITS', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Credits(), font =("Goudy Stout", 13)) 
        btn_Credits.place(x = 700, y = 550 )

        btn_Exit = Button(C_Game, text = 'EXIT GAME', bg = 'black', fg = 'Yellow', height = 1, width = 10, command = lambda:General.Callback(), font =("Goudy Stout", 13)) 
        btn_Exit.place(x = 700 , y = 700 )



        
        
        btn_Play =Button(C_Game, text = 'PLAY CUMBIÓN', bg = 'black', fg = 'Yellow', height = 1,command = lambda: Thread(target = (General.Musica), args = (('Theme.wav'),)).start(),  width = 15, font =("Goudy Stout", 13))#Activa la música
        btn_Play.place(x = 6, y = 766)


        
        #End Menu

    def Callback():
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            WindGame.destroy()
    

    def GameOver(Jugador, Score, Condicion): 
        
        C_GameOver = Canvas(WindGame, width = 900 , height = 800, bg = 'green')
        C_GameOver.place(x=0, y=0)

        
        C_GameOver.Over = General.cargarImg2('GameOver.png')#Background
        
        Img = C_GameOver.create_image(0,0, anchor = NW , image = C_GameOver.Over)

        def setPuntuacion():
            WriteScore = open("notes\D_Montoya_Rivera_Scores.txt", 'a')
            WriteScore.write("\n" + Jugador + "\n" + str(Score))
            return
        setPuntuacion()

        if Condicion == "Victoria":
        
            lb_Fin = Label(C_GameOver, text= ("El tiempo se ha acabado"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_Fin.place(x= 250, y = 10)

            lb_Name = Label(C_GameOver, text= ("Name: " + Jugador), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13))
            lb_Name.place(x= 250, y = 50)
            
            lb_SCORE = Label(C_GameOver, text= ("Puntuacion = " + str(SCORE) + " pts"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_SCORE.place(x=250, y = 100)
            
        else:
            lb_Fin = Label(C_GameOver, text= ("Te han matado"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_Fin.place(x=250,y=10)
            
            lb_SCORE = Label(C_GameOver, text= ("Puntuacion = " + str(SCORE) + " pts"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_SCORE.place(x=250, y = 50)




            
        btn_Return = Button(C_GameOver, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 500, y = 700)

    def InterfazJuego(Name, Lvl): #Recibe el nombre del usuario, y el dificultad
        """
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
        """

        
        #***************Acciones de enemigos*********************
        
        def Enemigo(Img, shot):
            """
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
            """
            
            
            Daño = 0
            
            Demon = C_Juego.create_image(0,6,anchor = NW, image =Img)

            #Thread(target = RecursiveMovDer(Demon,0)).start()

            

            Shot = C_Juego.create_image(CoordEnemy[0]+90, CoordEnemy[1]+154,anchor = NW, image =shot)

            

            

            def RecursiveShotDemonDown(): #La funcion realiza la el disparo del proyectil
                global coordShot
                
                coordShot = C_Juego.coords(Shot)
                
                if coordShot[1] >= 800 or Vivo == False:
                    C_Juego.delete(Shot)
                else:
                    C_Juego.coords(Shot, coordShot[0], coordShot[1]+5)
                    WindGame.after(5, lambda: RecursiveShotDemonDown())
                
            Thread(target = RecursiveShotDemonDown).start()
            
            RecursiveMovDer(Demon,0)
            
        def RecursiveMovDer(ImgDemon, Daño): #Funcion encargada de la movilidad recursiva del enemigo Comun hacia la derecha

            global CoordEnemy, CoordBullet, ShotSlayer, SCORE, Hp, Tiempo
            
            coord = C_Juego.coords(ImgDemon) #Registro de la posicion del enemigo 
            CoordY = coord[1]
            CoordEnemy = C_Juego.coords(ImgDemon) #Registro de la posicion del enemigo 

            
            if Tiempo == 0 or Hp <= 0:
                CoordEnemy = [0,0]
                C_Juego.delete(ImgDemon)
                return
            else:
                if (CoordEnemy[0]+90 >= CoordSlayer[0]) and (CoordEnemy[0]+90 <=  CoordSlayer[0]+80) and (CoordEnemy[1]+154 >= CoordSlayer[1] ) and (CoordEnemy[1]+154 <= CoordSlayer[1]+124):
                    Hp -= 1
                    C_Juego.delete(ImgDemon)
                    return
                else:
                    if (CoordBullet[0]+10) <= (CoordEnemy[0]+150) and (CoordBullet[0]+10) >= (CoordEnemy[0]+40) and (CoordBullet[1]) <= (CoordEnemy[1]+154) and (CoordBullet[1]) >= (CoordEnemy[1]+46): #Colicion entre la bala y el enemigo  
                        if Daño == 3:#Evalúa la vida del enemigo
                            global Vivo
                            Vivo = False
                            Daño = 0
                            SCORE += 5
                            CoordBullet=[0,0]
                            CoordEnemy = [0,0]
                            C_Juego.delete(ImgDemon)
                            return
                        else:
                            Daño += 1
                            CoordBullet = [0,0]
                            WindGame.after(5, lambda: RecursiveMovDer(ImgDemon,Daño))
                            
                    else:
                        if coord[0] >= 750.0: #Evalua que el enemigo ya llegó al límmite de la pantalla
                            WindGame.after(5, lambda: RecursiveMovDown(ImgDemon, CoordY,Daño)) #Llamada a la funcion que hace que el enemigo se mueva hacia abajo
                        else:
                            C_Juego.coords(ImgDemon, coord[0]+1, coord[1]) #Realiza el movimiento a la derecha
                            WindGame.after(5, lambda: RecursiveMovDer(ImgDemon,Daño))#Llamada recursiva



        def RecursiveMovIzq(ImgDemon,Daño):#Funcion encargada de la movilidad recursiva del enemigo Comun hacia la izquierda
            
            global CoordEnemy, CoordBullet, ShotSlayer, SCORE, Tiempo, Hp
            coord = C_Juego.coords(ImgDemon)#Registro de la posicion del enemigo 
            CoordY = coord[1]
            CoordEnemy = coord

            if Tiempo == 0 or Hp <= 0:
                CoordEnemy = [0,0]
                C_Juego.delete(ImgDemon)
                return
            else:
                if (CoordBullet[0]+10) <= (CoordEnemy[0]+150) and (CoordBullet[0]+10) >= (CoordEnemy[0]+40) and (CoordBullet[1]) <= (CoordEnemy[1]+154) and (CoordBullet[1]) >= (CoordEnemy[1]+46): #Esta condiocion compara si el proyectil disparado es igual al hitbox del enemigo  
                    if Daño == 3:#Evalúa la vida del enemigo
                        global Vivo
                        Vivo = False
                        Daño = 0
                        SCORE += 5
                        CoordBullet=[0,0]
                        CoordEnemy = [0,0]
                        C_Juego.delete(ImgDemon)
                        return
                    else:
                        Daño += 1
                        CoordBullet = [0,0]
                        WindGame.after(5, lambda: RecursiveMovIzq(ImgDemon, Daño))
                        
                else:
                    if coord[0] <= 6: #Evalua que el enemigo esté en el límite del escenario
                        WindGame.after(5, lambda: RecursiveMovDown(ImgDemon, CoordY, Daño))
                    else:
                        C_Juego.coords(ImgDemon, coord[0]-1, coord[1])#Movimiento del objeto
                        WindGame.after(5, lambda: RecursiveMovIzq(ImgDemon, Daño))#Llamada recursiva
                    


        def RecursiveMovDown(ImgDemon, CoordY, Daño):#Funcion encargada de la movilidad recursiva del enemigo Comun hacia abajo
            global CoordEnemy, CoordBullet, ShotSlayer, SCORE, Hp, Tiempo
            coord = C_Juego.coords(ImgDemon)#Registro de la posicion del enemigo
            CoordEnemy = coord

            if Tiempo == 0 or Hp <= 0:
                CoordEnemy = [0,0]
                C_Juego.delete(ImgDemon)
                return
            else:
                if (CoordEnemy[0]+90 >= CoordSlayer[0]) and (CoordEnemy[0]+90 <=  CoordSlayer[0]+80) and (CoordEnemy[1]+154 >= CoordSlayer[1] ) and (CoordEnemy[1]+154 <= CoordSlayer[1]+124): #Colision entre el enemigo Comun y el personaje
                    Hp -= 1
                    C_Juego.delete(ImgDemon)
                else:
                    if coord[1] >= 600:
                        C_Juego.delete(ImgDemon)
                        return
                    else:
                        if (CoordBullet[0]+10) <= (CoordEnemy[0]+150) and (CoordBullet[0]+10) >= (CoordEnemy[0]+40) and (CoordBullet[1]) <= (CoordEnemy[1]+154) and (CoordBullet[1]) >= (CoordEnemy[1]+46): #Colision entre la bala y el enemigo Comun
                            
                            if Daño == 3:#Evalúa la vida del enemigo
                                global Vivo
                                Vivo = False
                                Daño = 0
                                SCORE += 5
                                CoordBullet=[0,0]
                                CoordEnemy = [0,0]
                                C_Juego.delete(ImgDemon)
                                return
                            else:
                                Daño += 1
                                CoordBullet = [0,0]
                                WindGame.after(5, lambda: RecursiveMovDown(ImgDemon, CoordY, Daño))
                                
                        else:
                            if coord[1] == (CoordY+120) and coord[0] == 750: #Evalua que la posicion del enemigo este abajo y a la derecha 
                                WindGame.after(5, lambda: RecursiveMovIzq(ImgDemon, Daño))
                            elif coord[1] == (CoordY+120) and coord[0] == 6: #Evalua que la posicion del enemigo este abajo y a la izquierda
                                WindGame.after(5, lambda: RecursiveMovDer(ImgDemon, Daño))
                            else:
                                C_Juego.coords(ImgDemon, coord[0], coord[1]+1) #Movimiento del objeto
                                WindGame.after(5, lambda: RecursiveMovDown(ImgDemon, CoordY, Daño))#Llamada recursiva


        
        def Enemigo2(Img):
            """
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
            """
            global Misil
            
            Misil = C_Juego.create_image((random.randint(0 , 800)),0 ,anchor = NW ,image =Img)

            RecursionMovMisil(Misil)
            
        def RecursionMovMisil(Misil): #Funcion recursiva encargada de la caída del misil
            global coordMisil, CoordBullet, SCORE, Hp, Tiempo
            coordMisil = C_Juego.coords(Misil)

            MisilHitbox = [C_Juego.coords(Misil)[0]+25, C_Juego.coords(Misil)[1]+60] #Establece el hitbox del misil
            
            if Tiempo == 0 or Hp <= 0:
                coordMisil=[0,0]
                C_Juego.delete(Misil)
                return
            else:
                if (MisilHitbox[0] >= CoordSlayer[0]) and (MisilHitbox[0] <= CoordSlayer[0]+80) and (MisilHitbox[1] >= CoordSlayer[1]) and (MisilHitbox[1] <=CoordSlayer[1]+124):#Colision del misil con el personaje
                    coordMisil = [0,0]
                    Hp-=2
                    C_Juego.delete(Misil)
                    return
                else:
                    if CoordBullet[0]+10 >= coordMisil[0] and CoordBullet[0]+10 <= coordMisil[0] +60 and CoordBullet[1] >= coordMisil[1] + 20 and CoordBullet[1] <= coordMisil[1] + 60: #Colision entre el misil y la bala
                        C_Juego.delete(Misil)
                        SCORE += 1
                        return
                    else:
                        if coordMisil[1] >= 900:
                            C_Juego.delete(Misil)
                        else:
                            C_Juego.coords(Misil,coordMisil[0], coordMisil[1]+3)#Movimiento del personaje
                            WindGame.after(5, lambda: RecursionMovMisil(Misil)) #Llamada recursiva






        def Enemigo3(Img, posicion, bala):
            """
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
            """

            
            global Aplasta, AplastaBala, daño, coordAplasta, CoordBullet

            AplastaBala = bala
            daño = 0


            if posicion == 1:
                Aplasta = C_Juego.create_image(25, 0, anchor = NW, image = Img)
                RecursionMovAplastaAbajo(Aplasta, daño)
            elif posicion == 2:
                Aplasta = C_Juego.create_image(800, 0, anchor = NW, image = Img)
                RecursionMovAplastaAbajo(Aplasta, daño)
            
            
            
        def RecursionMovAplastaAbajo(Aplasta, daño): #Movimiento del enemigo aplastador hacia abajo
            global coordAplasta, CoordBullet, SCORE, Hp, Tiempo
            
            coordAplasta = C_Juego.coords(Aplasta)

            if Tiempo == 0 or Hp <= 0:
                coordAplasta=[0,0]
                C_Juego.delete(Aplasta)
                return
            else:
                if (coordAplasta[0] >= CoordSlayer[0]) and (coordAplasta[0] <= CoordSlayer[0]+80) and (coordAplasta[1]>= CoordSlayer[1]) and (coordAplasta[1]<=CoordSlayer[1]+124):#Colicion del enemigo Aplastador con el personaje
                    Hp -= 1
                    coordAplasta = [0,0]
                    C_Juego.delete(Aplasta)
                    return
                else:
                    if CoordBullet[0]+10 >= coordAplasta[0]+5 and CoordBullet[0]+10 <= coordAplasta[0]+65 and CoordBullet[1] >= coordAplasta[1] and CoordBullet[1] <= coordAplasta[1]+70: #Colision del enemigo aplastador y la bala
                        if daño == 5: #Evalúa la vida del enemigo
                            coordMisil = [0,0]
                            daño = 0
                            C_Juego.delete(Aplasta)
                            SCORE += 20
                            return
                        else:
                            daño += 1
                            CoordBullet=[0,0]
                            RecursionMovAplastaAbajo(Aplasta, daño)
                    else:
                        if coordAplasta[1] >= 700.0:
                            if coordAplasta[0] <= 25:
                                RecursionMovAplastaDer(Aplasta)
                            else:
                                RecursionMovAplastaIzq(Aplasta)
                        else:
                            C_Juego.coords(Aplasta,coordAplasta[0], coordAplasta[1]+2)#Movimiento del objeto
                            WindGame.after(5, lambda: RecursionMovAplastaAbajo(Aplasta, daño))#Llamada recursiva

        def RecursionMovAplastaDer(Aplasta): #Movimiento del enemigo aplastador hacia la derecha
            global coordAplasta, SCORE,Hp, Tiempo
            
            coordAplasta = C_Juego.coords(Aplasta)

            
            if Tiempo == 0 or Hp <= 0:
                coordAplasta=[0,0]
                C_Juego.delete(Aplasta)
                return
            else:
                if (coordAplasta[0] >= CoordSlayer[0]) and (coordAplasta[0] <= CoordSlayer[0]+50) and (coordAplasta[1]>= CoordSlayer[1]) and (coordAplasta[1]<=CoordSlayer[1]+124):#Colicion del enemigo Aplastador con el personaje
                    Hp -= 1
                    coordAplasta = [0,0]
                    C_Juego.delete(Aplasta)
                    return
                else:
                    if coordAplasta[0] >= 850:
                        Thread(target = DisparoRecursivoAplasta(coordAplasta, 1))
                        C_Juego.delete(Aplasta)
                        SCORE += 2
                    else:
                        C_Juego.coords(Aplasta, coordAplasta[0]+2, coordAplasta[1])#Movimiento del objeto
                        WindGame.after(5, lambda: RecursionMovAplastaDer(Aplasta))#Llamada recursiva


        def RecursionMovAplastaIzq(Aplasta): #Movimiento del enemigo aplastador hacia la izquierda
            global coordAplasta, SCORE, Hp, Tiempo
            
            coordAplasta = C_Juego.coords(Aplasta)
            
            if Tiempo == 0 or Hp <= 0:
                coordAplasta=[0,0]
                C_Juego.delete(Aplasta)
                return
            else:
                if (coordAplasta[0] >= CoordSlayer[0]) and (coordAplasta[0] <= CoordSlayer[0]+50) and (coordAplasta[1]>= CoordSlayer[1]) and (coordAplasta[1]<=CoordSlayer[1]+124):#Colicion del enemigo Aplastador con el personaje
                    Hp -= 1
                    coordAplasta = [0,0]
                    C_Juego.delete(Aplasta)
                    return
                else:
                    if coordAplasta[0] <= 5:
                        Thread(target = DisparoRecursivoAplasta(coordAplasta, 2))
                        C_Juego.delete(Aplasta)
                        SCORE+=2
                        return
                    else:
                        C_Juego.coords(Aplasta,coordAplasta[0]-2, coordAplasta[1])#Movimiento del objeto
                        WindGame.after(5, lambda: RecursionMovAplastaIzq(Aplasta))#Llamada recursiva


        def DisparoRecursivoAplasta(Coordenada, Direccion): #Funcion encargada de la creacion del proyectil del enemigo aplastador cuando este llega a un extremo de la pantalla
            global AplastaBullet
            AplastaBullet = Coordenada

            BulletAplasta = C_Juego.create_image(AplastaBullet[0],AplastaBullet[1], anchor = NW, image = AplastaBala)

            RecusionBalaAplasta(BulletAplasta, Direccion)

        def RecusionBalaAplasta(BulletAplasta, Direccion): #Movimiento del proyectil
            global AplastaBullet, Hp, Tiempo
            AplastaBullet =  C_Juego.coords(BulletAplasta)


            if Tiempo == 0 or Hp <= 0:
                C_Juego.delete(BulletAplasta)
                return
            else:
                if (AplastaBullet[0] >= CoordSlayer[0]) and (AplastaBullet[0] <= CoordSlayer[0]+60) and (AplastaBullet[1] >= CoordSlayer[1]) and (AplastaBullet[1] <=CoordSlayer[1]+124): #Colision del proyectil del aplastador y el personaje
                    Hp -= 1
                    C_Juego.delete(BulletAplasta)
                    return
                else:
                    if Direccion == 1:
                        if AplastaBullet[0] <= 5:
                            C_Juego.delete(BulletAplasta)
                            return
                        else:
                            C_Juego.coords(BulletAplasta,AplastaBullet[0]-2, AplastaBullet[1])#Movimiento del objeto
                            WindGame.after(5, lambda: RecusionBalaAplasta(BulletAplasta,Direccion))#Llamada recursiva
                    else:
                        if AplastaBullet[0] >= 850:
                            C_Juego.delete(BulletAplasta)
                            return
                        else:
                            C_Juego.coords(BulletAplasta,AplastaBullet[0]+2, AplastaBullet[1])#Movimiento del objeto
                            WindGame.after(5, lambda: RecusionBalaAplasta(BulletAplasta,Direccion))#Llamada recursiva

#***************Acciones de enemigos*********************




#***************Acciones del personaje*********************
            
        def MovDoom(event): 
            """
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
            """

            def MovDoomUp(): #Realiza el salto del personaje

                coordSlayer = C_Juego.coords(Slayer) #Coordenada del pesonaje controlado
                
                global CoordSlayer
                CoordSlayer = coordSlayer
                
                if coordSlayer[1] <= 426: #Limite del salto
                    C_Juego.coords(Slayer, coordSlayer[0], 466)
                    MovDoomDown() #Llamada a la funcion de caída del personaje
                else:
                    C_Juego.coords(Slayer, coordSlayer[0], coordSlayer[1]-2)
                    WindGame.after(1, lambda:MovDoomUp())


            def MovDoomDown(): #Caída del personaje
                
                coordSlayer = C_Juego.coords(Slayer)#Coordenada del pesonaje controlado

                global CoordSlayer
                CoordSlayer = coordSlayer
                
                if coordSlayer[1] >= 656:
                    C_Juego.coords(Slayer, coordSlayer[0], 666)
                else:
                    C_Juego.coords(Slayer, coordSlayer[0], coordSlayer[1]+2)
                    WindGame.after(1, lambda:MovDoomDown())


            def DisparoDoom():
                
                coordSlayer = C_Juego.coords(Slayer) #Coordenada del personaje
                ShotSlayer = C_Juego.create_image(coordSlayer[0]+28,coordSlayer[1]-50, anchor = NW , image =C_Juego.ShotSlayer) #Posicionamiento del disparo con respecto al personaje
                

                def RecursionMovBullet():
                    coordBullet = C_Juego.coords(ShotSlayer)
                    global CoordBullet
                    global Valor
                    Valor = False
                    CoordBullet = coordBullet
                    
                    if coordBullet[1] <= 0 or ((CoordBullet[0]+10) <= (CoordEnemy[0]+150) and (CoordBullet[0]+10) >= (CoordEnemy[0]+40) and (CoordBullet[1]) <= (CoordEnemy[1]+154) and (CoordBullet[1]) >= (CoordEnemy[1]+46)) or (CoordBullet[0]+10 >= coordAplasta[0]+5 and CoordBullet[0]+10 <= coordAplasta[0]+65 and CoordBullet[1] >= coordAplasta[1] and CoordBullet[1] <= coordAplasta[1]+70) or (CoordBullet[0]+10 >= coordMisil[0] + 10 and CoordBullet[0]+10 <= coordMisil[0] + 40 and CoordBullet[1] >= coordMisil[1] + 20 and CoordBullet[1] <= coordMisil[1] + 60):#Colision del proyectil
                        CoordBullet = [0,0]
                        C_Juego.delete(ShotSlayer)
                    else:
                        C_Juego.coords(ShotSlayer, CoordBullet[0], CoordBullet[1]-3)
                        WindGame.after(5, lambda: RecursionMovBullet())
                        
                Thread(target = RecursionMovBullet()).start() #Llamada a la funcion recursiva que realiza el movimiento de la bala

#***************Acciones del personaje*********************

            
            global CoordSlayer, CoordBullet, Salto, Derecha, Izquierda, Disparo
            
            CoordSlayer = C_Juego.coords(Slayer) #Registro de la posicion del personaje
            
            if (event.char).upper() == Izquierda: #Al ser presionada la tecla el personaje se mueve a la izquierda
                if CoordSlayer[0] >= 5: #Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego
                    
                    C_Juego.coords(Slayer, CoordSlayer[0]-12, CoordSlayer[1])#Movimiento del personaje a la izquierda
                    
                    
                    
            elif(event.char).upper() == Derecha:#Al ser presionada la tecla el personaje se mueve a la derecha
                if CoordSlayer[0] <= 850:#Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego

                    C_Juego.coords(Slayer, CoordSlayer[0]+12, CoordSlayer[1])#Movimiento del personaje a la derecha
                    
                    
            elif(event.char).upper() == Salto: #Al ser presionada la tecla el personaje salta
                if CoordSlayer[1] >= 656: #No puede saltar hasta que llegue a la coordenada y = 656
                    Thread(target = MovDoomUp()).start() #Llamada al salto
                
            elif (event.char).upper() == Disparo: #Tecla de disparo
                    if CoordBullet[1] <= 500: #Si el proyectil disparado no supera la coordenada y = 500 entonces no se podrá disparar de nuevo
                        Thread(target=DisparoDoom()).start() #Llamada al disparo
                
        #End MovDoom        
                
        
        global ShotSlayer, C_Juego, Misil, Aplasta, Tiempo, Dificultad, Hp, CoordBullet, coordSlayer, SCORE, CoordSlayer, CoordBullet, CoordEnemy, coordAplasta, AplastaBullet,coordMisil, Vivo, lb_Tiempo, lb_SCORE, lb_Vida, Salto, Derecha, Izquierda, Disparo

        CoordSlayer = [0,0]
        CoordBullet = [0,0]
        CoordEnemy  = [9001,9050]
        coordAplasta = [9002,9040]
        AplastaBullet = [9003,9020]
        coordMisil = [9004,9100]
        Vivo = True
        SCORE = 0
        Hp = 3
        Tiempo = 40

        
        if Lvl == 1.5:
            Dificultad = 1.25
        elif Lvl == 1:
            Dificultad = 1
        else:
            Dificultad = 0.75

        
        C_Juego = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Juego.place(x=0, y=0)
        
        C_Juego.Campo = General.cargarImg2('Escenario.png') #Creacion del escenario del juego
        Campo = C_Juego.create_image(0,0, anchor = NW , image =C_Juego.Campo)




        C_Juego.Slayer = General.cargarImg2('Slayer\Slayer1.png') #Creación del personaje que el jugador opera
        Slayer = C_Juego.create_image(400,666,anchor = NW, image =C_Juego.Slayer)

       

        
        

        C_Juego.Demon = General.cargarImg2('Demon\DemonR.png') #Creacion del enemigo simple

        C_Juego.ShotSlayer = General.cargarImg2('Slayer\Shot.png') #Creación del disparo

        C_Juego.Misil = General.cargarImg2('Demon\FF.png')#Creacion del enemigo simple

        C_Juego.Aplasta = General.cargarImg2('Demon\C.png')#Creacion del enemigo simple

        C_Juego.ShotEnemy = General.cargarImg2('Demon\DemonShot2.png')#Creacion del enemigo simple


        lb_Tiempo = Label(C_Juego, text = ("Tiempo =  " + str(Tiempo) + " segundos"), bg ='Black', fg = 'Red', font ="Arial 13")
        lb_Tiempo.place(x=0,y=0)

        lb_SCORE = Label(C_Juego, text = ("Score =  " + str(SCORE) + " pts"), bg ='Black', fg = 'Red', font ="Arial 13")
        lb_SCORE.place(x=200, y = 0)

        lb_Vida = Label(C_Juego, text = ("H.P =  " + str(Hp)), bg ='Black', fg = 'Red', font ="Arial 13")
        lb_Vida.place(x=400, y = 0)

        ln_Name = Label(C_Juego, text = ("Jugador  " + Name), bg ='Black', fg = 'Red', font ="Arial 13")
        ln_Name.place(x=600, y = 0)

        #Llamada de funciones
    

        C_Juego.bind("<KeyPress>", MovDoom) #Llamada a la funcion que contiene las acciones del personaje
        C_Juego.focus_set() #Hace que el Canvas se enfoque en la accion a realizar por parte de la tecla
        
        
        def Timer(): #Temporizador de 40 segundos
            global Tiempo, Hp
            if Tiempo == 0 or Hp <= 0:
                return
            else:
                Tiempo-=1
                WindGame.after(1000,lambda:Timer())
                
        Thread(target = Timer()).start()
        

        def TimerVidaYPuntuacion(): #La funcion actualiza el tiempo, vida y puntuacion del jugador
            global Tiempo, SCORE, Hp, lb_Tiempo, lb_SCORE, lb_Vida

            lb_Vida.config(text= ("H.P = " + str(Hp)), bg ='Black', fg = 'Red', font ="Arial 13")

            lb_SCORE.config(text= ("Score = " + str(SCORE) + " pts"), bg ='Black', fg = 'Red', font ="Arial 13")

            lb_Tiempo.config(text= ("Tiempo = " + str(Tiempo) + " segundos"), bg ='Black', fg = 'Red', font ="Arial 13")


            if Hp <=0: #Si la vida del jugador llega a 0 el juego termina
                General.GameOver(Name, SCORE, "Derrota")
            elif Tiempo == 0:#Si el tiempo a 0 el juego termina
                General.GameOver(Name, SCORE, "Victoria")
            else:
                WindGame.after(10,lambda:TimerVidaYPuntuacion())
        Thread(target=TimerVidaYPuntuacion()).start()
        
      
        def GeneraEnemigos(): #Funcion que genera un thread que lleva a la creacion de los patrones de movimiento de los enemigos simples, y sus cantidad con respecto al tiempo
            global Tiempo, Hp

            if Tiempo==0 or Hp <= 0:
                return
            else:
                Thread(target = Enemigo(C_Juego.Demon, C_Juego.ShotEnemy)).start()
                WindGame.after(int(4000*Dificultad), lambda: GeneraEnemigos())
            
        Thread(target = GeneraEnemigos()).start()

        def GeneraMisiles(): #Funcion que genera un thread que lleva a la creacion de los misiles
            global Tiempo, Hp
                
            if Tiempo==0 or Hp <= 0:
                return
            else:
                Thread(target = Enemigo2(C_Juego.Misil)).start()
                WindGame.after(int(2000*Dificultad), lambda: GeneraMisiles())

        Thread(target = GeneraMisiles()).start()

        def GeneraAplasta(): #Funcion que genera un thread que lleva a la creacion del enemigo aplastador
            global Tiempo, Hp

            if Tiempo==0 or Hp <= 0:
                return
            else:
                X = (random.randrange(1,3))
                Thread(target = Enemigo3(C_Juego.Aplasta ,X ,C_Juego.ShotEnemy)).start()
                WindGame.after(int(7000*Dificultad), lambda: GeneraAplasta())
                   
        Thread(target = GeneraAplasta()).start()

        

        if Hp != 3: #Cuando el programa se inicializa, a veces la vida del personaje aparece en 2 o en 1, esta instruccion evita que esto suceda
            Hp = 3
        
        
        #Llamada de funciones

    #End InterfazJuego

        
#End Class General
            
General.Principal()


















