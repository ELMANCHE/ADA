import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ejercicio2 {

    public static void calcularAntenas(int[] casas, int R) {
        // para comenzar se debe asegurar que este ordenado 
        Arrays.sort(casas);

        List<Integer> posicionesAntenas = new ArrayList<>();
        int i = 0;
        int n = casas.length;

        // aca se recorre
        while (i < n) {
            // en casa cubierta se encuentra la primera casa no cubierta
            int casaNoCubierta = casas[i];

            // luego se coloca la antena en la posición casaNoCubierta + R para cubrir el max
            int posicionAntena = casaNoCubierta + R;
            posicionesAntenas.add(posicionAntena);

            // ahora se omiten las casas que quedan cubiertas por esta antena
            // en otras palabras las casas que estan a la derecha de posicionAntena + R
            while (i < n && casas[i] <= posicionAntena + R) {
                i++;
            }
        }

        // por ultimo se muestran los reusltados
        System.out.println("Antenas colocadas aproximadamente en:");
        for (int pos : posicionesAntenas) {
            System.out.println(pos);
        }
        System.out.println("Cantidad total: " + posicionesAntenas.size());
    }

    public static void main(String[] args) {
        // ejem1
        System.out.println("ejem1");
        int[] casas1 = {1, 2, 7, 11, 20, 21, 30};
        int R1 = 5;
        calcularAntenas(casas1, R1);

        // ejem2
        System.out.println("\nejem2");
        int[] casas2 = {2, 4, 8, 15, 18, 22};
        int R2 = 3;
        calcularAntenas(casas2, R2);
    }
}