/**
 * Alumno: Elias Manchego Navarro 
 * PROBLEMA 1. Verificar si un arreglo está ordenado.
 * Descripción: Diseñe un algoritmo recursivo que determine si un arreglo de enteros se encuentra ordenado de menor a mayor.
*/

import java.util.Arrays;

public class Problema1 {

    // main metod for problem1
    public boolean martinaverifica(int[] arreglo) {
        if (arreglo == null) {
            return true;
        }
        return ordenmartina(arreglo, arreglo.length);
    }

    // aca comienza el problema en si 
    private boolean ordenmartina(int[] arreglo, int n) {
        // esto es para saber si el arreglo tiene 0 o 1 elemneto 
        if (n <= 1) {
            return true;
        }

        // para saberlo colocare esto que va al ultimo elemnto y compara con el anterior
        if (arreglo[n - 1] < arreglo[n - 2]) {
            return false; 
        }

        // entonces debo reducir a algo mas peqeuno como un subproblema y asi...
        return ordenmartina(arreglo, n - 1);
    }

    public static void main(String[] args) {
        Problema1 solucion = new Problema1();

        // pruebas que nos dio en el ejercicio
        int[] ejemplo1 = {1, 2, 3, 5, 8};
        int[] ejemplo2 = {1, 4, 2, 8};

        System.out.println("ejercicio1");
        System.out.println("primer arreglo : " + Arrays.toString(ejemplo1) + " = esta ordenado o no matina?: " + solucion.martinaverifica(ejemplo1));
        System.out.println("segundo arreglo : " + Arrays.toString(ejemplo2) + " = esta ordenado o no matina?: " + solucion.martinaverifica(ejemplo2));
    }
}