
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

import ArbolBST
import ArbolBST2
import ArbolBST3
import ArbolBST4

import ArbolAVL
import ArbolAVL2
import ArbolAVL3
import ArbolAVL4

import ArbolB
import ArbolB2
import ArbolB3
import ArbolB4

import ArbolSplay
import ArbolSplay2
import ArbolSplay3
import ArbolSplay4
"""
from player2Controles import *
from player3Controles import *
"""

class General: #La clase contiene todas las interfaces presentes en el menu, con sus respectivos botones.

    global CoordBullet, CoordSlayer, CoordEnemy,coordMisil, coordAplasta, Misil, Aplasta, Vivo, AplastaBullet, SCORE, Tiempo,  PlayOrNot, Hp, Salto, Derecha, Izquierda, Disparo   #Variables globales correspondientes a las coordenadas de los objetos del juego
    global player1, player2, player3, player4, player1Avl, player2Avl, player3Avl, player4Avl, player1BST, player2BST, player3BST, player4BST, player1B, player2B, player3B, player4B, player1Splay, player2Splay, player3Splay, player4Splay


    player1 = player1Controles.Controles()
    player2 = player2Controles.Controles()
    player3 = player3Controles.Controles()
    player4 = player4Controles.Controles()

    player1Avl = ArbolAVL.AVL()
    player2Avl = ArbolAVL2.AVL()
    player3Avl = ArbolAVL3.AVL()
    player4Avl = ArbolAVL4.AVL()

    player1BST = ArbolBST.Node(0)
    player2BST = ArbolBST2.Node(0)
    player3BST = ArbolBST3.Node(0)
    player4BST = ArbolBST4.Node(0)
    
    player1B = ArbolB.BTree(3)
    player2B = ArbolB2.BTree(3)
    player3B = ArbolB3.BTree(3)
    player4B = ArbolB4.BTree(3)

    player1Splay = ArbolSplay.SplayTree()
    player2Splay = ArbolSplay2.SplayTree()
    player3Splay = ArbolSplay3.SplayTree()
    player4Splay = ArbolSplay4.SplayTree()



    #player1Splay.insert(1)
    #player1Splay.pretty_print()
    #player1Splay.delete()

    #player1B.insert(15)
    #player1B.print_order()
    #player1B.delete()

    #player1BST.insert(15)
    #player1BST.PrintTree()
    #player1BST.delete()
    

    #player1Avl.insert(15)
    #player1Avl.preShow(player1Avl.root)
    #player1Avl.delete()

    Hp = 3
    
    
    def Principal(): #Funcion generadora de la interfaz
        """
*************************************************************************
                    Instituto Tecnológico de Costa Rica
                        Ingeniería en Computadores
        Función: Principal

        Descripcion de la Funcion: 
        La funcion se encarga de la creacion de toda la interfaz gráfica,
        ajusta su tamaño, evita que su tamaño sea editable y le añade un
        ícono a esta. Luego de establecer e creacion de toda la interfaz gráfica,
        ajusta su tamaño, evita que su tamaño sea editable y le añade un
        ícono a esta. Luego de establecer estos parámetros llama a la
        funcion


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

        
        #General.SmashInteface(4,"1","2","3","4")
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
                    General.SmashInteface(Jugadores, Jugador1, Jugador2, "", "")
            elif Jugadores == 3:
                if not Jugador1 or not Jugador2 or not Jugador3:
                    MuestraErrores(1)
                elif (len(Jugador1) > 11 or len(Jugador2) > 11 or len(Jugador3) > 11):
                    MuestraErrores(2)
                else:
                    EscondeErrores()
                    print("Funca 3")
                    General.SmashInteface(Jugadores, Jugador1, Jugador2,Jugador3, "")
            elif Jugadores == 4:
                if not Jugador1 or not Jugador2 or not Jugador3 or not Jugador4:
                    MuestraErrores(1)
                elif (len(Jugador1) > 11 or len(Jugador2) > 11 or len(Jugador3) > 11 or len(Jugador4) > 11):
                    MuestraErrores(2)
                else:
                    EscondeErrores()
                    print("Funca 4")
                    General.SmashInteface(Jugadores, Jugador1, Jugador2, Jugador3, Jugador4)
                    

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

        Descripcion de la Funcion: 
        La funcion crea un canvas que contiene al menu principal del juego
        y dentro de ese mismo canvas añade seis botones que realizan llamadas
        a seis funciones diferentes cuando son presionados, estas funciones
        tienen un botón que les permite regresar al menu principal. 

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
        
        C_GameOver = Canvas(WindGame, width = 1500 , height = 800, bg = 'green')
        C_GameOver.place(x=0, y=0)

        
        C_GameOver.Over = General.cargarImg2('InterfazMenu.png')#Background
        
        Img = C_GameOver.create_image(0,0, anchor = NW , image = C_GameOver.Over)

        def setPuntuacion():
            WriteScore = open("notes\D_Montoya_Rivera_Scores.txt", 'a')
            WriteScore.write("\n" + Jugador + "\n" + str(Score))
            return
        setPuntuacion()

        if Condicion == "Victoria":
        
            lb_Fin = Label(C_GameOver, text= ("El tiempo se ha acabado"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_Fin.place(x= 250, y = 10)

            lb_Name = Label(C_GameOver, text= ("Winner: " + Jugador), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13))
            lb_Name.place(x= 250, y = 50)
            
            lb_SCORE = Label(C_GameOver, text= ("Puntuacion = " + str(Score) + " pts"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_SCORE.place(x=250, y = 100)
            
        else:
            lb_Fin = Label(C_GameOver, text= ("Los jugadores se han caído del mapa"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_Fin.place(x=250,y=10)

            lb_Name = Label(C_GameOver, text= ("Winner: " + Jugador), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 13))
            lb_Name.place(x= 250, y = 50)
            
            lb_SCORE = Label(C_GameOver, text= ("Puntuacion = " + str(Score) + " pts"), bg ='Black', fg = 'Red', font =("Goudy Stout", 13))
            lb_SCORE.place(x=250, y = 100)




            
        btn_Return = Button(C_GameOver, text = 'Return', bg = 'black', fg = 'Yellow', height = 1, width = 13,command = lambda:General.Menu(), font =("Goudy Stout", 13)) # Regresa al menu Principal
        btn_Return.place(x = 1200, y = 700)



    def SmashInteface(Players, Name1, Name2, Name3, Name4):

        global CoordSlayer1, CoordSlayer2, CoordSlayer3, CoordSlayer4, Condicion1, Condicion2, Condicion3, Condicion4, Tiempo, Build, Slayer1, Slayer2, Slayer3, Slayer4, Caida1, Caida2, Caida3, Caida4, Escudo1, Escudo2, Escudo3, Escudo4, CantPlayers
        global CoordPower, StatusPlayer1, StatusPlayer2, StatusPlayer3, StatusPlayer4, Score1, Score2, Score3, Score4, Elementos1, Elementos2, Elementos3, Elementos4, Elementos

        CantPlayers = Players

        CoordSlayer1 = [0,0]
        CoordSlayer2 = [100,100]
        CoordSlayer3 = [200,200]
        CoordSlayer4 = [300,300]

        CoordPower = [1000,1000]
        
        Condicion1=True
        Condicion2=True
        Condicion3=True
        Condicion4=True

        Caida1=True
        Caida2=True
        Caida3=True
        Caida4=True

        StatusPlayer1 = True
        StatusPlayer2 = True
        StatusPlayer3 = False
        StatusPlayer4 = False

        if Players >= 3:
            StatusPlayer3 = True
            if Players == 4:
                StatusPlayer4 = True

        Escudo1=False
        Escudo2=False
        Escudo3=False
        Escudo4=False

        Score1=0
        Score2=0
        Score3=0
        Score4=0
        
        Tiempo = 300
        Build  = ""
        X = 0

        Elementos = 0
        Elementos1 = 0
        Elementos2 = 0
        Elementos3 = 0
        Elementos4 = 0


        player1B.insert(0)
        player1Avl.insert(0)
        player1BST.insert(0)
        player1Splay.insert(0)
        
        player2B.insert(0)
        player2Avl.insert(0)
        player2BST.insert(0)
        player2Splay.insert(0)
        
        player3B.insert(0)
        player3Avl.insert(0)
        player3BST.insert(0)
        player3Splay.insert(0)
        
        player4B.insert(0)
        player4Avl.insert(0)
        player4BST.insert(0)
        player4Splay.insert(0)

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
        lb_P1 = Label(C_Objetivos, text= ("Player 1 Tree  PTS:", Score1), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))
        lb_P1.place(x=0 , y = 0)

        lb_Tree1 = Label(C_Objetivos, text= ("."), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_Tree1.place(x=0 , y = 25)
        
        lb_P2 = Label(C_Objetivos, text= ("Player 2 Tree  PTS:", Score2), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))
        lb_P2.place(x=0 , y = 200)
        
        lb_Tree2 = Label(C_Objetivos, text= ("."), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_Tree2.place(x=0 , y = 225)
        
        lb_P3 = Label(C_Objetivos, text= ("Player 3 Tree  PTS:", Score3), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))
        lb_P3.place(x=0 , y = 400)
        
        lb_Tree3 = Label(C_Objetivos, text= ("."), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_Tree3.place(x=0 , y = 425)
        
        lb_P4 = Label(C_Objetivos, text= ("Player 4 Tree  PTS:", Score4), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))
        lb_P4.place(x=0 , y = 600)
        
        lb_Tree4 = Label(C_Objetivos, text= ("."), bg ='White', fg = 'Green', font =("Goudy Stout", 10))
        lb_Tree4.place(x=0 , y = 625)
        #Label para los árboles


        #Label del Objetivo y Tiempo del juego

        lb_ObjetivoTime = Label(C_Juego, text= ("Tiempo:" , Tiempo, "Build:", Build), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10), height = 3, width=75)
        lb_ObjetivoTime.place(x=0 , y = 0) 


        def GeneraRandom(Num): #Funcion encargada de generar un número aleatorio entre 1 y un límite que se le pasa como parámetro.
            X = (random.randint(1,Num))
            return X

        def MovDoom(event): #La función se encarga de las mecánicas del movimiento y acciones de los jugadores dentro del escenario del juego
            
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


                    def ActivarEfecto(): #Activación del poder
                        global CoordSlayer2, CoordSlayer3, CoordSlayer4, Escudo1, Escudo2, Escudo3, Escudo4
                        if player1.poder == "Force": #Efecto del poder Force
                            player1.poder=""
                            if Players == 2:
                                if not Escudo2:  #Si el jugador enemigo al cual se le aplica el efecto tiene un escudo entonces no realizará ninguna acción de empuje
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

                        elif player1.poder == "Shield": #Activa el escudo del jugador, la acción dura 10 segundos
                            player1.poder = ""
                            ActivaEscudo(1)
                        elif player1.poder == "Jump": #Teletransporta al juegador a una posición segura del mapa
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
                            player3.poder=""
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
                            player4.poder=""
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
                            player4.poder = ""
                            ActivaEscudo(4)
                        elif player4.poder == "Jump":
                            player4.poder = ""
                            CoordX = (random.randint(360,1000))
                            C_Juego.coords(Slayer4,CoordX,50)
                        else:
                            print("4, No tienes ningún efecto activo")

                    #Movimiento del Jugador 4


        #***************Acciones del personaje*********************
                        
                    global CoordSlayer1, Condicion1, CoordSlayer2, Condicion2, CoordSlayer3, Condicion3, CoordSlayer4, Condicion4



                    def mov1():
                        global CoordSlayer1, Condicion1, StatusPlayer1

                        if StatusPlayer1: #Evalúa si el personaje está vivo
                            
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
                        global CoordSlayer2, Condicion2, StatusPlayer2

                        if StatusPlayer2:
                            
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
                        global CoordSlayer3, Condicion3, StatusPlayer3
                        
                        if StatusPlayer3:
                            
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
                        global CoordSlayer4, Condicion4, StatusPlayer4

                        if StatusPlayer4:
                            
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
            global Tiempo, CantPlayers, Score1, Score2, Score3, Score4
            
            if Tiempo <= 0 or CantPlayers <= 1:#Si el tiempo llega a 0 o la cantidad de jugadortes es 1 el juego termina
                Tiempo = 0
                return
            else:

                
                Tiempo -=1
                
                WindGame.after(1000,lambda:Timer())
                
        

        def Objetivo(): #La funcion se encarga de cambiar el objetivo del juego cada 60 segundos
            
            global Tiempo, Build
            
            if Tiempo == 0 or CantPlayers <= 1:
                return
            else:
                if Tiempo == 300 or Tiempo == 240  or Tiempo == 180  or Tiempo == 120  or Tiempo == 60:
                    GeneraObjetivo()
                    WindGame.after(1000, lambda:Objetivo())
                else:
                    WindGame.after(1, lambda:Objetivo())

        def GeneraObjetivo(): #Función encargada de generar el objetivo del juego
            global Build, Elementos1,Elementos2,Elementos3,Elementos4, Elementos
            
            player1B.delete()
            player1Avl.delete()
            player1BST.delete()
            player1Splay.deleteTree()
            
            player2B.delete()
            player2Avl.delete()
            player2BST.delete()
            player2Splay.deleteTree()
            
            player3B.delete()
            player3Avl.delete()
            player3BST.delete()
            player3Splay.deleteTree()
            
            player4B.delete()
            player4Avl.delete()
            player4BST.delete()
            player4Splay.deleteTree()

            Elementos1 = 0
            Elementos2 = 0
            Elementos3 = 0
            Elementos4 = 0
            
            Elementos = (random.randint(2,5))
            
            X = (random.randint(1,4))
            if X == 1:
                Build = "BST" 
            elif X == 2:
                Build = "AVL"
            elif X == 3:
                Build = "B"
            else:
                Build = "SPLAY"

        
        def TimerObj(): #La funcion actualiza el tiempo, vida y puntuacion del jugador
            global Tiempo, Build, CantPlayers, CoordSlayer1,CoordSlayer2,CoordSlayer3,CoordSlayer4,Elementos, StatusPlayer1, StatusPlayer2,StatusPlayer3,StatusPlayer4, Score1, Score2, Score3,Score4

            lb_ObjetivoTime.config(text= ("Tiempo: " , Tiempo, "Build: ", Build, " of: ", Elementos, " elementos"), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10), height = 3, width=75)

            if Tiempo <= 0 or CantPlayers <= 1:#Si el tiempo a 0 el juego termina
                
                CoordSlayer1 = [99999,99999]
                CoordSlayer2 = [99999,99999]
                CoordSlayer3 = [99999,99999]
                CoordSlayer4 = [99999,99999]
                
                player1.poder = ""
                player2.poder = ""
                player3.poder = ""
                player4.poder = ""

                if CantPlayers == 1:
                    Winner = ""
                    Puntuacion = 0
                    CantPlayers = 0
                    
                    if StatusPlayer1:
                        Winner = Name1
                        Puntuacion = Score1
                    elif StatusPlayer2:
                        Winner = Name2
                        Puntuacion = Score2
                    elif StatusPlayer3:
                        Winner = Name3
                        Puntuacion = Score3
                    elif StatusPlayer4:
                        Winner = Name4
                        Puntuacion = Score4
                    General.GameOver(Winner, Puntuacion, "Derrota")
                    
                elif Tiempo <=0:

                    Winner = ""
                    Puntuacion = 0
                    
                    CantPlayers = 0
                    #>< = 
                    Tiempo = 0
                    if (Score1 > Score2) and (Score1 > Score3) and (Score1 > Score4): #Evalúa si el ganador por puntuacion es el jugador 1
                        
                        Winner = Name1
                        Puntuacion = Score1
                        
                    elif (Score2 > Score1) and (Score2 > Score3) and (Score2 > Score4):#Evalúa si el ganador por puntuacion es el jugador 2
                        
                        Winner = Name2
                        Puntuacion = Score2
                        
                    elif (Score3 > Score1) and (Score3 > Score2) and (Score3 > Score4):#Evalúa si el ganador por puntuacion es el jugador 3

                        Winner = Name3
                        Puntuacion = Score3

                    elif (Score4 > Score1) and (Score4 > Score2) and (Score4 > Score3): #Evalúa si el ganador por puntuacion es el jugador 4

                        Winner = Name4
                        Puntuacion = Score4

                    elif (Score1 == Score2) and (Score1 > Score3) and (Score1 > Score4): #Evalúa si el ganador por puntuacion es el jugador 1 y 2

                        Winner = Name1 + " y " + Name2
                        Puntuacion = Score1

                    elif (Score1 == Score3) and (Score1 > Score2) and (Score1 > Score4):#Evalúa si el ganador por puntuacion es el jugador 1 y 3
                        
                        Winner = Name1 + " y " + Name3
                        Puntuacion = Score1

                    elif (Score1 == Score4) and (Score1 > Score2) and (Score1 > Score3): #Evalúa si el ganador por puntuacion es el jugador 1 y 4

                        Winner = Name1 + " y " + Name4
                        Puntuacion = Score1

                    elif (Score2 == Score3) and (Score2 > Score1) and (Score2 > Score4): #Evalúa si el ganador por puntuacion es el jugador 2 y 3

                        Winner = Name2 + " y " + Name3
                        Puntuacion = Score2
                        
                    elif (Score2 == Score4) and (Score2 > Score1) and (Score2 > Score3): #Evalúa si el ganador por puntuacion es el jugador 2 y 4

                        Winner = Name2 + " y " + Name4
                        Puntuacion = Score2

                    elif (Score4 == Score3) and (Score4 > Score1) and (Score4 > Score2): #Evalúa si el ganador por puntuacion es el jugador 4 y 3 

                        Winner = Name4 + " y " + Name3
                        Puntuacion = Score2

                    elif (Score1 == Score2) and (Score1 == Score3) and (Score1 > Score4): #Evalúa si el ganador por puntuacion es el jugador 1,2,3

                        Winner = Name1 + ", " + Name2 + " y " + Name3 
                        Puntuacion = Score1

                    elif (Score1 == Score3) and (Score1 == Score4) and (Score1 > Score2): #Evalúa si el ganador por puntuacion es el jugador 1,3,4

                        Winner = Name1 + ", " + Name3 + " y " + Name4 
                        Puntuacion = Score1

                        
                    elif (Score2 == Score3) and (Score2 == Score4) and (Score2 > Score1): #Evalúa si el ganador por puntuacion es el jugador 2,3,4

                        Winner = Name2 + ", " + Name3 + " y " + Name4 
                        Puntuacion = Score2

                    elif (Score2 == Score4) and (Score2 == Score1) and (Score2 > Score3): #Evalúa si el ganador por puntuacion es el jugador 1,2,4

                        Winner = Name1 + ", " + Name2 + " y " + Name4 
                        Puntuacion = Score2

                    else: #Todos empatan

                        Winner = Name1 + ", " + Name2 + ", " + Name3 + ", " + Name4
                        Puntuacion = Score1

                    General.GameOver(Winner, Puntuacion, "Victoria")
            else:
                WindGame.after(1,lambda:TimerObj())
                


        def gravity1(): #La funcion se encarga de evaluar si el jugador se encuentra en el suelo, sino este entonces estará cayendo
            global CoordSlayer1, Caida1, CantPlayers, StatusPlayer1
            
            if not StatusPlayer1 or CoordSlayer1[1] >= 700 or Tiempo == 0 or CantPlayers <= 1: #Si el juegador se cae del mapa entonces se elimina al personaje 
                CoordSlayer1 = [99999,99999]
                C_Juego.delete(Slayer1)
                StatusPlayer1 = False
                CantPlayers -= 1
                return
            else:
                if (CoordSlayer1[0]+30 >= 555  and CoordSlayer1[0]+30 <= 1050 and CoordSlayer1[1]+130 >=255 and CoordSlayer1[1]+130 <=265) or (CoordSlayer1[0]+30 >= 260  and CoordSlayer1[0]+30 <= 480 and CoordSlayer1[1]+130 >=360 and CoordSlayer1[1]+130 <=370) or (CoordSlayer1[0]+30 >= 1130  and CoordSlayer1[0]+30 <= 1200 and CoordSlayer1[1]+130 >=360 and CoordSlayer1[1]+130 <=370) or (CoordSlayer1[0]+30 >= 910  and CoordSlayer1[0]+30 <= 1200 and CoordSlayer1[1]+130 >=460 and CoordSlayer1[1]+130 <=470) or (CoordSlayer1[0]+30 >= 330  and CoordSlayer1[0]+30 <= 700 and CoordSlayer1[1]+130 >=460 and CoordSlayer1[1]+130 <=470):
                    Caida1 = False
                    WindGame.after(10,lambda:gravity1())
                else:
                    Caida1 = True
                    C_Juego.coords(Slayer1, CoordSlayer1[0], CoordSlayer1[1]+3)
                    WindGame.after(10,lambda:gravity1())
                
        def gravity2():#La funcion se encarga de evaluar si el jugador se encuentra en el suelo, sino este entonces estará cayendo
            global CoordSlayer2, Caida2, CantPlayers, StatusPlayer2
            
            if not StatusPlayer2 or CoordSlayer2[1] >= 700 or Tiempo == 0 or CantPlayers <= 1:
                CoordSlayer2 = [99999,99999]
                C_Juego.delete(Slayer2)
                StatusPlayer2 = False
                CantPlayers -= 1
                return
            else:
                if (CoordSlayer2[0]+30 >= 555  and CoordSlayer2[0]+30 <= 1050 and CoordSlayer2[1]+130 >=255 and CoordSlayer2[1]+130 <=265) or (CoordSlayer2[0]+30 >= 260  and CoordSlayer2[0]+30 <= 480 and CoordSlayer2[1]+130 >=360 and CoordSlayer2[1]+130 <=370) or (CoordSlayer2[0]+30 >= 1130  and CoordSlayer2[0]+30 <= 1200 and CoordSlayer2[1]+130 >=360 and CoordSlayer2[1]+130 <=370) or (CoordSlayer2[0]+30 >= 910  and CoordSlayer2[0]+30 <= 1200 and CoordSlayer2[1]+130 >=460 and CoordSlayer2[1]+130 <=470) or (CoordSlayer2[0]+30 >= 330  and CoordSlayer2[0]+30 <= 700 and CoordSlayer2[1]+130 >=460 and CoordSlayer2[1]+130 <=470):
                    Caida2 = False
                    WindGame.after(10,lambda:gravity2())
                else:
                    Caida2 = True
                    C_Juego.coords(Slayer2, CoordSlayer2[0], CoordSlayer2[1]+3)
                    WindGame.after(10,lambda:gravity2())
                
        def gravity3():#La funcion se encarga de evaluar si el jugador se encuentra en el suelo, sino este entonces estará cayendo
            global CoordSlayer3, Caida3, CantPlayers, StatusPlayer3
            
            if not StatusPlayer3 or CoordSlayer3[1] >= 700 or Tiempo == 0 or CantPlayers <= 1:
                CoordSlayer3 = [99999,99999]
                C_Juego.delete(Slayer3)
                StatusPlayer3 = False
                CantPlayers -= 1
                return
            else:
                if (CoordSlayer3[0]+30 >= 555  and CoordSlayer3[0]+30 <= 1050 and CoordSlayer3[1]+130 >=255 and CoordSlayer3[1]+130 <=265) or (CoordSlayer3[0]+30 >= 260  and CoordSlayer3[0]+30 <= 480 and CoordSlayer3[1]+130 >=360 and CoordSlayer3[1]+130 <=370) or (CoordSlayer3[0]+30 >= 1130  and CoordSlayer3[0]+30 <= 1200 and CoordSlayer3[1]+130 >=360 and CoordSlayer3[1]+130 <=370) or (CoordSlayer3[0]+30 >= 910  and CoordSlayer3[0]+30 <= 1200 and CoordSlayer3[1]+130 >=460 and CoordSlayer3[1]+130 <=470) or (CoordSlayer3[0]+30 >= 330  and CoordSlayer3[0]+30 <= 700 and CoordSlayer3[1]+130 >=460 and CoordSlayer3[1]+130 <=470):
                    Caida3 = False
                    WindGame.after(10,lambda:gravity3())
                else:
                    Caida3 = True
                    C_Juego.coords(Slayer3, CoordSlayer3[0], CoordSlayer3[1]+3)
                    WindGame.after(10,lambda:gravity3())
                
        def gravity4():#La funcion se encarga de evaluar si el jugador se encuentra en el suelo, sino este entonces estará cayendo
            global CoordSlayer4, Caida4, CantPlayers, StatusPlayer4
            
            if not StatusPlayer4 or CoordSlayer4[1] >= 700 or Tiempo == 0 or CantPlayers <= 1:
                CoordSlayer4 = [99999,99999]
                C_Juego.delete(Slayer4)
                StatusPlayer4 = False
                CantPlayers -= 1
                return
            else:
                if (CoordSlayer4[0]+30 >= 555  and CoordSlayer4[0]+30 <= 1050 and CoordSlayer4[1]+130 >=255 and CoordSlayer4[1]+130 <=265) or (CoordSlayer4[0]+30 >= 260  and CoordSlayer4[0]+30 <= 480 and CoordSlayer4[1]+130 >=360 and CoordSlayer4[1]+130 <=370) or (CoordSlayer4[0]+30 >= 1130  and CoordSlayer4[0]+30 <= 1200 and CoordSlayer4[1]+130 >=360 and CoordSlayer4[1]+130 <=370) or (CoordSlayer4[0]+30 >= 910  and CoordSlayer4[0]+30 <= 1200 and CoordSlayer4[1]+130 >=460 and CoordSlayer4[1]+130 <=470) or (CoordSlayer4[0]+30 >= 330  and CoordSlayer4[0]+30 <= 700 and CoordSlayer4[1]+130 >=460 and CoordSlayer4[1]+130 <=470):
                    Caida4 = False
                    WindGame.after(10,lambda:gravity4())
                else:
                    Caida4 = True
                    C_Juego.coords(Slayer4, CoordSlayer4[0], CoordSlayer4[1]+3)
                    WindGame.after(10,lambda:gravity4())


        def posPlayer1(): #Funcion encargada de actualizar la posición del Jugador 1 en el juego
            global CoordSlayer1, StatusPlayer1

            CoordSlayer1 = C_Juego.coords(Slayer1)

            if not StatusPlayer1 or  CoordSlayer1[1] >= 700 or Tiempo == 0 or CantPlayers <= 1:
                return
            else:
                WindGame.after(1, lambda: posPlayer1())
                
        def posPlayer2():#Funcion encargada de actualizar la posición del Jugador 2 en el juego
            global CoordSlayer2, StatusPlayer2

            CoordSlayer2 = C_Juego.coords(Slayer2)

            if not StatusPlayer2 or  Tiempo == 0 or CantPlayers <= 1:
                return
            else:
                WindGame.after(1, lambda: posPlayer2())

                
        def posPlayer3():#Funcion encargada de actualizar la posición del Jugador 3 en el juego
            global CoordSlayer3, StatusPlayer3

            CoordSlayer3 = C_Juego.coords(Slayer3)

            if not StatusPlayer3 or  CoordSlayer3[1] >= 700 or Tiempo == 0 or CantPlayers <= 1:
                return
            else:
                WindGame.after(1, lambda: posPlayer3())

        def posPlayer4():#Funcion encargada de actualizar la posición del Jugador 4 en el juego
            global CoordSlayer4, StatusPlayer4

            CoordSlayer4 = C_Juego.coords(Slayer4)

            if not StatusPlayer4 or CoordSlayer4[1] >= 700 or Tiempo == 0 or CantPlayers <= 1:
                return
            else:
                WindGame.after(1, lambda: posPlayer4())


        def ActivaEscudo(Jugador): #Funcion encargada de activar el escudo del jugador
            global Escudo1,Escudo2,Escudo3,Escudo4

            if Jugador == 1:
                Escudo1 = True
            elif Jugador == 2:
                Escudo2 = True
            elif Jugador == 3:
                Escudo3 = True
            else:
                Escudo4 = True
            WindGame.after(10000, lambda:DesactivaEscudo(Jugador))
                
        def DesactivaEscudo(Jugador): #Funcion encargada de desactivar el escudo del jugador
            global Escudo1,Escudo2,Escudo3,Escudo4
            if Jugador == 1:
                Escudo1 = False
            elif Jugador == 2:
                Escudo2 = False
            elif Jugador == 3:
                Escudo3 = False
            else:
                Escudo4 = False


        def PoderMov(Img, Poder): #Funcion encargada de crear la imagen 
            
            PowerImage = C_Juego.create_image((random.randint(0 , 800)),50 ,anchor = NW ,image = Img)

            Thread(target = RecursionMovPower(PowerImage,Poder)).start()
            
        def RecursionMovPower(Imagen,Poder): #Funcion recursiva encargada de la caída del Poder
            
            global Tiempo, CoordPower, CoordSlayer1, CoordSlayer2, CoordSlayer3, CoordSlayer4, CantPlayers, StatusPlayer1,StatusPlayer2,StatusPlayer3,StatusPlayer4
            
            CoordPower = C_Juego.coords(Imagen)

            PowerHitbox = [C_Juego.coords(Imagen)[0]+25, C_Juego.coords(Imagen)[1]+60] #Establece el hitbox del misil
            
            if Tiempo == 0 or CoordPower[1] >= 800 or CantPlayers <= 1:
                CoordPower=[10000,10000]
                C_Juego.delete(Imagen)
                return
            else:
                if  StatusPlayer1 and (PowerHitbox[0] >= CoordSlayer1[0]) and (PowerHitbox[0] <= CoordSlayer1[0]+80) and (PowerHitbox[1] >= CoordSlayer1[1]) and (PowerHitbox[1] <=CoordSlayer1[1]+124):#Colision del poder con el personaje 1
                    CoordPower=[10000,10000]
                    player1.poder = Poder
                    C_Juego.delete(Imagen)
                    return
                elif StatusPlayer2 and (PowerHitbox[0] >= CoordSlayer2[0]) and (PowerHitbox[0] <= CoordSlayer2[0]+80) and (PowerHitbox[1] >= CoordSlayer2[1]) and (PowerHitbox[1] <=CoordSlayer2[1]+124):#Colision del poder con el personaje 2
                    CoordPower=[10000,10000]
                    player2.poder = Poder
                    C_Juego.delete(Imagen)
                    return
                elif StatusPlayer3 and (PowerHitbox[0] >= CoordSlayer3[0]) and (PowerHitbox[0] <= CoordSlayer3[0]+80) and (PowerHitbox[1] >= CoordSlayer3[1]) and (PowerHitbox[1] <=CoordSlayer3[1]+124):#Colision del poder con el personaje 3
                    CoordPower=[10000,10000]
                    player3.poder = Poder
                    C_Juego.delete(Imagen)
                    return
                elif StatusPlayer4 and (PowerHitbox[0] >= CoordSlayer4[0]) and (PowerHitbox[0] <= CoordSlayer4[0]+80) and (PowerHitbox[1] >= CoordSlayer4[1]) and (PowerHitbox[1] <=CoordSlayer4[1]+124):#Colision del poder con el personaje 4
                    CoordPower=[10000,10000]
                    player4.poder = Poder
                    C_Juego.delete(Imagen)
                    return
                else:
                    C_Juego.coords(Imagen,CoordPower[0], CoordPower[1]+1)#Movimiento del personaje
                    WindGame.after(5, lambda: RecursionMovPower(Imagen,Poder)) #Llamada recursiva


        def generaPowers(): #Funcion que genera un thread que lleva a la creacion de los poderes que caen
            global Tiempo, CantPlayers
                
            if Tiempo==0 or CantPlayers <= 1: #Si el tiempo se acaba o la cantidad de jugadores vivos es 1 la funcion termina
                return
            else:
                x=GeneraRandom(3) #Se genera un numero aleatorio el cual corresponde a los poderes que van a caer. 1 para force, 2 para jump y 3 para shield
                
                if x == 1: #La condición genera el poder Force
                    Thread(target = PoderMov(C_Juego.Force, "Force")).start()
                elif x == 2:#La condición genera el poder Jump
                    Thread(target = PoderMov(C_Juego.Jump, "Jump")).start()
                else:#La condición genera el poder Shield
                    Thread(target = PoderMov(C_Juego.Shield, "Shield")).start()
                    
                WindGame.after(7000, lambda: generaPowers())

        def actualizaScorePlayer(Jugador): #Actualiza los árboles de los jugadores cada vez que alguno toma un nodo
            global Score1, Score2, Score3, Score4
            
            if Jugador == 1:
                lb_P1.config( text= ("Player 1 Tree  PTS:", Score1), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))
            elif Jugador ==2:
                lb_P2.config( text= ("Player 1 Tree  PTS:", Score2), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))
            elif Jugador ==3:
                lb_P3.config( text= ("Player 1 Tree  PTS:", Score3), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))
            elif Jugador ==4:
                lb_P4.config( text= ("Player 1 Tree  PTS:", Score4), bg ='Black', fg = 'Yellow', font =("Goudy Stout", 10))

        def actualizaLabelTree(Jugador, Texto): #Actualiza los árboles de los jugadores cada vez que alguno toma un nodo
            if Jugador == 1:
                lb_Tree1.config(text= ("→", Texto), bg ='Black', fg = 'Yellow', font =("Arial 9"))
            elif Jugador ==2:
                lb_Tree2.config(text= ("→", Texto), bg ='Black', fg = 'Yellow', font =("Arial 9"))
            elif Jugador ==3:
                lb_Tree3.config(text= ("→", Texto), bg ='Black', fg = 'Yellow', font =("Arial 9"))
            elif Jugador ==4:
                lb_Tree4.config(text= ("→", Texto), bg ='Black', fg = 'Yellow', font =("Arial 9"))
        
        def player1Tree(Nodo, Objetivo):
            
            global Build, Elementos1, Score1, Elementos

            if Build == Objetivo:
                
                Texto = ""
                Elementos1+=1
                
                if Build == "AVL":
                    
                    player1Avl.insert(Nodo)
                    Texto = player1Avl.preShow(player1Avl.root)
                    #actualizaLabelTree(1, player1Avl.preShow(player1Avl.root))
                    
                elif Build == "BST":
                    
                    player1BST.insert(Nodo)
                    Texto = player1BST.PrintTree()
                    #actualizaLabelTree(1, player1BST.PrintTree())
                    
                elif Build == "B":
                
                    player1B.insert(Nodo)
                    Texto = player1B.print_order()
                    #actualizaLabelTree(1, player1B.print_order())

                elif Build == "SPLAY":
                
                    player1Splay.insert(Nodo)
                    Texto = player1Splay.pretty_print()
                    #actualizaLabelTree(1, player1Splay.pretty_print())

                actualizaLabelTree(1, Texto)

                if Elementos == Elementos1:
                    Score1 +=1
                    actualizaScorePlayer(1)
                
            else:
                Elementos1 = 0
                player1Avl.delete()
                player1Avl.delete()
                player1Avl.delete()
                player1BST.delete()
                player1BST.delete()
                player1BST.delete()
                player1B.delete()
                player1B.delete()
                player1B.delete()
                player1Splay.deleteTree()
                player1Splay.deleteTree()
                player1Splay.deleteTree()
                actualizaLabelTree(1, "")
                

        def player2Tree(Nodo, Objetivo):
            
            global Build, Elementos2, Score2, Elementos
            
            if Build == Objetivo:
                
                Texto = ""
                Elementos2+=1
                
                if Build == "AVL":
                    
                    player2Avl.insert(Nodo)
                    Texto = player2Avl.preShow(player2Avl.root)
                    #actualizaLabelTree(1, player1Avl.preShow(player1Avl.root))
                    
                elif Build == "BST":
                    
                    player2BST.insert(Nodo)
                    Texto = player2BST.PrintTree()
                    #actualizaLabelTree(1, player1BST.PrintTree())
                    
                elif Build == "B":
                
                    player2B.insert(Nodo)
                    Texto = player2B.print_order()
                    #actualizaLabelTree(1, player1B.print_order())

                elif Build == "SPLAY":
                
                    player2Splay.insert(Nodo)
                    Texto = player2Splay.pretty_print()
                    #actualizaLabelTree(1, player1Splay.pretty_print())

                actualizaLabelTree(2, Texto)

                if Elementos == Elementos2:
                    Score2 +=1
                    actualizaScorePlayer(2)
                
            else:
                Elementos2 = 0
                player2Avl.delete()
                player2Avl.delete()
                player2Avl.delete()
                player2BST.delete()
                player2BST.delete()
                player2BST.delete()
                player2B.delete()
                player2B.delete()
                player2B.delete()
                player2Splay.deleteTree()
                player2Splay.deleteTree()
                player2Splay.deleteTree()
                actualizaLabelTree(2, "")
            
        def player3Tree(Nodo, Objetivo):
            
            global Build, Elementos3, Score3, Elementos
            
            if Build == Objetivo:
                
                Texto = ""
                Elementos3+=1
                
                if Build == "AVL":
                    
                    player3Avl.insert(Nodo)
                    Texto = player3Avl.preShow(player3Avl.root)
                    #actualizaLabelTree(1, player1Avl.preShow(player1Avl.root))
                    
                elif Build == "BST":
                    
                    player3BST.insert(Nodo)
                    Texto = player3BST.PrintTree()
                    #actualizaLabelTree(1, player1BST.PrintTree())
                    
                elif Build == "B":
                
                    player3B.insert(Nodo)
                    Texto = player3B.print_order()
                    #actualizaLabelTree(1, player1B.print_order())

                elif Build == "SPLAY":
                
                    player3Splay.insert(Nodo)
                    Texto = player3Splay.pretty_print()
                    #actualizaLabelTree(1, player1Splay.pretty_print())

                actualizaLabelTree(3, Texto)

                if Elementos == Elementos3:
                    Score3 +=1
                    actualizaScorePlayer(3)
                
            else:
                Elementos3 = 0
                player3Avl.delete()
                player3Avl.delete()
                player3Avl.delete()
                player3BST.delete()
                player3BST.delete()
                player3BST.delete()
                player3B.delete()
                player3B.delete()
                player3B.delete()
                player3Splay.deleteTree()
                player3Splay.deleteTree()
                player3Splay.deleteTree()
                actualizaLabelTree(3, "")
            
        def player4Tree(Nodo, Objetivo):
            
            global Build, Elementos4, Score4, Elementos
            
            if Build == Objetivo:
                
                Texto = ""
                Elementos4+=1
                
                if Build == "AVL":
                    
                    player4Avl.insert(Nodo)
                    Texto = player4Avl.preShow(player4Avl.root)
                    #actualizaLabelTree(1, player1Avl.preShow(player1Avl.root))
                    
                elif Build == "BST":
                    
                    player4BST.insert(Nodo)
                    Texto = player4BST.PrintTree()
                    #actualizaLabelTree(1, player1BST.PrintTree())
                    
                elif Build == "B":
                
                    player4B.insert(Nodo)
                    Texto = player4B.print_order()
                    #actualizaLabelTree(1, player1B.print_order())

                elif Build == "SPLAY":
                
                    player4Splay.insert(Nodo)
                    Texto = player4Splay.pretty_print()
                    #actualizaLabelTree(1, player1Splay.pretty_print())

                actualizaLabelTree(4, Texto)

                if Elementos == Elementos4:
                    Score4 +=1
                    actualizaScorePlayer(4)
                
            else:
                Elementos4 = 0
                player4Avl.delete()
                player4Avl.delete()
                player4Avl.delete()
                player4BST.delete()
                player4BST.delete()
                player4BST.delete()
                player4B.delete()
                player4B.delete()
                player4B.delete()
                player4Splay.deleteTree()
                player4Splay.deleteTree()
                player4Splay.deleteTree()
                actualizaLabelTree(4, "")

        def treeMov(Img, Num, Obj):
            
            Nodo = C_Juego.create_image((random.randint(50 , 1100)),50 ,anchor = NW ,image = Img)

            Thread(target = recursionMovArbol(Nodo,Num, Obj)).start()

        def recursionMovArbol(Imagen, Nodo, Objetivo):

            global Build, Tiempo, CoordSlayer1, CoordSlayer2, CoordSlayer3, CoordSlayer4, StatusPlayer1, StatusPlayer2, StatusPlayer3, StatusPlayer4
            
            CoordTree = C_Juego.coords(Imagen)

            TreeHitbox = [C_Juego.coords(Imagen)[0]+25, C_Juego.coords(Imagen)[1]+60] #Establece el hitbox del misil
            
            if Tiempo == 0 or CoordTree[1] >= 800 or CantPlayers <= 1:
                CoordTree=[10000,10000]
                C_Juego.delete(Imagen)
                return
            else:
                if  StatusPlayer1 and (TreeHitbox[0] >= CoordSlayer1[0]) and (TreeHitbox[0] <= CoordSlayer1[0]+80) and (TreeHitbox[1] >= CoordSlayer1[1]) and (TreeHitbox[1] <=CoordSlayer1[1]+124):#Colision del nodo que cae con el personaje 1
                    C_Juego.delete(Imagen)
                    TreeHitbox = [1000,1000]
                    CoordTree=[10000,10000]
                    player1Tree(Nodo, Objetivo)
                    return
                elif StatusPlayer2 and (TreeHitbox[0] >= CoordSlayer2[0]) and (TreeHitbox[0] <= CoordSlayer2[0]+80) and (TreeHitbox[1] >= CoordSlayer2[1]) and (TreeHitbox[1] <=CoordSlayer2[1]+124):#Colision del  nodo que cae con el personaje 2
                    C_Juego.delete(Imagen)
                    TreeHitbox = [1000,1000]
                    CoordTree=[10000,10000]
                    player2Tree(Nodo, Objetivo)
                    return
                elif StatusPlayer3 and (TreeHitbox[0] >= CoordSlayer3[0]) and (TreeHitbox[0] <= CoordSlayer3[0]+80) and (TreeHitbox[1] >= CoordSlayer3[1]) and (TreeHitbox[1] <=CoordSlayer3[1]+124):#Colision del  nodo que cae con el personaje 3
                    C_Juego.delete(Imagen)
                    TreeHitbox = [1000,1000]
                    CoordTree=[10000,10000]
                    player3Tree(Nodo, Objetivo)
                    return
                elif StatusPlayer4 and (TreeHitbox[0] >= CoordSlayer4[0]) and (TreeHitbox[0] <= CoordSlayer4[0]+80) and (TreeHitbox[1] >= CoordSlayer4[1]) and (TreeHitbox[1] <=CoordSlayer4[1]+124) and StatusPlayer4:#Colision del  nodo que cae con el personaje 4
                    C_Juego.delete(Imagen)
                    TreeHitbox = [1000,1000]
                    CoordTree=[10000,10000]
                    player4Tree(Nodo, Objetivo)
                    return
                else:
                    C_Juego.coords(Imagen,CoordTree[0], CoordTree[1]+1)#Movimiento del personaje
                    WindGame.after(10, lambda: recursionMovArbol(Imagen, Nodo, Objetivo)) #Llamada recursiva

                    
        def generaAvl(): #Funcion encargada de generar un tipo de nodo específico del árbol AVL
            global Tiempo, CantPlayers
                
            if Tiempo==0 or CantPlayers <= 1: #Si el tiempo se acaba o la cantidad de jugadores vivos es 1 la funcion termina
                return
            else:
                x=GeneraRandom(10) #Se genera un numero aleatorio el cual corresponde a los poderes que van a caer. 1 para force, 2 para jump y 3 para shield
                
                if x == 1: #Las condiciones para generar un tipo de nodo en específico
                    Thread(target = treeMov(C_Juego.AVL1, 1, "AVL")).start()
                elif x == 2:
                    Thread(target = treeMov(C_Juego.AVL2, 2, "AVL")).start()
                elif x == 3:
                    Thread(target = treeMov(C_Juego.AVL3, 3, "AVL")).start()
                elif x == 4:
                    Thread(target = treeMov(C_Juego.AVL4, 4, "AVL")).start()
                elif x == 5:
                    Thread(target = treeMov(C_Juego.AVL5, 5, "AVL")).start()
                elif x == 6:
                    Thread(target = treeMov(C_Juego.AVL6, 6, "AVL")).start()
                elif x == 7:
                    Thread(target = treeMov(C_Juego.AVL7, 7, "AVL")).start()
                elif x == 8:
                    Thread(target = treeMov(C_Juego.AVL8, 8, "AVL")).start()
                elif x == 9:
                    Thread(target = treeMov(C_Juego.AVL9, 9, "AVL")).start()
                elif x == 10:
                    Thread(target = treeMov(C_Juego.AVL10, 10, "AVL")).start()
                    
                WindGame.after(5000, lambda: generaAvl())


        def generaBST(): #Funcion encargada de generar un tipo de nodo específico del árbol BST
            global Tiempo, CantPlayers
                
            if Tiempo==0 or CantPlayers <= 1: #Si el tiempo se acaba o la cantidad de jugadores vivos es 1 la funcion termina
                return
            else:
                x=GeneraRandom(10) #Se genera un numero aleatorio el cual corresponde a los poderes que van a caer. 1 para force, 2 para jump y 3 para shield
                
                if x == 1: #Las condiciones para generar un tipo de nodo en específico
                    Thread(target = treeMov(C_Juego.BST1, 1, "BST")).start()
                elif x == 2:
                    Thread(target = treeMov(C_Juego.BST2, 2, "BST")).start()
                elif x == 3:
                    Thread(target = treeMov(C_Juego.BST3, 3, "BST")).start()
                elif x == 4:
                    Thread(target = treeMov(C_Juego.BST4, 4, "BST")).start()
                elif x == 5:
                    Thread(target = treeMov(C_Juego.BST5, 5, "BST")).start()
                elif x == 6:
                    Thread(target = treeMov(C_Juego.BST6, 6, "BST")).start()
                elif x == 7:
                    Thread(target = treeMov(C_Juego.BST7, 7, "BST")).start()
                elif x == 8:
                    Thread(target = treeMov(C_Juego.BST8, 8, "BST")).start()
                elif x == 9:
                    Thread(target = treeMov(C_Juego.BST9, 9, "BST")).start()
                elif x == 10:
                    Thread(target = treeMov(C_Juego.BST10, 10, "BST")).start()
                    
                WindGame.after(5000, lambda: generaBST())


        def generaSplay(): #Funcion encargada de generar un tipo de nodo específico del árbol Splay
            global Tiempo, CantPlayers
                
            if Tiempo==0 or CantPlayers <= 1: #Si el tiempo se acaba o la cantidad de jugadores vivos es 1 la funcion termina
                return
            else:
                x=GeneraRandom(10) #Se genera un numero aleatorio el cual corresponde a los poderes que van a caer. 1 para force, 2 para jump y 3 para shield
                
                if x == 1: #Las condiciones para generar un tipo de nodo en específico
                    Thread(target = treeMov(C_Juego.SPLAY1, 1, "SPLAY")).start()
                elif x == 2:
                    Thread(target = treeMov(C_Juego.SPLAY2, 2, "SPLAY")).start()
                elif x == 3:
                    Thread(target = treeMov(C_Juego.SPLAY3, 3, "SPLAY")).start()
                elif x == 4:
                    Thread(target = treeMov(C_Juego.SPLAY4, 4, "SPLAY")).start()
                elif x == 5:
                    Thread(target = treeMov(C_Juego.SPLAY5, 5, "SPLAY")).start()
                elif x == 6:
                    Thread(target = treeMov(C_Juego.SPLAY6, 6, "SPLAY")).start()
                elif x == 7:
                    Thread(target = treeMov(C_Juego.SPLAY7, 7, "SPLAY")).start()
                elif x == 8:
                    Thread(target = treeMov(C_Juego.SPLAY8, 8, "SPLAY")).start()
                elif x == 9:
                    Thread(target = treeMov(C_Juego.SPLAY9, 9, "SPLAY")).start()
                elif x == 10:
                    Thread(target = treeMov(C_Juego.SPLAY10, 10, "SPLAY")).start()
                    
                WindGame.after(5000, lambda: generaSplay())


        def generaB(): #Funcion encargada de generar un tipo de nodo específico del árbol B
            global Tiempo, CantPlayers
                
            if Tiempo==0 or CantPlayers <= 1: #Si el tiempo se acaba o la cantidad de jugadores vivos es 1 la funcion termina
                return
            else:
                x=GeneraRandom(10) #Se genera un numero aleatorio el cual corresponde a los poderes que van a caer. 1 para force, 2 para jump y 3 para shield
                
                if x == 1: #Las condiciones para generar un tipo de nodo en específico
                    Thread(target = treeMov(C_Juego.B1, 1, "B")).start()
                elif x == 2:
                    Thread(target = treeMov(C_Juego.B2, 2, "B")).start()
                elif x == 3:
                    Thread(target = treeMov(C_Juego.B3, 3, "B")).start()
                elif x == 4:
                    Thread(target = treeMov(C_Juego.B4, 4, "B")).start()
                elif x == 5:
                    Thread(target = treeMov(C_Juego.B5, 5, "B")).start()
                elif x == 6:
                    Thread(target = treeMov(C_Juego.B6, 6, "B")).start()
                elif x == 7:
                    Thread(target = treeMov(C_Juego.B7, 7, "B")).start()
                elif x == 8:
                    Thread(target = treeMov(C_Juego.B8, 8, "B")).start()
                elif x == 9:
                    Thread(target = treeMov(C_Juego.B9, 9, "B")).start()
                elif x == 10:
                    Thread(target = treeMov(C_Juego.B10, 10, "B")).start()
                    
                WindGame.after(5000, lambda: generaB())

                
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
                
        #Creación de Personajes

        #Creación de Objetos del Juego

        C_Juego.Force = General.cargarImg2('Power\Force.png')#Creación del Poder Force
        C_Juego.Jump = General.cargarImg2('Power\Jump.png')#Creación del Poder Jump
        C_Juego.Shield = General.cargarImg2('Power\Shield.png')#Creación del Poder Shield


        C_Juego.AVL1 = General.cargarImg2('Avl\Rama1.png') #Creación de las imágenes del árbol AVL
        C_Juego.AVL2 = General.cargarImg2('Avl\Rama2.png')
        C_Juego.AVL3 = General.cargarImg2('Avl\Rama3.png')
        C_Juego.AVL4 = General.cargarImg2('Avl\Rama4.png')
        C_Juego.AVL5 = General.cargarImg2('Avl\Rama5.png')
        C_Juego.AVL6 = General.cargarImg2('Avl\Rama6.png')
        C_Juego.AVL7 = General.cargarImg2('Avl\Rama7.png')
        C_Juego.AVL8 = General.cargarImg2('Avl\Rama8.png')
        C_Juego.AVL9 = General.cargarImg2('Avl\Rama9.png')
        C_Juego.AVL10 = General.cargarImg2('Avl\Rama10.png')

        C_Juego.BST1 = General.cargarImg2('BST\Rama1.png')#Creación de las imágenes del árbol BST
        C_Juego.BST2 = General.cargarImg2('BST\Rama2.png')
        C_Juego.BST3 = General.cargarImg2('BST\Rama3.png')
        C_Juego.BST4 = General.cargarImg2('BST\Rama4.png')
        C_Juego.BST5 = General.cargarImg2('BST\Rama5.png')
        C_Juego.BST6 = General.cargarImg2('BST\Rama6.png')
        C_Juego.BST7 = General.cargarImg2('BST\Rama7.png')
        C_Juego.BST8 = General.cargarImg2('BST\Rama8.png')
        C_Juego.BST9 = General.cargarImg2('BST\Rama9.png')
        C_Juego.BST10 = General.cargarImg2('BST\Rama10.png')

        C_Juego.B1 = General.cargarImg2('B\Rama1.png')#Creación de las imágenes del árbol B
        C_Juego.B2 = General.cargarImg2('B\Rama2.png')
        C_Juego.B3 = General.cargarImg2('B\Rama3.png')
        C_Juego.B4 = General.cargarImg2('B\Rama4.png')
        C_Juego.B5 = General.cargarImg2('B\Rama5.png')
        C_Juego.B6 = General.cargarImg2('B\Rama6.png')
        C_Juego.B7 = General.cargarImg2('B\Rama7.png')
        C_Juego.B8 = General.cargarImg2('B\Rama8.png')
        C_Juego.B9 = General.cargarImg2('B\Rama9.png')
        C_Juego.B10 = General.cargarImg2('B\Rama10.png')


        C_Juego.SPLAY1 = General.cargarImg2('Splay\Rama1.png')#Creación de las imágenes del árbol Splay
        C_Juego.SPLAY2 = General.cargarImg2('Splay\Rama2.png')
        C_Juego.SPLAY3 = General.cargarImg2('Splay\Rama3.png')
        C_Juego.SPLAY4 = General.cargarImg2('Splay\Rama4.png')
        C_Juego.SPLAY5 = General.cargarImg2('Splay\Rama5.png')
        C_Juego.SPLAY6 = General.cargarImg2('Splay\Rama6.png')
        C_Juego.SPLAY7 = General.cargarImg2('Splay\Rama7.png')
        C_Juego.SPLAY8 = General.cargarImg2('Splay\Rama8.png')
        C_Juego.SPLAY9 = General.cargarImg2('Splay\Rama9.png')
        C_Juego.SPLAY10 = General.cargarImg2('Splay\Rama10.png')
        

        #C_Juego.Pixel = General.cargarImg2('Power\Force.png')
        #Pixel = C_Juego.create_image(330,460,anchor = NW, image =C_Juego.Pixel)

        

        #Creación de Objetos del Juego

                
        #Llamada de funciones

        GeneraObjetivo()

        C_Juego.bind("<KeyPress>", MovDoom) #Llamada a la funcion que contiene las acciones del personaje
        C_Juego.focus_set() #Hace que el Canvas se enfoque en la accion a realizar por parte de la tecla


        Thread(target=Timer()).start()      
        Thread(target=Objetivo()).start()        
        Thread(target=TimerObj()).start()
        Thread(target=posPlayer1()).start()
        Thread(target=posPlayer2()).start()
        Thread(target=gravity1()).start()
        Thread(target=gravity2()).start()

        
        Thread(target = generaAvl()).start()
        Thread(target = generaBST()).start()
        Thread(target = generaSplay()).start()
        Thread(target = generaB()).start()
        Thread(target = generaPowers()).start()
        
        
        
        #Llamada de funciones


    #End InterfazJuego

        
#End Class General
            
General.Principal()


















