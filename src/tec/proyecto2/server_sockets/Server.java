package tec.proyecto2.server_sockets;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;


/***
 * Clase Server la cual está encargada de escuchar por medio de sockets cuando un jugador obtiene un token,
 * además de crear los challenges correspondientes.
 */
public class Server {
    public static void main(String[] args) throws IOException {
        /***
         Para la comunicación por medio de sockets en el server ya está establecido un puerto en el cuál será
         escuchado el cliente correspondiente
         */
        String tosend ="Bienvenido";
        int port = 6000;
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println(tosend);
        /***
          EL while(true) proporciona el bucle para que así no se cierre el servidor y se pierda contacto
         */
        while(true){
            Socket socket = serverSocket.accept();
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            DataInputStream dis = new DataInputStream(socket.getInputStream());
            try {
                dos.writeUTF(tosend);
                String message = new String(dis.readAllBytes());
                System.out.println(message);
                

                /***
                 * Este condicional if cierra el servidor cuando se cierre el cliente correspondiente
                 */
                if(message.equals("Exit")) {
                    System.out.println("Cerrando el servidor");
                    socket.close();
                    dis.close();
                    dos.close();
                    System.out.println("Se cerró el servidor");
                    break;
                }

            }catch (Exception e){
                e.printStackTrace();
            }


        }
    }
}
