import java.util.Arrays;

// aca es el principal donde ejecutare todas mis pruebas de los problemas que nos dio
public class Main {
    public static void main(String[] args) {
        System.out.println("prueba de todos los ejercicios\n");

        //problema1
        Problema1 p1 = new Problema1();
        int[] arreglo1 = {1, 2, 3, 5, 8};
        int[] arreglo2 = {1, 4, 2, 8};
        
        System.out.println("ejercicio 1");
        System.out.println("Arreglo 1: " + Arrays.toString(arreglo1) + "  esta ordenado mor?: " + p1.martinaverifica(arreglo1));
        System.out.println("Arreglo 2: " + Arrays.toString(arreglo2) + "  esta ordenado mor?: " + p1.martinaverifica(arreglo2));
        System.out.println();

        //problema2
        Problema2 p2 = new Problema2();
        int[] datosP2 = {8, 3, 10, 5, 7};
        
        System.out.println("ejercicio 2");
        System.out.println("arreglo: " + Arrays.toString(datosP2));
        System.out.println("segundo elemento más grande: " + p2.buscarsegundohachicomax(datosP2));
        System.out.println();

        //problema3
        Problema3 p3 = new Problema3();
        int[] arreglo = {3, 1, 2};
        
        System.out.println("ejercicio 3");
        System.out.println("arreglo: " + Arrays.toString(arreglo));
        System.out.println("total de inversiones encontradas: " + p3.scottycuentainversiones(arreglo));
    }
}
