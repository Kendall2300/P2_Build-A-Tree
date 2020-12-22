package TEC.Servidor;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
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
        setBounds(200,100,450,300);
        JPanel milamina=new JPanel();
        milamina.setBorder(new EmptyBorder(10,10,10,10));
        milamina.setLayout(new BorderLayout(0,0));
        areatexto=new JTextArea();
        milamina.add(areatexto,BorderLayout.CENTER);
        add(milamina);
        setVisible(true);
        milamina.add(new JScrollPane(areatexto));





        Thread mihilo=new Thread(this);
        mihilo.start();
    }

    /**
     * run
     * Este metodo es el que se encarga de manejar los datos recibidos y el socket
     */
    public void run(){
        try{
            ServerSocket servidor=new ServerSocket(6000);
            //String ip = "127.0.0.1";
            String tosend = "Bienvenido";
            areatexto.append("\n" + tosend);
            while (true){
                Socket misocket=servidor.accept();
                DataOutputStream dos = new DataOutputStream(misocket.getOutputStream());
                DataInputStream dis = new DataInputStream(misocket.getInputStream());

                try {
                    dos.writeUTF(tosend);
                    String message = new String(dis.readAllBytes());
                    areatexto.append("\n" + message);

                    if(message.equals("Exit")){
                        areatexto.append("\n" + "Cerrando el servidor");
                        misocket.close();
                        dis.close();
                        dos.close();
                        areatexto.append("\n" + "Se cerró el servidor");
                    }
                } catch(Exception e){
                    e.printStackTrace();
                }


            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

