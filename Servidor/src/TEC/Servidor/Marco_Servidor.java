package TEC.Servidor;

import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.net.*;

/**
 * Marco_Servidor
 * Esta clase se encarga de crear el marco del servidor y manejar los sockets
 *
 * @author Kendall Martinez, Daniel Montoya && Gustavo Gamboa
 * @version 1.0
 */
public class Marco_Servidor extends JFrame implements Runnable {

    private JTextArea areatexto;

    /**
     * Marco_Servidor
     * Este metodo se encarga de definir los parametros que se necesitan para que el servidor se muestre como un panel y sea
     * mas sencillo visualizar lo que sucede.
     */
    public Marco_Servidor(){
        setBounds(1200,300,280,350);
        JPanel milamina=new JPanel();
        milamina.setLayout(new BorderLayout());

        areatexto=new JTextArea();
        milamina.add(areatexto,BorderLayout.CENTER);
        add(milamina);
        setVisible(true);

        Thread mihilo=new Thread(this);
        mihilo.start();
    }

    /**
     * run
     * Este metodo es el que se encarga de manejar los datos recibidos y el socket
     */
    public void run(){
        try{
            ServerSocket servidor=new ServerSocket(9999);
            String ip = "127.0.0.1";
            while (true){
                Socket misocket=servidor.accept();

                //areatexto.append();

                misocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

