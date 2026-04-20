public class OrdenamientoMejorado {

    // Bubble Sort mejorado 
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        // mejora de variables para contar operaciones
        int comparaciones = 0;
        int intercambios = 0;
        
        // mejora variable booleana para detectar si ya está ordenado
        boolean swapped;

        for (int i = 0; i < n - 1; i++) {
            swapped = false; // Se resetea en cada vuelta del ciclo externo
            
            // mejora el límite 'n - i - 1' evita revisar lo que ya está en su sitio
            for (int j = 0; j < n - i - 1; j++) {
                comparaciones++; // mejora contar cada comparación
                
                if (arr[j] > arr[j + 1]) {
                    // Intercambio (Swap)
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    
                    intercambios++; // mejora contar cada intercambio
                    swapped = true; // mejora si hubo un cambio, ponemos la bandera en true
                }
            }

            // mejora si después de recorrer el ciclo interno 'swapped' significa que el arreglo ya está ordenado y podemos terminar.
            if (!swapped) {
                break;
            }
        }
        
        // print resultados  
        System.out.println("Comparaciones: " + comparaciones);
        System.out.println("Intercambios: " + intercambios);
    }

    // Selection Sort con contadores
    public static void selectionSort(int[] arr) {
        int n = arr.length;

        int comparaciones = 0;
        int intercambios = 0;

        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;

            for (int j = i + 1; j < n; j++) {
                comparaciones++;
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }

            // Solo intercambia si el mínimo no es ya el elemento actual
            if (minIdx != i) {
                int temp = arr[minIdx];
                arr[minIdx] = arr[i];
                arr[i] = temp;
                intercambios++;
            }
        }

        // print resultados
        System.out.println("Comparaciones: " + comparaciones);
        System.out.println("Intercambios: " + intercambios);
    }
}