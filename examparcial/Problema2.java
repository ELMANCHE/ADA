/**
 * Alumno: Elias Manchego Navarro 
 * PROBLEMA 2. Segundo elemento más grande usando divide y vencerás
 * Descripción: Diseñe un algoritmo utilizando divide y vencerás que encuentre el segundo elemento más grande de un arreglo de enteros.
*/
public class Problema2 {
    
    // esto lo usare para guardar el max y segundo max 
    public static class parejahachikomax {
        public int max;
        public int segundohachicomax;

        public parejahachikomax(int max, int segundohachicomax) {
            this.max = max;
            this.segundohachicomax = segundohachicomax;
        }
    }

    // comenzamos con el dividir y venceras pipipi
    public int buscarsegundohachicomax(int[] arreglo) {
        if (arreglo == null || arreglo.length < 2) {
            throw new IllegalArgumentException("El arreglo debe contener al menos 2 elementos.");
        }
        parejahachikomax resultado = diviryvencerashachiko(arreglo, 0, arreglo.length - 1);
        return resultado.segundohachicomax;
    }

    private parejahachikomax diviryvencerashachiko(int[] arreglo, int inicio, int fin) {
        // comienzo con un solo elemento 
        if (inicio == fin) {
            return new parejahachikomax(arreglo[inicio], Integer.MIN_VALUE);
        }

        // ahora para dos elementos 
        if (fin == inicio + 1) {
            if (arreglo[inicio] > arreglo[fin]) {
                return new parejahachikomax(arreglo[inicio], arreglo[fin]);
            } else {
                return new parejahachikomax(arreglo[fin], arreglo[inicio]);
            }
        }
        // esto es porqie si es mas que 2 elementos ingresa el divide y venceras dividiendo el arreglo a mitades
        int medio = inicio + (fin - inicio) / 2;
        parejahachikomax izq = diviryvencerashachiko(arreglo, inicio, medio);
        parejahachikomax der = diviryvencerashachiko(arreglo, medio + 1, fin);
        // y luego de combinan los resultados de cada mitad para obetenr un maximo global
        int maxGlobal;
        int segundohachicomaxGlobal;

        //combino los resultados 
        if (izq.max > der.max) {
            maxGlobal = izq.max;
            segundohachicomaxGlobal = Math.max(izq.segundohachicomax, der.max);
        } else {
            maxGlobal = der.max;
            segundohachicomaxGlobal = Math.max(der.segundohachicomax, izq.max);
        }
        //
        return new parejahachikomax(maxGlobal, segundohachicomaxGlobal);
    }
}