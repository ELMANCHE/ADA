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

}