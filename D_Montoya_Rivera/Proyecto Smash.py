
from tkinter import *
import os
import pygame
from threading import Thread
from tkinter import messagebox
import random

import player1Controles
import player2Controles
import player3Controles
import player4Controles
"""
from player2Controles import *
from player3Controles import *
"""

class General: #La clase contiene todas las interfaces presentes en el menu, con sus respectivos botones.

    global CoordBullet, CoordSlayer, CoordEnemy,coordMisil, coordAplasta, Misil, Aplasta, Vivo, AplastaBullet, SCORE, Tiempo,  PlayOrNot, Hp, Salto, Derecha, Izquierda, Disparo   #Variables globales correspondientes a las coordenadas de los objetos del juego
    global player1, player2, player3, player4

    player1 = player1Controles.Controles()
    player2 = player2Controles.Controles()
    player3 = player3Controles.Controles()
    player4 = player4Controles.Controles()
    
    
    

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
        General.SmashInteface(4)
        #General.Menu()
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

        global Gamers

        C_Play = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Play.place(x=0, y=0)

        C_Play.image1 = General.cargarImg2('InterfazMenu.png') #Background
        imgCanvas = C_Play.create_image(0,0, anchor = NW , image =C_Play.image1)

        #Labels de los jugadores
        
        Lb_Nombre1 = Label(C_Play, text= 'Player 1 Name', bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13), height = 1, width = 13 )
        Lb_Nombre1.place_forget()
        
        Lb_Nombre2 = Label(C_Play, text= 'Player 2 Name', bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13), height = 1, width = 13 )
        Lb_Nombre2.place_forget()
        
        Lb_Nombre3 = Label(C_Play, text= 'Player 3 Name', bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13), height = 1, width = 13 )
        Lb_Nombre3.place_forget()

        Lb_Nombre4 = Label(C_Play, text= 'Player 4 Name', bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13), height = 1, width = 13 )
        Lb_Nombre4.place_forget()

        #Entradas de los nombres de los jugadores
        
        En_Nombre1 = Entry(C_Play)
        En_Nombre1.place_forget()
        
        En_Nombre2 = Entry(C_Play)
        En_Nombre2.place_forget()
        
        En_Nombre3 = Entry(C_Play)
        En_Nombre3.place_forget()

        En_Nombre4 = Entry(C_Play)
        En_Nombre4.place_forget()


        #Botones de selección de jugadores, ingreso al juego y retroceso
        
        btn_Go1 = Button(C_Play, text = '2 Players', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:Play_aux(C_Play,2), font =("Goudy Stout", 13))
        btn_Go1.place(x = 200, y = 400)

        btn_Go2 = Button(C_Play, text = '3 Players', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:Play_aux(C_Play,3), font =("Goudy Stout", 13))
        btn_Go2.place(x = 600, y = 400)

        btn_Go3 = Button(C_Play, text = '4 Players', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:Play_aux(C_Play,4), font =("Goudy Stout", 13))
        btn_Go3.place(x = 1000, y = 400)
        
        btn_Return = Button(C_Play, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 1200, y = 700 )

        btn_Play = Button(C_Play, text = 'Lets play!', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:ValidaTexto(En_Nombre1.get().strip(),En_Nombre2.get().strip(),En_Nombre3.get().strip(),En_Nombre4.get().strip(), Gamers), font =("Goudy Stout", 13))
        btn_Play.place_forget()
        
        



        #Labels de error

        lb_Error = Label(C_Play, text= 'El nombre no puede estar vacío', bg ='Black', fg = 'Red', font ="Arial 13")
        lb_Error.place_forget()

        lb_Error2 = Label(C_Play, text= 'El nombre no debe exeder la cantidad de caracteres máximos (11)', bg ='Black', fg = 'Red', font ="Arial 13")
        lb_Error2.place_forget()
        

        



        def Play_aux(C_Play,Jugadores):
            global Gamers
            Gamers = Jugadores

            btn_Play.place(x=1200, y = 500)
            btn_Go1.place_forget()
            btn_Go2.place_forget()
            btn_Go3.place_forget()

                
            Lb_Nombre1.place(x=100, y = 100)
            En_Nombre1.place(x = 420, y = 105)

            Lb_Nombre2.place(x=100, y = 300)
            En_Nombre2.place(x =420, y = 305)

            if Jugadores == 3:
                
                Lb_Nombre3.place(x=100, y = 500)
                En_Nombre3.place(x=420, y = 505)

            elif Jugadores == 4:

                Lb_Nombre3.place(x=100, y = 500)
                En_Nombre3.place(x=420, y = 505)

                Lb_Nombre4.place(x=100, y = 700)
                En_Nombre4.place(x=420, y = 705)

                


        def ValidaTexto(Jugador1, Jugador2, Jugador3,Jugador4, Jugadores):

            if Jugadores == 2:
                if not Jugador1 or not Jugador2:
                    MuestraErrores(1)
                elif len(Jugador1) > 11 or len(Jugador2) > 11 :
                    MuestraErrores(2)
                else:
                    EscondeErrores()
                    print("Funca 2")
                    General.SmashInteface(Jugadores)
            elif Jugadores == 3:
                if not Jugador1 or not Jugador2 or not Jugador3:
                    MuestraErrores(1)
                elif (len(Jugador1) > 11 or len(Jugador2) > 11 or len(Jugador3) > 11):
                    MuestraErrores(2)
                else:
                    EscondeErrores()
                    print("Funca 3")
                    General.SmashInteface(Jugadores)
            elif Jugadores == 4:
                if not Jugador1 or not Jugador2 or not Jugador3 or not Jugador4:
                    MuestraErrores(1)
                elif (len(Jugador1) > 11 or len(Jugador2) > 11 or len(Jugador3) > 11 or len(Jugador4) > 11):
                    MuestraErrores(2)
                else:
                    EscondeErrores()
                    print("Funca 4")
                    General.SmashInteface(Jugadores)
                    

        def MuestraErrores(Num):

            if Num == 1:
                lb_Error2.place_forget()
                lb_Error.place(x=745, y = 180)
            else:
                lb_Error.place_forget()
                lb_Error2.place(x=550, y = 180)

        def EscondeErrores():
            lb_Error2.place_forget()
            lb_Error.place_forget()
                
                         
        
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

        global Salto, Derecha, Izquierda, Disparo, player
        
        C_Help = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_Help.place(x=0,y=0)
        
        C_Help.image1 = General.cargarImg2('InterfazMenu.png')#Background 
        imgCanvas = C_Help.create_image(0,0, anchor = NW , image =C_Help.image1)

        player = 0


        

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

        #Efecto
        lb_Efecto = Label(C_Help, text = 'EFECTO:' , bg = 'White', fg = 'black', font = "Arial 12")
        lb_Efecto.place_forget()
        
        lb_TeclaEfecto = Label(C_Help, text = Disparo , bg = 'White', fg = 'black', font = "Arial 12")
        lb_TeclaEfecto.place_forget()

        en_Efecto = Entry(C_Help)
        en_Efecto.place_forget()

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

        #Labels de error
        lB_ErrorInput =  Label(C_Help, text= 'La entrada no puede estar vacía | Las teclas NO pueden ser las mismas | Solo puede ser 1 caracter', bg ='Black', fg = 'Red', font ="Arial 16")
        
        
        #Botones de la interfaz de ayuda
        
        btn_Change = Button(C_Help, text = 'Save Changes', bg = 'black', fg = 'Yellow', height = 1, width = 13, font =("Goudy Stout", 13),command = lambda: CambioControles((en_Efecto.get()).upper(), (en_MoverIzq.get()).upper(),(en_MoverDer.get()).upper() , (en_Salto.get()).upper())) #Se encarga de cambiar los contrles 
        btn_Change.place_forget()                                                                                                                       #def CambioControles(Efect, Left, Right, Jump): #Evalúa que la edición de teclas sea correcta

        btn_Player1 = Button(C_Help, text = 'Jugador 1', bg = 'black', fg = 'Yellow', height = 1, width = 13, font =("Goudy Stout", 13),command = lambda:(SetVisibleControles(),
                                                                                                                                                          lb_Ayuda.place_forget(),
                                                                                                                                                          MuestraControles(player1.efecto,player1.izquierda,player1.derecha,player1.salto,1))) #Se encarga de cambiar los contrles 
        btn_Player1.place_forget()
                                                                                                                                                        
        btn_Player2 = Button(C_Help, text = 'Jugador 2', bg = 'black', fg = 'Yellow', height = 1, width = 13, font =("Goudy Stout", 13),command = lambda: (SetVisibleControles(),
                                                                                                                                                          lb_Ayuda.place_forget(),
                                                                                                                                                          MuestraControles(player2.efecto,player2.izquierda,player2.derecha,player2.salto,2))) #Se encarga de cambiar los contrles 
        btn_Player2.place_forget()

        btn_Player3 = Button(C_Help, text = 'Jugador 3', bg = 'black', fg = 'Yellow', height = 1, width = 13, font =("Goudy Stout", 13),command = lambda: (SetVisibleControles(),
                                                                                                                                                          lb_Ayuda.place_forget(),
                                                                                                                                                          MuestraControles(player3.efecto,player3.izquierda,player3.derecha,player3.salto,3))) #Se encarga de cambiar los contrles 
        btn_Player3.place_forget()

        btn_Player4 = Button(C_Help, text = 'Jugador 4', bg = 'black', fg = 'Yellow', height = 1, width = 13, font =("Goudy Stout", 13),command = lambda: (SetVisibleControles(),
                                                                                                                                                          lb_Ayuda.place_forget(),
                                                                                                                                                          MuestraControles(player4.efecto,player4.izquierda,player4.derecha,player4.salto,4))) #Se encarga de cambiar los contrles 
        btn_Player4.place_forget()
        

        
        btn_Controles = Button(C_Help, text = 'Controles', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda:(SetInvisibleControles(),
                                                                                                                                  lb_Ayuda.place_forget(),
                                                                                                                                  btn_Player1.place(x=900, y = 100),
                                                                                                                                  btn_Player2.place(x=900, y = 150),
                                                                                                                                  btn_Player3.place(x=900, y = 200),
                                                                                                                                  btn_Player4.place(x=900, y = 250)),  font =("Goudy Stout", 13))# Se encarga de mostrar los controles
        btn_Controles.place(x = 1200 , y = 100)
        
        btn_Objetivo = Button(C_Help, text = 'Objectivo', bg = 'black', fg = 'Yellow', height = 1, width = 13, command = lambda: (SetInvisibleControles(),
                                                                                                                                  lb_Ayuda.place(x=100,y=100),
                                                                                                                                  btn_Player1.place_forget(),
                                                                                                                                  btn_Player2.place_forget(),
                                                                                                                                  btn_Player3.place_forget(),
                                                                                                                                  btn_Player4.place_forget(),
                                                                                                                                  lB_ErrorInput.place_forget()), font =("Goudy Stout", 13))# Se encarga de mostrar el objetivo del juego 
        btn_Objetivo.place(x = 1200, y = 500 )


        
        
        btn_Return = Button(C_Help, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 1200, y = 700 )


        def SetVisibleControles():
            
            lb_Salto.place(x = 10, y = 100)
            lb_TeclaSalto.place(x = 300, y = 100)
            en_Salto.place(x=400, y = 100)

            lb_Efecto.place(x = 10, y = 200)
            lb_TeclaEfecto.place(x = 300, y = 200)
            en_Efecto.place(x=400, y = 200)
            
            lb_MoverIzq.place(x = 10, y = 300)
            lb_TeclaMoverIzq.place(x = 300, y = 300)
            en_MoverIzq.place(x=400, y = 300)
            
            lb_MoverDer.place(x = 10, y = 400)
            lb_TeclaMoverDer.place(x = 300, y = 400)
            en_MoverDer.place(x=400, y = 400)
            
            btn_Change.place(x = 1200 , y = 300)

        def SetInvisibleControles():
            lb_Salto.place_forget()
            lb_TeclaSalto.place_forget()
            en_Salto.place_forget()
            lb_Efecto.place_forget()
            lb_TeclaEfecto.place_forget()
            en_Efecto.place_forget()
            lb_MoverIzq.place_forget()
            lb_TeclaMoverIzq.place_forget()
            en_MoverIzq.place_forget()
            lb_MoverDer.place_forget()
            lb_TeclaMoverDer.place_forget()
            en_MoverDer.place_forget()
            btn_Change.place_forget()
            


        def MuestraControles(Efect, Left, Right, Jump, Number):
            global player
            player = Number

            print(player)
            
            lb_TeclaSalto.config(text = Jump , bg = 'White', fg = 'black', font = "Arial 12")
            
            lb_TeclaEfecto.config(text = Efect , bg = 'White', fg = 'black', font = "Arial 12")

            lb_TeclaMoverIzq.config(text = Left , bg = 'White', fg = 'black', font = "Arial 12")

            lb_TeclaMoverDer.config(text = Right , bg = 'White', fg = 'black', font = "Arial 12")


        def CambioControles(Efect, Left, Right, Jump): #Evalúa que la edición de teclas sea correcta

            global Salto, Derecha, Izquierda, Disparo

            if len(Efect) > 1 or len(Left) > 1 or len(Right) > 1 or len(Jump) > 1:
                lB_ErrorInput.config(text= 'SOLO puede ser 1 caracter', bg ='Black', fg = 'Red', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
            elif Efect == Left or Efect == Jump or Efect == Right or Left == Jump or Left == Right or Jump == Right:
                lB_ErrorInput.config(text= 'Las teclas NO pueden ser las mismas', bg ='Black', fg = 'Red', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
            elif len(Efect) == 0 or len(Left)  == 0 or len(Jump)  == 0 or len(Right)  == 0 :
                lB_ErrorInput.config(text= 'La entrada NO puede estar vacía', bg ='Black', fg = 'Red', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
            elif not ValidaControles(Efect, Left, Right, Jump):
                lB_ErrorInput.config(text= 'Los controles no deben coincidir con alguno de los controles de los demás jugadores', bg ='Black', fg = 'Red', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
                
            else:
                if player == 1:
                    player1.efecto = Efect
                    player1.izquierda = Left
                    player1.derecha = Right
                    player1.salto = Jump
                    print("Estuve en 1")
                elif player == 2:
                    player2.efecto = Efect
                    player2.izquierda = Left
                    player2.derecha = Right
                    player2.salto = Jump
                    print("Estuve en 2")
                elif player == 3:
                    player3.efecto = Efect
                    player3.izquierda = Left
                    player3.derecha = Right
                    player3.salto = Jump
                    print("Estuve en 3")
                elif player == 4:
                    player4.efecto = Efect
                    player4.izquierda = Left
                    player4.derecha = Right
                    player4.salto = Jump
                    print("Estuve en 4")
                    
                    
                Salto=Jump
                Derecha=Right
                Disparo=Efect
                Izquierda=Left

                print ("Salto1: ",player1.salto, "     Salto2: ",player2.salto, "     Salto3: ",player3.salto, "     Salto4: ",player4.salto)
                print("Derecha1: ",player1.derecha,"    Derecha2: ",player2.derecha,"    Derecha3: ",player3.derecha,"    Derecha4: ",player4.derecha)
                print("Efecto1: ",player1.efecto,"     Efecto2: ",player2.efecto,"    Efecto3: ",player3.efecto,"    Efecto4: ",player4.efecto)
                print("Izquierda1: ", player1.izquierda,"     Izquierda2: ", player2.izquierda,"     Izquierda3: ", player3.izquierda,"     Izquierda4: ", player4.izquierda)
                                
                lb_TeclaSalto.config(text = Salto , bg = 'White', fg = 'black', font = "Arial 12")
                
                lb_TeclaEfecto.config(text = Disparo , bg = 'White', fg = 'black', font = "Arial 12")

                lb_TeclaMoverIzq.config(text = Izquierda , bg = 'White', fg = 'black', font = "Arial 12")

                lb_TeclaMoverDer.config(text = Derecha , bg = 'White', fg = 'black', font = "Arial 12")

                
                lB_ErrorInput.config(text= 'Cambios realizados exitósamente', bg ='Black', fg = 'Green', font ="Arial 13")
                lB_ErrorInput.place(x = 100, y = 500)
                return


        def ValidaControles(Efect, Left, Right, Jump):
            Condicion = True
            

            ListaControles = [player1.efecto,player1.izquierda,player1.derecha,player1.salto,player2.efecto,player2.izquierda,player2.derecha,player2.salto,player3.efecto,player3.izquierda,player3.derecha,player3.salto,player4.efecto,player4.izquierda,player4.derecha,player4.salto]

            while ListaControles != []:
                if ListaControles[0] == Efect or ListaControles[0] == Left or ListaControles[0] == Right or ListaControles[0] == Jump:
                    Condicion = False
                    ListaControles = []
                else:
                    ListaControles = ListaControles[1:]
            
            return Condicion

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
















































    def SmashInteface(Players):

        global CoordSlayer1, CoordSlayer2, CoordSlayer3, CoordSlayer4, Condicion1, Condicion2, Condicion3, Condicion4, Tiempo, Build, Slayer1, Slayer2, Slayer3, Slayer4, Caida1, Caida2, Caida3, Caida4, Escudo1, Escudo2, Escudo3, Escudo4, CantPlayers

        CantPlayers = Players

        CoordSlayer1 = [0,0]
        CoordSlayer1 = [100,100]
        CoordSlayer1 = [200,200]
        CoordSlayer1 = [300,300]
        
        Condicion1=True
        Condicion2=True
        Condicion3=True
        Condicion4=True

        Caida1=True
        Caida2=True
        Caida3=True
        Caida4=True

        Escudo1=False
        Escudo2=False
        Escudo3=False
        Escudo4=False
        
        Tiempo = 300
        Build  = ""
        X = 0


        

        

        print("El numero de jugadores es: ", Players, " jugadores")
        
        C_Juego = Canvas(WindGame, width = 1200 , height = 800, bg = 'green')
        C_Juego.place(x=0, y=0)
        
        C_Objetivos = Canvas(WindGame, width = 300 , height = 800, bg = 'black')
        C_Objetivos.place(x=1200, y=0)
        
        C_Juego.Campo = General.cargarImg2('Escenario.png') #Creacion del escenario del juego
        Campo = C_Juego.create_image(0,50, anchor = NW , image = C_Juego.Campo)

        #C_Objetivos.Campo = General.cargarImg2('Escenario.png') #Creacion del campo de las misiones
        #Campo2 = C_Objetivos.create_image(0,0, anchor = NW , image =C_Objetivos.Campo)


        #Label para los árboles
        lb_P1 = Label(C_Objetivos, text= ("Player 1 Tree "), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_P1.place(x=0 , y = 0)
        
        lb_P2 = Label(C_Objetivos, text= ("Player 2 Tree "), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_P2.place(x=0 , y = 200)
        
        lb_P3 = Label(C_Objetivos, text= ("Player 3 Tree "), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_P3.place(x=0 , y = 400)
        
        lb_P4 = Label(C_Objetivos, text= ("Player 4 Tree "), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_P4.place(x=0 , y = 600)
        #Label para los árboles


        #Label del Objetivo y Tiempo del juego

        lb_ObjetivoTime = Label(C_Juego, text= ("Tiempo:" , Tiempo, "Build:", Build), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10), height = 3, width=75)
        lb_ObjetivoTime.place(x=0 , y = 0) 


        def GeneraRandom(Num):
            X = (random.randint(1,Num))
            return X

        def MovDoom(event):
            
                    #Movimiento del Jugador 1
                    def MovDoomUp(CordY): #Realiza el salto del personaje

                        global CoordSlayer1, Condicion1
                        
                        coordSlayer1 = CoordSlayer1 #Coordenada del pesonaje controlado
                        
                        
                        if CordY >= 250: #Limite del salto
                            MovDoomDown(CordY) #Llamada a la funcion de caída del personaje
                        else:
                            C_Juego.coords(Slayer1, coordSlayer1[0], coordSlayer1[1]-4)
                            WindGame.after(7, lambda:MovDoomUp(CordY+2))


                    def MovDoomDown(CordY): #Caída del personaje
                        global CoordSlayer1,Condicion1, Caida1
                        
                        coordSlayer1 = CoordSlayer1

                        if Caida1 == True:
                            Condicion1 = False
                            WindGame.after(5, lambda:MovDoomDown(CordY))
                        elif CordY <= 0 or Caida1 == False:
                            Condicion1 = True
                        else:
                            C_Juego.coords(Slayer1, coordSlayer1[0], coordSlayer1[1]+2)
                            WindGame.after(5, lambda:MovDoomDown(CordY-2))


                    def ActivarEfecto():
                        global CoordSlayer2, CoordSlayer3, CoordSlayer4, Escudo1, Escudo2, Escudo3, Escudo4
                        if player1.poder == "Force":
                            player1.poder=""
                            if Players == 2:
                                if not Escudo2:
                                    C_Juego.coords(Slayer2,CoordSlayer2[0]+100, CoordSlayer2[1])
                                else:
                                    print("El jugador 2 tiene escudo activo")
                            elif Players == 3:
                                y = GeneraRandom(2)
                                if y == 2:
                                    if not Escudo2:
                                        C_Juego.coords(Slayer2,CoordSlayer2[0]+100, CoordSlayer2[1])
                                    else:
                                        print("El jugador 2 tiene escudo activo")
                                else:
                                    if not Escudo3:
                                        C_Juego.coords(Slayer3,CoordSlayer3[0]+100, CoordSlayer3[1])
                                    else:
                                        print("El jugador 3 tiene escudo activo")
                            elif Players == 4:
                                y = GeneraRandom(3)
                                if y == 1:
                                    if not Escudo2:
                                        C_Juego.coords(Slayer2,CoordSlayer2[0]+100, CoordSlayer2[1])
                                    else:
                                        print("El jugador 2 tiene escudo activo")
                                elif y == 2:
                                    if not Escudo3:
                                        C_Juego.coords(Slayer3,CoordSlayer3[0]+100, CoordSlayer3[1])
                                    else:
                                        print("El jugador 3 tiene escudo activo")
                                else:
                                    if not Escudo4:
                                        C_Juego.coords(Slayer4,CoordSlayer4[0]+100, CoordSlayer4[1])
                                    else:
                                        print("El jugador 4 tiene escudo activo")
                                    
                        elif player1.poder == "Shield":
                            player1.poder = ""
                            ActivaEscudo(1)
                        elif player1.poder == "Jump":
                            player1.poder = ""
                            CoordX = (random.randint(360,1000))
                            C_Juego.coords(Slayer1,CoordX,50)
                        else:
                            print("1, No tienes ningún efecto activo")
                        
                    #Movimiento del Jugador 1



                        


                    #Movimiento del Jugador 2
                    def MovDoomUp2(CordY): #Realiza el salto del personaje

                        global CoordSlayer2, Condicion2
                        
                        coordSlayer2 = CoordSlayer2
                        
                        if CordY >= 250: #Limite del salto
                            MovDoomDown2(CordY) #Llamada a la funcion de caída del personaje
                        else:
                            C_Juego.coords(Slayer2, coordSlayer2[0], coordSlayer2[1]-4)
                            WindGame.after(7, lambda:MovDoomUp2(CordY+2))


                    def MovDoomDown2(CordY): #Caída del personaje
                        global CoordSlayer2,Condicion2, Caida2
                        
                        coordSlayer2 = CoordSlayer2 

                        if Caida2==True:
                            Condicion2 = False
                            WindGame.after(5, lambda:MovDoomDown2(CordY))
                        elif CordY <= 0 or Caida2 == False:
                            Condicion2 = True
                        else:
                            C_Juego.coords(Slayer2, coordSlayer2[0], coordSlayer2[1]+2)
                            WindGame.after(5, lambda:MovDoomDown2(CordY-2))

                    def ActivarEfecto2():
                        global CoordSlayer1, CoordSlayer3, CoordSlayer4, Escudo1, Escudo2, Escudo3, Escudo4
                        if player2.poder == "Force":
                            player2.poder=""
                            if Players == 2:
                                if not Escudo1:
                                    C_Juego.coords(Slayer1,CoordSlayer1[0]+100, CoordSlayer1[1])
                                else:
                                    print("El jugador 1 tiene escudo activo")
                            elif Players == 3:
                                y = GeneraRandom(2)
                                if y == 1:
                                    if not Escudo1:
                                        C_Juego.coords(Slayer1,CoordSlayer1[0]+100, CoordSlayer1[1])
                                    else:
                                        print("El jugador 1 tiene escudo activo")
                                else:
                                    if not Escudo3:
                                        C_Juego.coords(Slayer3,CoordSlayer3[0]+100, CoordSlayer3[1])
                                    else:
                                        print("El jugador 3 tiene escudo activo")
                            elif Players == 4:
                                y = GeneraRandom(3)
                                if y == 1:
                                    if not Escudo1:
                                        C_Juego.coords(Slayer1,CoordSlayer1[0]+100, CoordSlayer1[1])
                                    else:
                                        print("El jugador 1 tiene escudo activo")
                                elif y == 2:
                                    if not Escudo3:
                                        C_Juego.coords(Slayer3,CoordSlayer3[0]+100, CoordSlayer3[1])
                                    else:
                                        print("El jugador 3 tiene escudo activo")
                                else:
                                    if not Escudo4:
                                        C_Juego.coords(Slayer4,CoordSlayer4[0]+100, CoordSlayer4[1])
                                    else:
                                        print("El jugador 4 tiene escudo activo")
                                    
                        elif player2.poder == "Shield":
                            player2.poder = ""
                            ActivaEscudo(2)
                        elif player2.poder == "Jump":
                            player2.poder = ""
                            CoordX = (random.randint(360,1000))
                            C_Juego.coords(Slayer2,CoordX,50)
                        else:
                            print("2, No tienes ningún efecto activo")

                    #Movimiento del Jugador 2


                    #Movimiento del Jugador 3
                    def MovDoomUp3(CordY): #Realiza el salto del personaje

                        global CoordSlayer3, Condicion3
                        
                        coordSlayer3 = CoordSlayer3
                        
                        if CordY >= 250: #Limite del salto
                            MovDoomDown3(CordY) #Llamada a la funcion de caída del personaje
                        else:
                            C_Juego.coords(Slayer3, coordSlayer3[0], coordSlayer3[1]-4)
                            WindGame.after(7, lambda:MovDoomUp3(CordY+2))


                    def MovDoomDown3(CordY): #Caída del personaje
                        global CoordSlayer3,Condicion3, Caida3
                        
                        coordSlayer3 = CoordSlayer3
                        
                        if Caida3 == True:
                            Condicion3 = False
                            WindGame.after(5, lambda:MovDoomDown3(CordY)) 
                        elif CordY <= 0 or Caida3 == False:
                            Condicion3 = True
                        else:
                            C_Juego.coords(Slayer3, coordSlayer3[0], coordSlayer3[1]+2)
                            WindGame.after(5, lambda:MovDoomDown3(CordY-2))


                    def ActivarEfecto3():
                        global CoordSlayer1, CoordSlayer2, CoordSlayer4, Escudo1, Escudo2, Escudo3, Escudo4
                        
                        if player3.poder == "Force":
                            player1.poder=""
                            if Players == 3:
                                y = GeneraRandom(2)
                                if y == 1:
                                    if not Escudo1:
                                        C_Juego.coords(Slayer1,CoordSlayer1[0]+100, CoordSlayer1[1])
                                    else:
                                        print("El jugador 1 tiene escudo activo")
                                else:
                                    if not Escudo2:
                                        C_Juego.coords(Slayer2,CoordSlayer2[0]+100, CoordSlayer2[1])
                                    else:
                                        print("El jugador 2 tiene escudo activo")
                            elif Players == 4:
                                y = GeneraRandom(3)
                                if y == 1:
                                    if not Escudo1:
                                        C_Juego.coords(Slayer1,CoordSlayer1[0]+100, CoordSlayer1[1])
                                    else:
                                        print("El jugador 1 tiene escudo activo")
                                elif y == 2:
                                    if not Escudo2:
                                        C_Juego.coords(Slayer2,CoordSlayer2[0]+100, CoordSlayer2[1])
                                    else:
                                        print("El jugador 2 tiene escudo activo")
                                else:
                                    if not Escudo4:
                                        C_Juego.coords(Slayer4,CoordSlayer4[0]+100, CoordSlayer4[1])
                                    else:
                                        print("El jugador 4 tiene escudo activo")
                                    
                        elif player3.poder == "Shield":
                            player3.poder = ""
                            ActivaEscudo(3)
                        elif player3.poder == "Jump":
                            player3.poder = ""
                            CoordX = (random.randint(360,1000))
                            C_Juego.coords(Slayer3,CoordX,50)
                        else:
                            print("3, No tienes ningún efecto activo")
                    #Movimiento del Jugador 3
                        
                    #Movimiento del Jugador 4
                    def MovDoomUp4(CordY): #Realiza el salto del personaje

                        global CoordSlayer4, Condicion4
                        
                        coordSlayer4 = CoordSlayer4
                        
                        if CordY >= 250: #Limite del salto
                            MovDoomDown4(CordY) #Llamada a la funcion de caída del personaje
                        else:
                            C_Juego.coords(Slayer4, coordSlayer4[0], coordSlayer4[1]-4)
                            WindGame.after(7, lambda:MovDoomUp4(CordY+2))

                    def MovDoomDown4(CordY): #Caída del personaje
                        global CoordSlayer4,Condicion4, Caida4
                        
                        coordSlayer4 = CoordSlayer4

                        if Caida4 == True:
                            Condicion4 = False
                            WindGame.after(5, lambda:MovDoomDown4(CordY))
                        elif CordY <= 0 or Caida4 == False:
                            Condicion4 = True
                        else:
                            C_Juego.coords(Slayer4, coordSlayer4[0], coordSlayer4[1]+2)
                            WindGame.after(5, lambda:MovDoomDown4(CordY-2))


                    def ActivarEfecto4():
                        global CoordSlayer1, CoordSlayer2, CoordSlayer3, Escudo1, Escudo2, Escudo3, Escudo4
                        
                        if player4.poder == "Force":
                            #player4.poder=""
                            y = GeneraRandom(3)
                            if y == 1:
                                if not Escudo1:
                                    C_Juego.coords(Slayer1,CoordSlayer1[0]+100, CoordSlayer1[1])
                                else:
                                    print("El jugador 1 tiene escudo activo")
                            elif y == 2:
                                if not Escudo2:
                                    C_Juego.coords(Slayer2,CoordSlayer2[0]+100, CoordSlayer2[1])
                                else:
                                    print("El jugador 2 tiene escudo activo")
                            else:
                                if not Escudo3:
                                    C_Juego.coords(Slayer3,CoordSlayer3[0]+100, CoordSlayer3[1])
                                else:
                                    print("El jugador 3 tiene escudo activo")
                                    
                        elif player4.poder == "Shield":
                            #player4.poder = ""
                            ActivaEscudo(4)
                        elif player4.poder == "Jump":
                            #player4.poder = ""
                            CoordX = (random.randint(360,1000))
                            C_Juego.coords(Slayer4,CoordX,50)
                        else:
                            print("4, No tienes ningún efecto activo")

                    #Movimiento del Jugador 4


        #***************Acciones del personaje*********************
                        
                    global CoordSlayer1, Condicion1, CoordSlayer2, Condicion2, CoordSlayer3, Condicion3, CoordSlayer4, Condicion4



                    def mov1():
                        global CoordSlayer1, Condicion1
                        
                        
                        if (event.char).upper() == player1.izquierda: #Al ser presionada la tecla el personaje se mueve a la izquierda
                            if CoordSlayer1[0] >= 5: #Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego
                                
                                C_Juego.coords(Slayer1, CoordSlayer1[0]-12, CoordSlayer1[1])#Movimiento del personaje a la izquierda
                                
                                
                                
                        elif(event.char).upper() == player1.derecha:#Al ser presionada la tecla el personaje se mueve a la derecha
                            if CoordSlayer1[0] <= 1125:#Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego

                                C_Juego.coords(Slayer1, CoordSlayer1[0]+12, CoordSlayer1[1])#Movimiento del personaje a la derecha
                                
                                
                        elif(event.char).upper() == player1.salto: #Al ser presionada la tecla el personaje salta
                            if Condicion1: #No puede saltar hasta que llegue a la coordenada y = 656
                                Condicion1 = False
                                MovDoomUp(0)#Llamada al salto
                            
                        elif (event.char).upper() == player1.efecto: #Tecla de disparo
                                    Thread(target=ActivarEfecto()).start() #Llamada al disparo

                    def mov2():
                        global CoordSlayer2, Condicion2
                        
                        if (event.char).upper() == player2.izquierda: #Al ser presionada la tecla el personaje se mueve a la izquierda
                            if CoordSlayer2[0] >= 5: #Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego
                                
                                C_Juego.coords(Slayer2, CoordSlayer2[0]-12, CoordSlayer2[1])#Movimiento del personaje a la izquierda
                                
                                
                                
                        elif(event.char).upper() == player2.derecha:#Al ser presionada la tecla el personaje se mueve a la derecha
                            if CoordSlayer2[0] <= 1125:#Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego

                                C_Juego.coords(Slayer2, CoordSlayer2[0]+12, CoordSlayer2[1])#Movimiento del personaje a la derecha
                                
                                
                        elif(event.char).upper() == player2.salto: #Al ser presionada la tecla el personaje salta
                            if Condicion2: #No puede saltar hasta que llegue a la coordenada y = 656
                                Condicion2 = False
                                MovDoomUp2(0)#Llamada al salto
                            
                        elif (event.char).upper() == player2.efecto: #Tecla de disparo
                                    Thread(target=ActivarEfecto2()).start() #Llamada al disparo

                    def mov3():
                        global CoordSlayer3, Condicion3
                        
                        
                        if (event.char).upper() == player3.izquierda: #Al ser presionada la tecla el personaje se mueve a la izquierda
                            if CoordSlayer3[0] >= 5: #Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego
                                
                                C_Juego.coords(Slayer3, CoordSlayer3[0]-12, CoordSlayer3[1])#Movimiento del personaje a la izquierda
                                
                                
                                
                        elif(event.char).upper() == player3.derecha:#Al ser presionada la tecla el personaje se mueve a la derecha
                            if CoordSlayer3[0] <= 1125:#Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego

                                C_Juego.coords(Slayer3, CoordSlayer3[0]+12, CoordSlayer3[1])#Movimiento del personaje a la derecha
                                
                                
                        elif(event.char).upper() == player3.salto: #Al ser presionada la tecla el personaje salta
                            if Condicion3: #No puede saltar hasta que llegue a la coordenada y = 656
                                Condicion3 = False
                                MovDoomUp3(0)#Llamada al salto
                            
                        elif (event.char).upper() == player3.efecto: #Tecla de disparo
                                    Thread(target=ActivarEfecto3()).start() #Llamada al disparo
                                    
                    def mov4():
                        global CoordSlayer4, Condicion4

                        
                        
                        if (event.char).upper() == player4.izquierda: #Al ser presionada la tecla el personaje se mueve a la izquierda
                            if CoordSlayer4[0] >= 5: #Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego
                                
                                C_Juego.coords(Slayer4, CoordSlayer4[0]-12, CoordSlayer4[1])#Movimiento del personaje a la izquierda
                                
                                
                                
                        elif(event.char).upper() == player4.derecha:#Al ser presionada la tecla el personaje se mueve a la derecha
                            if CoordSlayer4[0] <= 1125:#Limite del movimiento con respecto al tamaño Canvas, evita que el personaje se salga de la pantalla de juego

                                C_Juego.coords(Slayer4, CoordSlayer4[0]+12, CoordSlayer4[1])#Movimiento del personaje a la derecha
                                
                                
                        elif(event.char).upper() == player4.salto: #Al ser presionada la tecla el personaje salta
                            if Condicion4: #No puede saltar hasta que llegue a la coordenada y = 656
                                Condicion4 = False
                                MovDoomUp4(0)#Llamada al salto
                            
                        elif (event.char).upper() == player4.efecto: #Tecla de disparo
                                    Thread(target=ActivarEfecto4()).start() #Llamada al disparo

                        
                    Thread(target=mov1()).start()
                    Thread(target=mov2()).start()

                    if Players >=3:
                        Thread(target=mov3()).start()
                        if Players ==4:
                            Thread(target=mov4()).start()
                        
                #End MovDoom


        def Timer(): #Es el temporizador del juego
            global Tiempo
            
            if Tiempo == 0:#Si el tiempo a 0 el juego termina
                return
            else:
                Tiempo -=10
                WindGame.after(1000,lambda:Timer())
                
        

        def Objetivo():
            global Tiempo, Build
            if Tiempo == 300 or Tiempo == 240  or Tiempo == 180  or Tiempo == 120  or Tiempo == 60:
                GeneraObjetivo()
                WindGame.after(1000, lambda:Objetivo())
            else:
                WindGame.after(1, lambda:Objetivo())

        def GeneraObjetivo():
            global Build
            X = (random.randint(1,4))
            print(X)
            if X == 1:
                Build = "BST"
            elif X == 2:
                Build = "AVL"
            elif X == 3:
                Build = "B TREE"
            else:
                Build = "SPLAY"

        
        def TimerObj(): #La funcion actualiza el tiempo, vida y puntuacion del jugador
            global Tiempo, Build

            lb_ObjetivoTime.config(text= ("Tiempo:" , Tiempo, "Build:", Build), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10), height = 3, width=75)

            if Tiempo == 0:#Si el tiempo a 0 el juego termina
                General.GameOver("Prueba", 100, "Victoria")
            else:
                WindGame.after(1,lambda:TimerObj())
                


        def gravity1():
            global CoordSlayer1, Caida1, CantPlayers
            
            if CoordSlayer1[1] >= 700:
                C_Juego.delete(Slayer1)
                print("Adios 1")
                CantPlayers -= 1
            else:
                if (CoordSlayer1[0]+30 >= 555  and CoordSlayer1[0]+30 <= 1050 and CoordSlayer1[1]+130 >=255 and CoordSlayer1[1]+130 <=265) or (CoordSlayer1[0]+30 >= 260  and CoordSlayer1[0]+30 <= 480 and CoordSlayer1[1]+130 >=360 and CoordSlayer1[1]+130 <=370) or (CoordSlayer1[0]+30 >= 1130  and CoordSlayer1[0]+30 <= 1200 and CoordSlayer1[1]+130 >=360 and CoordSlayer1[1]+130 <=370) or (CoordSlayer1[0]+30 >= 910  and CoordSlayer1[0]+30 <= 1200 and CoordSlayer1[1]+130 >=460 and CoordSlayer1[1]+130 <=470) or (CoordSlayer1[0]+30 >= 330  and CoordSlayer1[0]+30 <= 700 and CoordSlayer1[1]+130 >=460 and CoordSlayer1[1]+130 <=470):
                    Caida1 = False
                    WindGame.after(10,lambda:gravity1())
                else:
                    Caida1 = True
                    C_Juego.coords(Slayer1, CoordSlayer1[0], CoordSlayer1[1]+3)
                    WindGame.after(10,lambda:gravity1())
                
        def gravity2():
            global CoordSlayer2, Caida2, CantPlayers
            
            if CoordSlayer2[1] >= 700:
                C_Juego.delete(Slayer2)
                print("Adios 2")
                CantPlayers -= 1
            else:
                if (CoordSlayer2[0]+30 >= 555  and CoordSlayer2[0]+30 <= 1050 and CoordSlayer2[1]+130 >=255 and CoordSlayer2[1]+130 <=265) or (CoordSlayer2[0]+30 >= 260  and CoordSlayer2[0]+30 <= 480 and CoordSlayer2[1]+130 >=360 and CoordSlayer2[1]+130 <=370) or (CoordSlayer2[0]+30 >= 1130  and CoordSlayer2[0]+30 <= 1200 and CoordSlayer2[1]+130 >=360 and CoordSlayer2[1]+130 <=370) or (CoordSlayer2[0]+30 >= 910  and CoordSlayer2[0]+30 <= 1200 and CoordSlayer2[1]+130 >=460 and CoordSlayer2[1]+130 <=470) or (CoordSlayer2[0]+30 >= 330  and CoordSlayer2[0]+30 <= 700 and CoordSlayer2[1]+130 >=460 and CoordSlayer2[1]+130 <=470):
                    Caida2 = False
                    WindGame.after(10,lambda:gravity2())
                else:
                    Caida2 = True
                    C_Juego.coords(Slayer2, CoordSlayer2[0], CoordSlayer2[1]+3)
                    WindGame.after(10,lambda:gravity2())
                
        def gravity3():
            global CoordSlayer3, Caida3, CantPlayers
            
            if CoordSlayer3[1] >= 700:
                C_Juego.delete(Slayer3)
                print("Adios 3")
                CantPlayers -= 1
            else:
                if (CoordSlayer3[0]+30 >= 555  and CoordSlayer3[0]+30 <= 1050 and CoordSlayer3[1]+130 >=255 and CoordSlayer3[1]+130 <=265) or (CoordSlayer3[0]+30 >= 260  and CoordSlayer3[0]+30 <= 480 and CoordSlayer3[1]+130 >=360 and CoordSlayer3[1]+130 <=370) or (CoordSlayer3[0]+30 >= 1130  and CoordSlayer3[0]+30 <= 1200 and CoordSlayer3[1]+130 >=360 and CoordSlayer3[1]+130 <=370) or (CoordSlayer3[0]+30 >= 910  and CoordSlayer3[0]+30 <= 1200 and CoordSlayer3[1]+130 >=460 and CoordSlayer3[1]+130 <=470) or (CoordSlayer3[0]+30 >= 330  and CoordSlayer3[0]+30 <= 700 and CoordSlayer3[1]+130 >=460 and CoordSlayer3[1]+130 <=470):
                    Caida3 = False
                    WindGame.after(10,lambda:gravity3())
                else:
                    Caida3 = True
                    C_Juego.coords(Slayer3, CoordSlayer3[0], CoordSlayer3[1]+3)
                    WindGame.after(10,lambda:gravity3())
                
        def gravity4():
            global CoordSlayer4, Caida4, CantPlayers
            
            if CoordSlayer4[1] >= 700:
                C_Juego.delete(Slayer4)
                print("Adios 4")
                CantPlayers -= 1
            else:
                if (CoordSlayer4[0]+30 >= 555  and CoordSlayer4[0]+30 <= 1050 and CoordSlayer4[1]+130 >=255 and CoordSlayer4[1]+130 <=265) or (CoordSlayer4[0]+30 >= 260  and CoordSlayer4[0]+30 <= 480 and CoordSlayer4[1]+130 >=360 and CoordSlayer4[1]+130 <=370) or (CoordSlayer4[0]+30 >= 1130  and CoordSlayer4[0]+30 <= 1200 and CoordSlayer4[1]+130 >=360 and CoordSlayer4[1]+130 <=370) or (CoordSlayer4[0]+30 >= 910  and CoordSlayer4[0]+30 <= 1200 and CoordSlayer4[1]+130 >=460 and CoordSlayer4[1]+130 <=470) or (CoordSlayer4[0]+30 >= 330  and CoordSlayer4[0]+30 <= 700 and CoordSlayer4[1]+130 >=460 and CoordSlayer4[1]+130 <=470):
                    Caida4 = False
                    WindGame.after(10,lambda:gravity4())
                else:
                    Caida4 = True
                    C_Juego.coords(Slayer4, CoordSlayer4[0], CoordSlayer4[1]+3)
                    WindGame.after(10,lambda:gravity4())


        def posPlayer1():
            global CoordSlayer1

            CoordSlayer1 = C_Juego.coords(Slayer1)

            if CoordSlayer1[1] >= 700 or Tiempo == 0:
                return
            else:
                WindGame.after(1, lambda: posPlayer1())
                
        def posPlayer2():
            global CoordSlayer2

            CoordSlayer2 = C_Juego.coords(Slayer2)

            if CoordSlayer2[1] >= 700 or Tiempo == 0:
                return
            else:
                WindGame.after(1, lambda: posPlayer2())

                
        def posPlayer3():
            global CoordSlayer3

            CoordSlayer3 = C_Juego.coords(Slayer3)

            if CoordSlayer3[1] >= 700 or Tiempo == 0:
                return
            else:
                WindGame.after(1, lambda: posPlayer3())

        def posPlayer4():
            global CoordSlayer4

            CoordSlayer4 = C_Juego.coords(Slayer4)

            if CoordSlayer4[1] >= 700 or Tiempo == 0:
                return
            else:
                WindGame.after(1, lambda: posPlayer4())


        def ActivaEscudo(Jugador):
            global Escudo1,Escudo2,Escudo3,Escudo4

            if Jugador == 1:
                Escudo1 = True
                print("1" , Escudo1)
            elif Jugador == 2:
                Escudo2 = True
                print("2" , Escudo2)
            elif Jugador == 3:
                Escudo3 = True
                print("3" , Escudo3)
            else:
                Escudo4 = True
                print("4" , Escudo4)
            WindGame.after(10000, lambda:DesactivaEscudo(Jugador))
                
        def DesactivaEscudo(Jugador):
            global Escudo1,Escudo2,Escudo3,Escudo4
            if Jugador == 1:
                Escudo1 = False
                print("1" , Escudo1)
            elif Jugador == 2:
                Escudo2 = False
                print("2" , Escudo2)
            elif Jugador == 3:
                Escudo3 = False
                print("3" , Escudo3)
            else:
                Escudo4 = False
                print("4" , Escudo4)



        #Creación de Personajes
        C_Juego.Slayer1 = General.cargarImg2('Slayer\Slayer1.png') #Creación del personaje que el jugador opera
        Slayer1 = C_Juego.create_image(400,666,anchor = NW, image =C_Juego.Slayer1)
        C_Juego.coords(Slayer1, 600, 120)

        C_Juego.Slayer2 = General.cargarImg2('Slayer\Slayer2.png') #Creación del personaje que el jugador opera
        Slayer2 = C_Juego.create_image(500,666,anchor = NW, image =C_Juego.Slayer2)
        C_Juego.coords(Slayer2, 250, 225)
        
        if Players >=3: #Evaluación para la creación del tercer jugador
            
            C_Juego.Slayer3 = General.cargarImg2('Slayer\Slayer3.png') #Creación del personaje que el jugador opera
            Slayer3 = C_Juego.create_image(100,666,anchor = NW, image =C_Juego.Slayer3)
            C_Juego.coords(Slayer3, 600, 325)
            Thread(target=posPlayer3()).start()
            Thread(target=gravity3()).start()
            
            if Players == 4:#Evaluación para la creación del cuarto jugador
                
                C_Juego.Slayer4 = General.cargarImg2('Slayer\Slayer4.png') #Creación del personaje que el jugador opera
                Slayer4 = C_Juego.create_image(700,666,anchor = NW, image =C_Juego.Slayer4)
                C_Juego.coords(Slayer4, 1000, 325)
                Thread(target=posPlayer4()).start()
                Thread(target=gravity4()).start()

        C_Juego.Pixel = General.cargarImg2('pixel.png') #Creación del personaje que el jugador opera
        Pixel = C_Juego.create_image(330,460,anchor = NW, image =C_Juego.Pixel)

        #Creación de Personajes

                
        #Llamada de funciones

        C_Juego.bind("<KeyPress>", MovDoom) #Llamada a la funcion que contiene las acciones del personaje
        C_Juego.focus_set() #Hace que el Canvas se enfoque en la accion a realizar por parte de la tecla

        GeneraObjetivo()

        Thread(target=Timer()).start()      
        Thread(target=Objetivo()).start()        
        Thread(target=TimerObj()).start()
        Thread(target=posPlayer1()).start()
        Thread(target=posPlayer2()).start()
        Thread(target=gravity1()).start()
        
        Thread(target=gravity2()).start()
        
        #Llamada de funciones



        
        

















    
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
                    WindGame.after(7, lambda:MovDoomUp())


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


















