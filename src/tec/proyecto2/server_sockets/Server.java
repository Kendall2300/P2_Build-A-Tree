package tec.proyecto2.server_sockets;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

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
        String tosend = "Bienvenido";
        int port = 6000;
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println(tosend);
        /***
         * EL while(true) proporciona el bucle para que así no se cierre el servidor y se pierda contacto
         */
        while(true){
            Socket socket = serverSocket.accept();
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            InputStream dis = socket.getInputStream();
            try {
                dos.writeUTF(tosend);
                String message = new String(dis.readAllBytes());
                System.out.println("Mensaje recibido: " + message);
                /***
                 * En esta función if se recibirá un mensaje del cliente a la hora de tocar el botón "play", de
                 * esta manera el servidor mandará por medio de socket el challenge correspondiente al juego de
                 * manera aleatoria con el Random
                 */
                if(message.equals("Play")) {
                    Random rand = new Random();
                    int upperbound = 4;
                    int int_random = rand.nextInt(upperbound);

                    if(int_random==0){
                        tosend = "Build BST";
                        dos.writeUTF(tosend);
                        System.out.println("Este es tu challenge: " + tosend);
                    }
                    else if(int_random==1){
                        tosend = "Build B Tree";
                        dos.writeUTF(tosend);
                        System.out.println("Este es tu challenge: " + tosend);

                    } else if (int_random==2) {
                        tosend = "Build AVL";
                        dos.writeUTF(tosend);
                        System.out.println("Este es tu challenge: " + tosend);
                    } else if(int_random == 3){
                        tosend = "Build Splay";
                        dos.writeUTF(tosend);
                        System.out.println("Este es tu challenge: " + tosend);
                    }
                }
                /***
                 * Esta función if cierra el servidor cuando se cierre el cliente correspondiente
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
