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
            try{
                Scanner scanner = new Scanner(System.in);
                InputStream request = socket.getInputStream();
                DataInputStream dis = new DataInputStream(request);
                DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
                String message = new String(dis.readAllBytes());
                System.out.println("Mensaje recibido :" + message);
                String tosend = scanner.nextLine();
                dos.writeUTF(tosend);
                System.out.println("Mensaje enviado");



            } catch(Exception e){
                e.printStackTrace();
            }


        }


    }
}
