package TEC.Servidor;
import javax.swing.*;

/**
 * Servidor
 * Esta clase se encarga de iniciar el servidor
 *
 * @author Kendall Martinez, Daniel Montoya && Gustavo Gamboa
 * @version 1.0
 */
public class Servidor {
    /**
     * main
     * Este metodo es el cual se encarga de inicializar los parametros que se le sean pasados.
     * @param args Una cadena de strings
     */
    public static void main(String[] args) {
        Marco_Servidor mimarco=new Marco_Servidor();
        mimarco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}

