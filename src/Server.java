import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server {
    public static void main(String[] args) throws IOException {
        int port = 6000;
        ServerSocket serverSocket = new ServerSocket(port);
        while(true){
            Socket socket = serverSocket.accept();
            Scanner scanner = new Scanner(System.in);
            InputStream dis = socket.getInputStream();
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            try {
                String tosend = scanner.nextLine();
                dos.writeUTF(tosend);
                System.out.println("Mensaje enviado ");
                String message = new String(dis.readAllBytes());
                System.out.println("Mensaje recibido: " + message);
                if(message.equals("Exit")) {
                    System.out.println("Cerrando el servidor");
                    socket.close();
                    dis.close();
                    dos.close();
                    scanner.close();
                    System.out.println("Se cerró el servidor");
                    break;
                }

            }catch (Exception e){
                e.printStackTrace();
            }


        }
    }
}
