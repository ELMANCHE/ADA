public class Main {

    public static void main(String[] args) {
        // casos que se pide en la tarea
        int[][] casos = {
            {5, 3, 8, 2},
            {1, 2, 3, 4, 5},
            {5, 4, 3, 2, 1}
        };

        for (int[] original : casos) {
            System.out.println("\n=======================================");
            System.out.print("PROBANDO ARREGLO: ");
            imprimir(original);
            System.out.println("=======================================");

            //  Sort 
            int[] copiaBubble = original.clone();
            System.out.println("Resultados Bubble Sort Mejorado:");
            OrdenamientoMejorado.bubbleSort(copiaBubble);
            System.out.print("Ordenado: ");
            imprimir(copiaBubble);

            System.out.println("---------------------------------------");

            // selection Sort
            int[] copiaSelection = original.clone();
            System.out.println("Resultados Selection Sort:");
            OrdenamientoMejorado.selectionSort(copiaSelection);
            System.out.print("Ordenado: ");
            imprimir(copiaSelection);
        }
    }

    // print main  
    public static void imprimir(int[] arr) {
        for (int i : arr) System.out.print(i + " ");
        System.out.println();
    }
}