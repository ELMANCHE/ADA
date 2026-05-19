/**
 * Alumno: Elias Manchego Navarro 
 * PROBLEMA 3. Contar inversiones en un arreglo
 * Descripción: Dado un arreglo de enteros, una inversión se define como un par de índices j tales que:
 * i<j
 * arr[i]>arr[j]
 * Es decir, ocurre una inversión cuando un elemento que aparece antes en el arreglo es mayor que uno que aparece después.
*/

import java.util.Arrays;


public class Problema3 {

    // casi muero en este ejercicio pero al escuchar golden de las guerras del kpop me dio animo
    // esta parte es la implementacion del conteo usando el merge sort modificado para contar las inversiones cruzadas entre las mitades del arreglo
    public long scottycuentainversiones(int[] arreglo) {
        if (arreglo == null || arreglo.length < 2) {
            return 0;
        }
        int[] copiaArreglo = arreglo.clone();
        return scottydivideycuenta(copiaArreglo, 0, copiaArreglo.length - 1);
    }

    private long scottydivideycuenta(int[] arreglo, int inicio, int fin) {
        long conteo = 0;
        if (inicio < fin) {
            int medio = inicio + (fin - inicio) / 2;

            conteo += scottydivideycuenta(arreglo, inicio, medio);
            conteo += scottydivideycuenta(arreglo, medio + 1, fin);
            conteo += fusionarYContarCruzadas(arreglo, inicio, medio, fin);
        }
        return conteo;
    }
    // esta parte es la implementacion del conteo usando el merge sort modificado 
    private long fusionarYContarCruzadas(int[] arreglo, int inicio, int medio, int fin) {
        int[] izquierda = Arrays.copyOfRange(arreglo, inicio, medio + 1);
        int[] derecha = Arrays.copyOfRange(arreglo, medio + 1, fin + 1);

        int i = 0, j = 0, k = inicio;
        long cruzeinversiones = 0;
        // aca mientras se fuciona se cuentan las inversiones cruzadas
        while (i < izquierda.length && j < derecha.length) {
            if (izquierda[i] <= derecha[j]) {
                arreglo[k++] = izquierda[i++];
            // cada vez que se toma un elemento de la derecha que es menor que el de la izquierda
            } else {
                arreglo[k++] = derecha[j++];
                cruzeinversiones += (izquierda.length - i);
            }
        }

        while (i < izquierda.length) {
            arreglo[k++] = izquierda[i++];
        }
        while (j < derecha.length) {
            arreglo[k++] = derecha[j++];
        }

        return cruzeinversiones;
    }
}